from datetime import datetime

from app.models import *
from app.serializers import *



class Matcher:
    STRENGTH_WEAKNESS_WEIGHT = 2.0
    TIMES_WEIGHT = 1.0
    FEEDBACK_WEIGHT = 1.0 # If this is positive, it floats good mentees, but it can be made negative to avoid bad mentees never getting mentored (TODO: THIS IS NO LONGER TRUE!)
    FEEDBACK_STAR_WEIGHT = 1.0
    FEEDBACK_SENTIMENT_WEIGHT = 0.05

    @staticmethod
    def compare_strengths_weaknesses(mentor, mentee):
        # Prefer mentoring between people with the most shared skills to unblock
        mentor_strengths = [s.sw_type for s in StrengthList.objects.filter(user__exact=mentor)]
        mentee_weaknesses = [w.sw_type for w in WeaknessList.objects.filter(user__exact=mentee)]
        return len(set(mentor_strengths).intersection(set(mentee_weaknesses)))

    @staticmethod
    def compare_times(mentor, mentee):
        # Find the time they would be able to allocate to each other, and
        # match it as closely as possible
        mentor_profile_time = Profile.objects.get(user__exact=mentor).time_available
        mentee_profile_time = Profile.objects.get(user__exact=mentor).time_available
        mentor_num_mentees = len([Pairing.objects.filter(mentor__exact=mentor)])
        mentor_mentored = len([Pairing.objects.filter(mentee__exact=mentor)])
        mentee_num_mentees = len([Pairing.objects.filter(mentor__exact=mentee)])
        mentor_time = mentor_profile_time / (mentor_num_mentees + int(mentor_mentored) + 1)
        mentee_time = mentee_profile_time / (mentee_num_mentees + 2)
        print(mentor_time - mentee_time, mentee_time)
        return mentee_time / max(mentor_time - mentee_time, 0.1)

    @staticmethod
    def assess_feedback(person):
        # Feedback should be on an ELO chess matching system!
        return sum([
            feedback.rating * Matcher.FEEDBACK_STAR_WEIGHT
                + feedback.sentiment * Matcher.FEEDBACK_SENTIMENT_WEIGHT
            for feedback in Feedback.objects.filter(mentor__exact=person)])

    @staticmethod
    def match_feedback(mentor, mentee): # User, # User
        mentor_feedback = Matcher.assess_feedback(mentor)
        mentee_feedback = Matcher.assess_feedback(mentee)
        return mentee_feedback / (mentor_feedback - mentee_feedback)

    @staticmethod
    def get_ordered_list(mentor, people): # User, QuerySet[User]
        mentee_scores = {}
        for mentee in people: # User
            if mentor.id == mentee.id:
                continue
            mentee_scores[mentee] = (
                Matcher.STRENGTH_WEAKNESS_WEIGHT
                        * Matcher.compare_strengths_weaknesses(mentor, mentee)
                + Matcher.TIMES_WEIGHT
                        * Matcher.compare_times(mentor, mentee)
                # + Matcher.FEEDBACK_WEIGHT
                #         * Matcher.match_feedback(mentor, mentee)
            )
        return list(reversed(sorted(mentee_scores, key=mentee_scores.get)))
