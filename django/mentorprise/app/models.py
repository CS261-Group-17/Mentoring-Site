from django.db import models

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    password_salt = models.TextField()
    password_hash = models.TextField()
    biography = models.TextField()
    email = models.TextField()
    business_area = models.TextField()
    job_title = models.TextField()
    expert = models.ForeignKey(StrengthWeakness, models.SET_NULL, null=True, blank=True) #if null the user is not an expert.
    mentor = models.BooleanField()

class StrengthWeakness(models.Model):
    sw_type = models.TextField()  

class StrengthWeaknessList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_strength = models.BooleanField()
    sw_type = models.ForeignKey(StengthWeakness, on_delete=models.CASCADE) 

class Notification(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField()
    title = models.TextField()
    description = models.TextField()
    is_read = models.BooleanField()
    link = models.TextField()

class Event(models.Models):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    start_datetime = models.DateTimeField()
    duration = models.IntegerField()
    cancelled = models.BooleanField()

    class Meta:
        abstract = True

#weaknesses an event is targeted to improving
class EventWeaknesses(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE) #this could be a problem, as it's referencing an abstract class
    weakness_type = models.ForeignKey(StengthWeakness, on_delete=models.CASCADE) 

class Meeting(Event):
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)

class GroupEvent(Event):
    event_type = models.TextField() #group session or workshop
    capacity = model.IntegerField()

class Attendance(models.Models):
    group_event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)
    attendee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    attended = models.BooleanField()

class Feedback(models.models):
    rating = models.IntegerField()
    positives = models.TextField()
    negatives = models.TextField()
    giver = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class MeetingFeedback(Feedback):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

class GroupEventFeedback(Feedback):
    group_event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)

class GeneralFeedback(Feedback):
    creation_datetime = models.DateTimeField()
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

class ImprovedWeaknesses(models.Model):
    feedback = models.ForeignKey(GeneralFeedback, on_delete=models.CASCADE)
    weakness_type = models.ForeignKey(StengthWeakness, on_delete=models.CASCADE) 

class SystemFeedback(models.Models):
    category = models.TextField()
    title = models.TextField()
    description = models.TextField()

class Milestone(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    complete = models.BooleanField()
    creation_datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    urgency = models.SmallIntegerField()


class PasswordReset(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    code = models.IntegerField()

class Pairing(models.Models):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    in_proposal = models.BooleanField()
    terminated = models.BooleanField()

class MeetingProposal(models.Models):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_rejected = models.BooleanField()
    rejection_note = models.TextField()
    time1 = models.DateTimeField()
    duration1 = models.IntegerField()
    time2 = models.DateTimeField()
    duration2 = models.IntegerField()
    time3 = models.DateTimeField()
    duration3 = models.IntegerField()

class Authenticator(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_token = models.IntegerField() #might overflow. IDK how big the auth token will be, or what the max integer size is for postgres

