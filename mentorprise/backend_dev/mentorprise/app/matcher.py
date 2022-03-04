from difflib import Match
from enum import Enum
from dataclasses import dataclass
from random import sample, randint, random, choice
import stat
from typing import List, Tuple

@dataclass
class Person:
    name: str
    strengths: List[str]
    weaknesses: List[str]
    time: float
    num_mentees: int
    mentored: bool
    meeting_feedback: List[Tuple[str, int, float]] # text, stars, sentiment analysis
    mentor_feedback: List[Tuple[str, int, float]]

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        # return f"{self.name} has strengths: {self.strengths}, weaknesses: {self.weaknesses}, and time: {self.time}"
        return self.name

class Matcher:
    STRENGTH_WEAKNESS_WEIGHT = 2.0
    TIMES_WEIGHT = 1.0
    FEEDBACK_WEIGHT = 1.0 # If this is positive, it floats good mentees, but it can be made negative to avoid bad mentees never getting mentored (TODO: THIS IS NO LONGER TRUE!)
    FEEDBACK_STAR_WEIGHT = 1.0
    FEEDBACK_SENTIMENT_WEIGHT = 0.05

    @staticmethod
    def compare_strengths_weaknesses(mentor, mentee):
        # Prefer mentoring between people with the most shared skills to unblock
        return len(set(mentor.strengths).intersection(set(mentee.weaknesses)))

    @staticmethod
    def compare_times(mentor, mentee):
        # Find the time they would be able to allocate to each other, and
        # match it as closely as possible
        mentor_time = mentor.time / (mentor.num_mentees + int(mentor.mentored) + 1)
        mentee_time = mentee.time / (mentee.num_mentees + 2)
        return mentee_time / (mentor_time - mentee_time)

    @staticmethod
    def assess_feedback(person):

        # Feedback should be on an ELO chess matching system!

        return (
            sum([f[1]*Matcher.FEEDBACK_STAR_WEIGHT+f[2]*Matcher.FEEDBACK_SENTIMENT_WEIGHT for f in person.meeting_feedback])
            + sum([f[1]*Matcher.FEEDBACK_STAR_WEIGHT+f[2]*Matcher.FEEDBACK_SENTIMENT_WEIGHT for f in person.mentor_feedback])
        )

    @staticmethod
    def match_feedback(mentor, mentee):
        mentor_feedback = Matcher.assess_feedback(mentor)
        mentee_feedback = Matcher.assess_feedback(mentee)
        return mentee_feedback / (mentor_feedback - mentee_feedback)

    @staticmethod
    def get_ordered_list(mentor, people):
        mentee_scores = {}
        for mentee in people:
            if mentor == mentee:
                continue
            mentee_scores[mentee] = (
                Matcher.STRENGTH_WEAKNESS_WEIGHT
                        * Matcher.compare_strengths_weaknesses(mentor, mentee)
                + Matcher.TIMES_WEIGHT
                        * Matcher.compare_times(mentor, mentee)
                + Matcher.FEEDBACK_WEIGHT
                        * Matcher.match_feedback(mentor, mentee)
            )
        print(mentee_scores)
        return list(reversed(sorted(mentee_scores, key=mentee_scores.get)))


if __name__=="__main__":
    NUM_PEOPLE = 10
    NAMES = "Liam,Olivia,Noah,Emma,Oliver,Ava,Elijah,Charlotte,William,Sophia,James,Amelia,Benjamin,Isabella,Lucas,Mia,Henry,Evelyn,Alexander,Harper".split(",")
    ALL_TOPICS = "Agile,Algorithm,API,Application,Adaptive,Bootstrap,Backend,Browser,Bug,Cache,Code,CSS,Data,Debugging,Deployment,Documentation,Domain,Frameworks,Frontend,Full,Git,GitHub,HTML,HTTP,Information,Java,JavaScript,jQuery,Languages,Libraries,Minification,Mobile,MVP,MySQL,Operating,PHP,Plugin,Python,Resolution,Responsive,Ruby,Sitemap,Software,SSL,Text,UI,UX,Version,Web,Wireframe".split(",")
    TOPICS = ALL_TOPICS[:int(NUM_PEOPLE/2)]

    PEOPLE = [
        Person(
            name=NAMES[i],
            strengths=sample(TOPICS, randint(1,5)),
            weaknesses=sample(TOPICS, randint(1,5)),
            time=round(random()*100, 2),
            num_mentees=choice([0,0,0,0,0,1,1,2,3]),
            mentored=bool(random()<0.5),
            meeting_feedback=[("Sample text",randint(1,5),(random()*4-2)) for _ in range(randint(0,10))],
            mentor_feedback=[("Sample text",randint(1,5),(random()*4-2)) for _ in range(randint(0,10))],
        ) for i in range(NUM_PEOPLE)
    ]
    # print(PEOPLE)

    matcher = Matcher()
    ordered_list = matcher.get_ordered_list(PEOPLE[0], PEOPLE)
    print(ordered_list)
