-- Old database model when initally created SQL schema before using Django ORM

DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS StrengthWeaknessList CASCADE;
DROP TABLE IF EXISTS StrengthWeakness CASCADE;
DROP TABLE IF EXISTS Inbox CASCADE;
DROP TABLE IF EXISTS BusinessArea CASCADE;
DROP TABLE IF EXISTS Pairing CASCADE;
DROP TABLE IF EXISTS Meeting CASCADE;
DROP TABLE IF EXISTS Events CASCADE;
DROP TABLE IF EXISTS UserList CASCADE;
DROP TABLE IF EXISTS RejectMentoringOffer CASCADE;
DROP TABLE IF EXISTS ProposeMeeting CASCADE;
DROP TABLE IF EXISTS PasswordReset CASCADE;
DROP TABLE IF EXISTS Milestones CASCADE;
DROP TABLE IF EXISTS Authenticate CASCADE;
DROP TABLE IF EXISTS SystemFeedback CASCADE;
DROP TABLE IF EXISTS MeetingFeedback CASCADE;
DROP TABLE IF EXISTS EventFeedback CASCADE;
DROP TABLE IF EXISTS GeneralFeedback CASCADE;

DROP TYPE IF EXISTS eventType CASCADE;
DROP TYPE IF EXISTS feedbackType CASCADE;

DROP SEQUENCE IF EXISTS strengthweakness_list_seq CASCADE;

CREATE TYPE eventType AS ENUM ('groupSession', 'workshop');
CREATE TYPE feedbackType AS ENUM ('error', 'feature', 'improvement'); -- Add whatever may be needed for type of system feedback

CREATE SEQUENCE strengthweakness_list_seq;

CREATE TABLE BusinessArea (
    bArea text PRIMARY KEY
);

CREATE TABLE StrengthWeaknessList (
    swlID integer,
    swName text NOT NULL, 
    PRIMARY KEY (swlID, swName)
);

CREATE TABLE StrengthWeakness (
    quality text PRIMARY KEY
);

CREATE TABLE Employee (
    userID SERIAL,
    firstName text NOT NULL,
    lastName text NOT NULL,
    passwordSalt text NOT NULL,
    passwordHash text NOT NULL,
    biography text NOT NULL,
    email text NOT NULL,
    strengthListID integer NOT NULL DEFAULT nextval('strengthweakness_list_seq'),
    weaknessListID integer NOT NULL DEFAULT nextval('strengthweakness_list_seq'),
    jobTitle text NOT NULL,
    businessArea text NOT NULL,
    isExpert boolean NOT NULL,
    isMentor boolean NOT NULL,
    PRIMARY KEY(userID),
    FOREIGN KEY(businessArea) REFERENCES BusinessArea(bArea)
);

CREATE TABLE PasswordReset (
    userID integer,
    startTime timestamptz NOT NULL,
    code integer NOT NULL,
    PRIMARY KEY(userID)
);

CREATE TABLE Inbox (
    notifID SERIAL,
    userID integer NOT NULL,
    creationTime timestamptz,
    title text NOT NULL,
    body text NOT NULL,
    isRead boolean NOT NULL,
    link text,
    PRIMARY KEY(notifID),
    FOREIGN KEY(userID) REFERENCES Employee(userID)
);

CREATE TABLE Pairing (
    mentorID integer NOT NULL,
    menteeID integer NOT NULL,
    isActive boolean NOT NULL,
    PRIMARY KEY (mentorID, menteeID),
    UNIQUE(menteeID),
    FOREIGN KEY(mentorID) REFERENCES Employee(userID),
    FOREIGN KEY(menteeID) REFERENCES Employee(userID) 
);

CREATE TABLE Meeting (
    meetingID SERIAL,
    mentorID integer NOT NULL,
    menteeID integer NOT NULL,
    title text NOT NULL,
    body text NOT NULL,
    startTime timestamptz NOT NULL,
    duration integer NOT NULL,
    weaknessListID integer NOT NULL DEFAULT nextval('strengthweakness_list_seq'),
    PRIMARY KEY(meetingID),
    FOREIGN KEY(mentorID, menteeID) REFERENCES PAIRING(mentorID, menteeID)
);

