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

class UserTestCase(TestCase):
    
    def test_auth(self):
        register_response = self.client.post('/api/users/register/', user1, content_type='application/json') 
        self.assertEqual(register_response.status_code, 201)
        login_response = self.client.post('/api/users/login/', {'username':user1['username'], 'password':user1['password']}, content_type='application/json')
        self.assertEqual(register_response.status_code, 201)
        token = json.loads(login_response.content)['token']
        logout_response = self.client.get('/api/users/logout/', HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(login_response.status_code, 200)

        

