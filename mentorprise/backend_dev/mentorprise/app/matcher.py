from difflib import Match
from enum import Enum
from dataclasses import dataclass
from random import sample, randint, random
from typing import List
# from numpy.random import normal

@dataclass
class Person:
    name: str
    strengths: List[str]
    weaknesses: List[str]
    time: float
    # meeting_feedback: List[int]
    # mentor_feedback: List[int]

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        # return f"{self.name} has strengths: {self.strengths}, weaknesses: {self.weaknesses}, and time: {self.time}"
        return self.name

@dataclass
class Matcher:
    @staticmethod
    def compare_strengths_weaknesses(mentor_strengths, mentee_weaknesses):
        return len(set(mentor_strengths).intersection(set(mentee_weaknesses)))

    @staticmethod
    def get_ordered_list(mentor, people):
        mentee_scores = {}
        for mentee in people:
            if mentor == mentee:
                print("Hit")
                continue
            print(mentee)
            mentee_scores[mentee] = (
                Matcher.compare_strengths_weaknesses(
                    mentor.strengths, mentee.weaknesses
                )
                + 0
            )
        print(mentee_scores)
        return sorted(mentee_scores, key=mentee_scores.get)


if __name__=="__main__":
    NUM_PEOPLE = 10
    NAMES = "Liam,Olivia,Noah,Emma,Oliver,Ava,Elijah,Charlotte,William,Sophia,James,Amelia,Benjamin,Isabella,Lucas,Mia,Henry,Evelyn,Alexander,Harper".split(",")
    ALL_TOPICS = "Agile,Algorithm,API,Application,Adaptive,Bootstrap,Backend,Browser,Bug,Cache,Code,CSS,Data,Debugging,Deployment,Documentation,Domain,Frameworks,Frontend,Full,Git,GitHub,HTML,HTTP,Information,Java,JavaScript,jQuery,Languages,Libraries,Minification,Mobile,MVP,MySQL,Operating,PHP,Plugin,Python,Resolution,Responsive,Ruby,Sitemap,Software,SSL,Text,UI,UX,Version,Web,Wireframe".split(",")
    TOPICS = ALL_TOPICS[:int(NUM_PEOPLE/2)]

    people = [
        Person(
            NAMES[i],
            sample(TOPICS, randint(1,5)),
            sample(TOPICS, randint(1,5)),
            round(random()*100, 2)
        ) for i in range(NUM_PEOPLE)
    ]

    matcher = Matcher()
    print(people)
    ordered_list = matcher.get_ordered_list(people[0], people)
    print(ordered_list)
