from django.test import TestCase
import json

user1 = {
    "email":"egoodman3141@gmail.com", 
    "username":"EdmundGoodman", 
    "first_name":"Edmund",
    "last_name":"Goodman",
    "password":"12345",
    "profile":{
        "biography":"I am a student who wants to mentor",
        "business_area":"Computer Science",
        "job_title":"Student",
        "mentor":True,
        "time_available":1.0
    }
}

user2 = {
    "email":"foobar@gmail.com",
    "username":"FooBar",
    "first_name":"Foo",
    "last_name":"Bar",
    "password":"12345",
    "profile":{
        "biography":"I am a student who wants to be mentored",
        "business_area":"Computer Science",
        "job_title":"Student",
        "mentor":False,
        "time_available":1.0
    }
}

class AuthTestCase(TestCase):
    
    def test_login_sequence(self):
        register_response = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response.status_code // 100, 2)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(login_response.status_code // 100, 2)
        token = json.loads(login_response.content)['token']
        logout_response = self.client.get('/api/users/logout/', HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(logout_response.status_code // 100, 2)

    def test_register_twice(self):
        register_response_1 = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response_1.status_code // 100, 2)
        register_response_2 = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response_2.status_code, 400)

    def test_login_twice(self):
        register_response = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response.status_code // 100, 2)
        login_response_1 = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(login_response_1.status_code // 100, 2)
        token_1 = json.loads(login_response_1.content)['token']
        login_response_2 = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        token_2 = json.loads(login_response_2.content)['token']
        self.assertEqual(token_1, token_2)

    def test_log_back_in(self):
        register_response = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response.status_code // 100, 2)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(login_response.status_code // 100, 2)
        token_1 = json.loads(login_response.content)['token']
        logout_response = self.client.get('/api/users/logout/', HTTP_AUTHORIZATION='Token {}'.format(token_1))
        self.assertEqual(login_response.status_code // 100, 2)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        token_2 = json.loads(login_response.content)['token']
        self.assertNotEqual(token_1, token_2)

    def test_user_deletion(self):
        register_response = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response.status_code // 100, 2)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(login_response.status_code // 100, 2)
        token = json.loads(login_response.content)['token']
        response = self.client.delete('/api/users/delete/', HTTP_AUTHORIZATION='Token {}'.format(token)) 
        self.assertEqual(response.status_code // 100, 2)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(login_response.status_code, 400)

class TopicTestCase(TestCase):
    def test_topics(self):
        topics = set(['Django', 'Python', 'Java'])
        for t in topics:
            response = self.client.post('/api/topics/', {'sw_type':t}, content_type='application/json') 
            self.assertEqual(response.status_code // 100, 2)

        while topics:
            #gets topics and checks if they're equal
            response = self.client.get('/api/topics/')
            self.assertEqual(response.status_code // 100, 2)
            topics_response = set([d['sw_type'] for d in json.loads(response.content)])
            self.assertEqual(topics, topics_response)

            #deletes a topic
            t = topics.pop()
            response = self.client.delete('/api/topics/', {'sw_type':t}, content_type='application/json')
            self.assertEqual(response.status_code // 100, 2)
        response = self.client.get('/api/topics/')
        self.assertEqual(response.status_code // 100, 2)
        topics_response = set([d['sw_type'] for d in json.loads(response.content)])
        self.assertEqual(topics, topics_response)

class UserTestCase(TestCase):
    def setUp(self):
        #registers and logins in the user to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token = json.loads(login_response.content)['token']

        #adds topics to the API
        self.topics = ['Django', 'Python', 'Java']
        for t in self.topics:
            self.client.post('/api/topics/', {'sw_type':t}, content_type='application/json') 

    def test_profile(self):
        response = self.client.get('/api/users/profile/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        profile = json.loads(response.content)
        res = True
        for k,v in user1['profile'].items():
            if not(k in profile and profile[k] == v):
                res = False 
                break
        self.assertTrue(res)

    def test_account(self):
        #gets and checks original account details
        response = self.client.get('/api/users/account/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        account = json.loads(response.content)
        res = True
        for k, v in account.items():
            if not(k in user1 and user1[k] == v):
                res = False
                break
        self.assertTrue(res)

        #updates account details
        changes = {'first_name':'Deadmund', 'last_name':'Badman'}
        response = self.client.patch('/api/users/account/', changes, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        #gets and checks updated account details
        response = self.client.get('/api/users/account/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        account = json.loads(response.content)
        res = True
        for k, v in account.items():
            if not(k in user1 and ((user1[k] == v and k not in changes) or (k in changes and changes[k] == v))):
                res = False
                break
        self.assertTrue(res)

    def test_sw(self):
        #adds strengths and weaknesses for the user
        response = self.client.post('/api/users/strengths/', {'sw_type':self.topics[0]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.post('/api/users/strengths/', {'sw_type':self.topics[1]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.post('/api/users/weaknesses/', {'sw_type':self.topics[2]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        #gets and compares strengths and weaknesses
        response = self.client.get('/api/users/strengths/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        strengths = [d['sw_type'] for d in json.loads(response.content)]
        self.assertEqual(strengths, self.topics[0:2])

        response = self.client.get('/api/users/weaknesses/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        weaknesses = [d['sw_type'] for d in json.loads(response.content)]
        self.assertEqual(weaknesses, self.topics[2:3])

        #deletes strengths a weaknesses
        response = self.client.delete('/api/users/strengths/', {'sw_type':self.topics[0]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.delete('/api/users/weaknesses/', {'sw_type':self.topics[2]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        #gets and compares modified strengths and weaknesses
        response = self.client.get('/api/users/strengths/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        strengths = [d['sw_type'] for d in json.loads(response.content)]
        self.assertEqual(strengths, self.topics[1:2])

        response = self.client.get('/api/users/weaknesses/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        weaknesses = [d['sw_type'] for d in json.loads(response.content)]
        self.assertEqual(weaknesses, [])

        #checks if a strength can also be a weakness (this shouldn't happen)
        response = self.client.post('/api/users/weaknesses/', {'sw_type':self.topics[1]}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        response = self.client.get('/api/users/strengths/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        strengths = [d['sw_type'] for d in json.loads(response.content)]
        response = self.client.get('/api/users/weaknesses/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        weaknesses = [d['sw_type'] for d in json.loads(response.content)]

        self.assertNotEqual(strengths, weaknesses)


class NotificationsTestCase(TestCase):
    def setUp(self):
        #registers and logins in the user to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token = json.loads(login_response.content)['token']
        # example notification
        self.notifications= [
                {
                    'title':'Notification 1',
                    'creation_datetime':'2021-07-06T00:00:00Z',
                    'description':'This is a description',
                    'is_read':False,
                    'link':'https://example.com/'
                
                },
                {
                    'title':'Notification 2',
                    'creation_datetime':'2021-07-07T00:00:00Z',
                    'description':'Test',
                    'is_read':False,
                    'link':'https://google.co.uk/'
                },
                {
                    'title':'Notification 3',
                    'creation_datetime':'2021-07-08T00:00:00Z',
                    'description':'hello world',
                    'is_read':True,
                    'link':'https://apple.co.uk/'
                }
            ]
    def test_notifications(self):
        #adds notifications
        for n in self.notifications:
            response = self.client.post('/api/notifications/', n, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
            self.assertEqual(response.status_code // 100, 2)

        #gets notifications and checks if they're the same
        response = self.client.get('/api/notifications/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        notifications = json.loads(response.content)
        res = True
        for x,y in zip(self.notifications, notifications):
            for k,v in x.items():
                if not(k in y and y[k] == v):
                    res = False
                    break
            if not res:
                break
        self.assertTrue(res)
        
        #tests if notification changes work
        response = self.client.patch('/api/notifications/', {'is_read':not(notifications[0]['is_read']), 'notification':notifications[0]['id']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        response = self.client.get('/api/notifications/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        new_notifications = json.loads(response.content)

        notifications[0]['is_read'] = not(notifications[0]['is_read'])
        self.assertEqual(notifications, new_notifications)

class MentoringTestCase(TestCase):
    def setUp(self):
        #registers and logins in user1 to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token_1 = json.loads(login_response.content)['token']

        #registers and logins in user2 to obtain an auth token
        self.client.post('/api/users/register/', user2, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user2['username'], 'password':user2['password']}, content_type='application/json')
        self.token_2 = json.loads(login_response.content)['token']
       
    def test_potential_mentees(self):
        response = self.client.get('/api/mentoring/potential_mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        potential_mentees = json.loads(response.content)
        self.assertEqual(len(potential_mentees), 1)
        mentee = potential_mentees[0]

        self.assertEqual(user2['username'], mentee['username'])
        self.assertEqual(user2['first_name'], mentee['first_name'])
        self.assertEqual(user2['last_name'], mentee['last_name'])

        res = True
        for k,v in user2['profile'].items():
            if not(k in mentee['profile'] and mentee['profile'][k] == v):
                res = False 
                break
        self.assertTrue(res)
        self.assertTrue('password' not in mentee)
    
    def test_mentoring(self):
        #creates the mentoring relationship
        response = self.client.get('/api/mentoring/potential_mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        potential_mentees = json.loads(response.content)
        mentee = potential_mentees[0]
        response = self.client.post('/api/mentoring/potential_mentees/', {'mentee':mentee['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.get('/api/mentoring/proposed_mentors/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        proposed_mentors = json.loads(response.content)
        self.assertEqual(len(proposed_mentors), 1)
        response = self.client.post('/api/mentoring/proposed_mentors/', {'mentor':proposed_mentors[0]['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)

        #gets users mentor
        response = self.client.get('/api/mentoring/mentor/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        mentor = json.loads(response.content)
        self.assertEqual(mentor['username'], user1['username'])
        #self.assertTrue('password' not in mentor)

        #gets mentors mentees
        response = self.client.get('/api/mentoring/mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        mentees = json.loads(response.content)
        self.assertEqual(len(mentees), 1)
        mentee = mentees[0]
        self.assertEqual(mentee['username'], user2['username'])
        #self.assertTrue('password' not in mentee)

        #terminates mentoring relationship
        response = self.client.delete('/api/mentoring/mentee/', data={'mentee':mentee['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)

        #checks if mentee's mentor has gone
        response = self.client.get('/api/mentoring/mentor/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code, 404)

        #checks if mentor's mentee has gone
        response = self.client.get('/api/mentoring/mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        mentees = json.loads(response.content)
        self.assertEqual(len(mentees), 0)


class POATestCase(TestCase):
    def setUp(self):
        #registers and logins in user to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token = json.loads(login_response.content)['token']

        self.milestones = [
                {
                    'title':'First milestone',
                    'description':'This is a description',
                    'complete':False,
                    'creation_datetime':'2022-06-07T00:00:00Z',
                    'deadline':'2022-06-08T00:00:00Z',
                    'urgency':3
                    },
                {
                    'title':'Second milestone',
                    'description':'yayayayya',
                    'complete':False,
                    'creation_datetime':'2022-06-08T00:00:00Z',
                    'deadline':'2022-06-11T00:00:00Z',
                    'urgency':2
                    },
                {
                    'title':'Third milestone',
                    'description':'yayayayya',
                    'complete':False,
                    'creation_datetime':'2022-06-09T00:00:00Z',
                    'deadline':'2022-06-18T00:00:00Z',
                    'urgency':1
                    }
                ]

    def test_POA(self):
        #checks if an empty plan of action is returned initially
        response = self.client.get('/api/plans_of_action/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        poa = json.loads(response.content)
        self.assertEqual(poa, [])

        #adds milestones
        response = self.client.post('/api/plans_of_action/milestones/', self.milestones[0], content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.post('/api/plans_of_action/milestones/', self.milestones[1], content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        response = self.client.post('/api/plans_of_action/milestones/', self.milestones[2], content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)

        #gets updated plan of action that contains new milestones
        response = self.client.get('/api/plans_of_action/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        poa = json.loads(response.content)
        #milestones are ordered locally by increasing creation_datetime, they should be returned in decreasing creation_datetime by the server
        res = True
        for m1,m2 in zip(reversed(self.milestones), poa):
            for k,v in m1.items():
                if not(k in m2 and m2[k] == v):
                    res = False
                    break
            if not res:
                break
        self.assertTrue(res)        

        #completes a milestone
        response = self.client.patch('/api/plans_of_action/milestones/', {'milestone':poa[0]['id'], 'complete':True}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        #check if milestone was correctly marked as complete
        response = self.client.get('/api/plans_of_action/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        poa = json.loads(response.content)
        self.assertTrue(poa[0]['complete'])

        while poa:
            #gets milestone and checks if they're equal
            response = self.client.get('/api/plans_of_action/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
            self.assertEqual(response.status_code // 100, 2)
            tmp_poa = json.loads(response.content)
            self.assertEqual(tmp_poa, poa)

            #deletes a milestone
            m = poa.pop()
            response = self.client.delete('/api/plans_of_action/milestones/', {'milestone':m['id']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token))
            self.assertEqual(response.status_code // 100, 2)
        response = self.client.get('/api/plans_of_action/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code // 100, 2)
        poa = json.loads(response.content)
        self.assertEqual(poa, [])


class MeetingsTestCase(TestCase):
    def setUp(self):
        #registers and logins in user1 to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token_1 = json.loads(login_response.content)['token']

        #registers and logins in user2 to obtain an auth token
        self.client.post('/api/users/register/', user2, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user2['username'], 'password':user1['password']}, content_type='application/json')
        self.token_2 = json.loads(login_response.content)['token']

    #tests if everything works when there's no data
    def test_empty(self):
        response = self.client.get('/api/meetings/request/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        self.assertEqual(json.loads(response.content), [])
        response = self.client.get('/api/meetings/propose/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        self.assertEqual(json.loads(response.content), [])
        response = self.client.get('/api/meetings/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        self.assertEqual(json.loads(response.content), [])
        response = self.client.get('/api/meetings/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        self.assertEqual(json.loads(response.content), [])

    def test_meetings(self):
        #creates mentor mentee relationship
        response = self.client.get('/api/mentoring/potential_mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        mentee = json.loads(response.content)[0]
        response = self.client.post('/api/mentoring/potential_mentees/', {'mentee':mentee['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        response = self.client.get('/api/mentoring/proposed_mentors/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        mentor = json.loads(response.content)[0]
        response = self.client.post('/api/mentoring/proposed_mentors/', {'mentor':mentor['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))

        response = self.client.post('/api/meetings/request/', {'description':'Just give me the f@cking meeting mate!'}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)

        response = self.client.get('/api/meetings/request/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        self.assertEqual(len(json.loads(response.content)), 1)

        response = self.client.get('/api/meetings/propose/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        self.assertEqual(response.status_code // 100, 2)
        meetings = json.loads(response.content)
        meeting = meetings[0]
        self.assertEqual(len(meetings), 1)

class FeedbackTestCase(TestCase):
    def setUp(self):
        #registers and logins in user1 to obtain an auth token
        self.client.post('/api/users/register/', user1, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.token_1 = json.loads(login_response.content)['token']

        #registers and logins in user2 to obtain an auth token
        self.client.post('/api/users/register/', user2, content_type='application/json') 
        login_response = self.client.post('/api/users/login/', {'username':user2['username'], 'password':user1['password']}, content_type='application/json')
        self.token_2 = json.loads(login_response.content)['token']

    def test_system_feedback(self):
        system_feedback = [
                {
                    'title':'system feedback 1',
                    'category':'test',
                    'description':'nothing much'
                    },
                {
                    'title':'system feedback 2',
                    'category':'Server',
                    'description':'blah blah blah'
                    },
                {
                    'title':'system feedback 3',
                    'category':'Speed',
                    'description':'text'
                    }
                ]
        for f in system_feedback:
            response = self.client.post('/api/feedback/system/', f, content_type='application/json') 
            self.assertEqual(response.status_code // 100, 2)

        response = self.client.get('/api/feedback/system/') 
        self.assertEqual(response.status_code // 100, 2)
        loaded_feedback = json.loads(response.content)
        for f in loaded_feedback:
            del f['id']
        self.assertEqual(system_feedback, loaded_feedback)

    def test_mentor_feedback(self):
        #creates mentor mentee relationship
        response = self.client.get('/api/mentoring/potential_mentees/', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        mentee = json.loads(response.content)[0]
        response = self.client.post('/api/mentoring/potential_mentees/', {'mentee':mentee['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_1))
        response = self.client.get('/api/mentoring/proposed_mentors/', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        mentor = json.loads(response.content)[0]
        response = self.client.post('/api/mentoring/proposed_mentors/', {'mentor':mentor['username']}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        
        response = self.client.get('/api/feedback/mentor/?mentor_id=1', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        feedback = json.loads(response.content)
        feedback = feedback[0]

        response = self.client.patch('/api/feedback/mentor/?mentor_id=1', {'feedback_id':feedback['id'], 'rating':feedback['rating'] + 1}, content_type='application/json', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)

        response = self.client.get('/api/feedback/mentor/?mentor_id=1', HTTP_AUTHORIZATION='Token {}'.format(self.token_2))
        self.assertEqual(response.status_code // 100, 2)
        retreived_feedback = json.loads(response.content)
        retreived_feedback = retreived_feedback[0]
        
        self.assertEqual(feedback['rating'] + 1, retreived_feedback['rating'])

    def test_meeting_feedback(self):
        pass