-- need to add checking if userid is a mentor by boolean?
-- modified: removed userListID
CREATE TABLE Events (
    eventID SERIAL,
    mentorID integer NOT NULL,
    title text NOT NULL,
    body text NOT NULL,
    startTime timestamptz NOT NULL,
    duration integer NOT NULL,
    weaknessListID integer NOT NULL DEFAULT nextval('strengthweakness_list_seq'),
    evntType eventType NOT NULL,
    capacity integer NOT NULL,
    PRIMARY KEY(eventID),
    FOREIGN KEY(mentorID) REFERENCES Employee(userID)
);

-- modified: now a list is found based on eventid instead of a uniqueid for a list of users, which is then stored in events
CREATE TABLE UserList (
    eventID integer NOT NULL, -- similar like weakness list, make a unique id
    userID integer NOT NULL,
    PRIMARY KEY (eventID, userID),
    FOREIGN KEY(userID) REFERENCES Employee(userID),
    FOREIGN KEY(eventID) REFERENCES Events(eventID)
);

CREATE TABLE RejectMentoringOffer (
    mentorID integer,
    menteeID integer,
    startTime timestamptz NOT NULL,
    PRIMARY KEY(mentorID, menteeID),
    FOREIGN KEY(mentorID) REFERENCES Employee(userID), 
    FOREIGN KEY(menteeID) REFERENCES Employee(userID) 
);

CREATE TABLE ProposeMeeting (
    mentorID integer NOT NULL,
    menteeID integer NOT NULL,
    body text NOT NULL,
    isRejected boolean NOT NULL,
    rejectionNote text NOT NULL,
    startTime1 timestamptz NOT NULL,
    duration1 integer NOT NULL,
    startTime2 timestamptz,
    duration2 integer,
    startTime3 timestamptz,
    duration3 integer,
    PRIMARY KEY(mentorID, menteeID),
    FOREIGN KEY(mentorID, menteeID) REFERENCES Pairing(mentorID, menteeID)
);

CREATE TABLE Milestones (
    milestoneID SERIAL,
    userID integer NOT NULL,
    title text NOT NULL,
    body text NOT NULL,
    urgency smallint NOT NULL,
    deadline timestamptz NOT NULL,
    isCompleted boolean NOT NULL,
    PRIMARY KEY(milestoneID, userID),
    FOREIGN KEY(userID) REFERENCES Employee(userID)
);

CREATE TABLE Authenticate (
    userID integer NOT NULL,
    authToken integer NOT NULL
);

CREATE TABLE SystemFeedback (
    systemFbID SERIAL,
    userID integer,
    fbType feedbackType NOT NULL,
    title text NOT NULL,
    body text NOT NULL,
    creationTime timestamptz NOT NULL,
    PRIMARY KEY(systemFbID),
    FOREIGN KEY(userID) REFERENCES Employee(userID)
);

CREATE TABLE MeetingFeedback (
    meetingFbID SERIAL,
    userID integer NOT NULL,
    meetingID integer NOT NULL,
    body text NOT NULL,
    creationTime timestamptz NOT NULL,
    rating integer NOT NULL,
    hasAttended boolean NOT NULL,
    sentimentMetric real,
    PRIMARY KEY(meetingFbID),
    FOREIGN KEY(userID) REFERENCES Employee(userID)
);

CREATE TABLE EventFeedback (
    eventFbID SERIAL,
    userID integer,
    eventID integer NOT NULL,
    body text NOT NULL,
    creationTime timestamptz NOT NULL,
    rating integer NOT NULL,
    hasAttended boolean NOT NULL,
    sentimentMetric real NOT NULL,
    PRIMARY KEY(eventFbID),
    FOREIGN KEY(userID) REFERENCES Employee(userID)
);

CREATE TABLE GeneralFeedback (
    generalFbID SERIAL,
    fromUserID integer NOT NULL,
    toUserID integer NOT NULL,
    body text NOT NULL,
    creationTime timestamptz NOT NULL,
    rating integer NOT NULL,
    topicAreas integer NOT NULL DEFAULT nextval('strengthweakness_list_seq'),
    sentimentMetric real NOT NULL,
    PRIMARY KEY(generalFbID),
    FOREIGN KEY(fromUserID) REFERENCES Employee(userID),
    FOREIGN KEY(toUserID) REFERENCES Employee(userID)
);