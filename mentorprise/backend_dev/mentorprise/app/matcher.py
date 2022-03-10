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
        mentee_weaknesses = [w.sw_type for w in WeaknessList.objects.filter(user__exact=mentee)])
        return len(set(mentor_strengths).intersection(set(mentee_weaknesses)))

    # @staticmethod
    # def compare_times(mentor, mentee):
    #     # Find the time they would be able to allocate to each other, and
    #     # match it as closely as possible
    #     mentor_profile = Profile.objects.get(user__exact=mentor)
    #     mentee_profile = Profile.objects.get(user__exact=mentee)
    #     mentor_time = mentor_profile.time / (mentor_profile.num_mentees + int(mentor_profile.mentored) + 1)
    #     mentee_time = mentee_profile.time / (mentee_profile.num_mentees + 2)
    #     return mentee_time / (mentor_time - mentee_time)

    # @staticmethod
    # def assess_feedback(person):
    #     # Feedback should be on an ELO chess matching system!
    #     return (
    #         sum([f[1]*Matcher.FEEDBACK_STAR_WEIGHT+f[2]*Matcher.FEEDBACK_SENTIMENT_WEIGHT for f in person.meeting_feedback])
    #         + sum([f[1]*Matcher.FEEDBACK_STAR_WEIGHT+f[2]*Matcher.FEEDBACK_SENTIMENT_WEIGHT for f in person.mentor_feedback])
    #     )

    # @staticmethod
    # def match_feedback(mentor, mentee): # User, # User
    #     mentor_feedback = Matcher.assess_feedback(mentor)
    #     mentee_feedback = Matcher.assess_feedback(mentee)
    #     return mentee_feedback / (mentor_feedback - mentee_feedback)

    @staticmethod
    def get_ordered_list(mentor, people): # User, QuerySet[User]
        mentee_scores = {}
        for mentee in people: # User
            if mentor.id == mentee.id:
                continue
            mentee_scores[mentee] = (
                Matcher.STRENGTH_WEAKNESS_WEIGHT
                        * Matcher.compare_strengths_weaknesses(mentor, mentee)
                # + Matcher.TIMES_WEIGHT
                #         * Matcher.compare_times(mentor, mentee)
                # + Matcher.FEEDBACK_WEIGHT
                #         * Matcher.match_feedback(mentor, mentee)
            )
        return list(reversed(sorted(mentee_scores, key=mentee_scores.get)))
