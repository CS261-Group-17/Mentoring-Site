from django.db import models
from django.contrib.auth.models import User

##############
### Topics ###
##############


class StrengthWeakness(models.Model):
    sw_type = models.TextField(unique=True)

############
### User ###
############


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    biography = models.TextField()
    business_area = models.TextField()
    job_title = models.TextField()
    # if null the user is not an expert.
    expert_at = models.ForeignKey(
        StrengthWeakness, models.SET_NULL, null=True, blank=True)
    mentor = models.BooleanField(default=False)
    mentee = models.BooleanField(default=True)
    time_available = models.FloatField()


class StrengthList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sw_type = models.ForeignKey(StrengthWeakness, on_delete=models.CASCADE)

class WeaknessList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sw_type = models.ForeignKey(StrengthWeakness, on_delete=models.CASCADE)


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    code = models.IntegerField()

#####################
### Notifications ###
#####################


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField()
    title = models.TextField()
    description = models.TextField()
    is_read = models.BooleanField(default=False)
    link = models.TextField()

##############
### Events ###
##############


class Event(models.Model):
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_instructor_meeting")
    title = models.TextField()
    description = models.TextField()
    start_datetime = models.DateTimeField()
    duration = models.IntegerField()
    cancelled = models.BooleanField()

    class Meta:
        abstract = True


class Meeting(Event):
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_mentee_meeting")


class GroupEvent(Event):
    event_type = models.TextField()  # group session or workshop
    capacity = models.IntegerField()

# weaknesses a group event is targeted to improving


class GroupEventWeaknesses(models.Model):
    event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)
    weakness_type = models.ForeignKey(
        StrengthWeakness, on_delete=models.CASCADE)

# weaknesses a meeting is targeted to improving


class MeetingWeaknesses(models.Model):
    event = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    weakness_type = models.ForeignKey(
        StrengthWeakness, on_delete=models.CASCADE)


class Attendance(models.Model):
    group_event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)
    attendee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    attended = models.BooleanField()


class MeetingProposal(models.Model):
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentor_meeting")
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentee_meeting")
    description = models.TextField()
    is_rejected = models.BooleanField()
    rejection_note = models.TextField()
    time1 = models.DateTimeField()
    duration1 = models.IntegerField()
    time2 = models.DateTimeField()
    duration2 = models.IntegerField()
    time3 = models.DateTimeField()
    duration3 = models.IntegerField()


class MeetingRequest(models.Model):
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentor_meeting_request")
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentee_meeting_request")
    proposal = models.OneToOneField(
        MeetingProposal, null=True, blank=True, on_delete=models.SET_NULL)


################
### Feedback ###
################

class Feedback(models.Model):
    rating = models.IntegerField()
    positives = models.TextField()
    negatives = models.TextField()
    giver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_given_feedback")

    class Meta:
        abstract = True


class MeetingFeedback(Feedback):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class GroupEventFeedback(Feedback):
    group_event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)


class GeneralFeedback(Feedback):
    creation_datetime = models.DateTimeField() # TODO: What is this?
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_received_feedback")


class ImprovedWeaknesses(models.Model):
    feedback = models.ForeignKey(GeneralFeedback, on_delete=models.CASCADE)
    weakness_type = models.ForeignKey(
        StrengthWeakness, on_delete=models.CASCADE)


class SystemFeedback(models.Model):
    category = models.TextField()
    title = models.TextField()
    description = models.TextField()

#######################
### Plans of action ###
#######################


class Milestone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    complete = models.BooleanField()
    creation_datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    urgency = models.SmallIntegerField()

#################
### Mentoring ###
#################


class Pairing(models.Model):
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentor_pairing")
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentee_pairing")
    in_proposal = models.BooleanField()
    terminated = models.BooleanField()
