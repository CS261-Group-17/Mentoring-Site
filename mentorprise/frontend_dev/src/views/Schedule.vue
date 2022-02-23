<template>
    <NavBar />
    <div id="schedule">
        <h1>Schedule</h1>
        <Calendar :events="this.schedule"/>
        <div id="requests">
            <h3>Requests</h3>
            <ul> 
                <li v-for="request in requests" :key="request.requestID" :class="request.requestType+'Request'">
                    {{requestText(request)}}
                    <button class="requestGone" @click="onDelete(request.requestID)"><fa icon="xmark" size="2x"/></button>
                    <button class="respondToRequest" @click="showModal[request.indexID]=true">Respond</button>
                    <transition name="fade" appear>
                        <div class="modal-overlay" v-if="showModal[request.indexID]" @click="showModal[request.indexID]=false"></div>
                    </transition>
                    <transition name="slide" appear>
                        <div class="modal" v-if="showModal[request.indexID]">
                            <h1>{{feedbackTitle(request)}}</h1>
                            <div v-if="request.requestType == 'FE'" class="feedbackForm">
                                <label for="feedback">Event Feedback:</label>
                                <textarea name="feedback" id="eventFeedback" rows="3" cols="60"></textarea>
                            </div>
                            <div v-if="request.requestType == 'FM'" class="feedbackForm">
                                <label for="feedback">Mentor-Mentee Feedback:</label>
                                <textarea name="feedback" id="mentorFeedback" rows="3" cols="60"></textarea>
                            </div>
                            <div v-if="request.requestType == 'M'" class="feedbackForm">
                                <label for="chooseDate">Select a date:</label> &nbsp;
                                <input name="chooseDate" id="meetingDateTime" type="datetime-local"/>
                            </div>
                            <button class="btn btn-primary" type="button" @click="submitFeedback(request)">
                                Submit Form
                            </button>
                            &nbsp;&nbsp;
                            <button class="btn btn-danger" type="button" @click="showModal[request.indexID] = false">
                                Close Form
                            </button>
                        </div>
                    </transition>
                </li>
            </ul>
        </div>
        <div id="requestMeetingDiv">
            <button type="button" class="btn btn-primary" id="requestAMeeting" @click="requestAMeeting()">Request a Meeting</button>
            <br><br><p id="requestStatus"></p>
        </div>
    </div>

</template>

<script>
    import NavBar from "../components/Navbar.vue"
    import Calendar from "../components/Calendar.vue"

    export default {
    name: "Schedule",
    components: {
        NavBar,
        Calendar
    },
    data() {
        return {
            showModal: [],
            profile: {},
            requests: [],
            schedule: []
        }
    },
    methods: {
        requestText(request) {
            if(request.requestType == "FE") {
                return "Give feedback on the recent event: " + request.eventName + "."
            }
            else if(request.requestType == "FM") {
                return "Give general feedback to " + request.mentorName+"."
            }
            else {
                return request.requesteeName + " wants to have a meeting soon."
            }
        },
        onDelete(requestID) {
            let del = false;
            for(let i=0;i<this.requests.length;i++) {
                if(this.requests[i].requestID == requestID) {
                    this.requests.splice(i, 1)
                    i--;
                    del=true;
                }
                else if(del) {
                    this.request.indexID = i;
                }
            }
        },
        requestAMeeting() {
            if(!this.profile.hasMentor) {
                document.getElementById("requestStatus").innerHTML = "Need to have a mentor to request a meeting."
            }
            else {
                document.getElementById("requestStatus").innerHTML = "Meeting requested!"
                // would request meeting
            }
        },
        feedbackTitle(request) {
            if(request.requestType == "FE") {
                //feedback on event
                return "Feedback on " + request.eventName;
            }
            else if(request.requestType == "FM") {
                //feedback on mentor
                return "Feedback on " + request.mentorName;
            }
            else {
                //mentee wants a meeting
                return "Meeting Request"
            }
        },
        submitFeedback(request) {
            
            //defo could improve here
            alert("Thanks for the feedback")

            // would send feedback off and then delete here
            if(request.requestType == "FE") {
                //feedback on event
                this.onDelete(request.requestID)
            }
            else if(request.requestType == "FM") {
                //feedback on mentor
                this.onDelete(request.requestID)
            }
            else {
                //mentee wants a meeting
                this.onDelete(request.requestID)
            }
        }
    },
    created() {
        this.profile = {
                first: "Ben",
                last:  "Lewis",
                email: "u2003284@warwick.live.ac.uk",
                jobTitle: "Student",
                isMentor: true,
                hasMentor: false,
                businessArea_type: "dev",
                password: "CompSci",
                ss: [{
                        id: 1,
                        val: "tennis",
                    },
                    {
                        id: 2,
                        val: "team"
                    }
                ],
                ws: [{
                        id: 1,
                        val: "communication"
                    },
                    {
                        id: 2,
                        val: "friendly"   
                    }                
                ]
        },
        this.requests = [
            // Request types:
            // . Feedback on event (FE)
            // . Meeting requests (M)
            // . Feedback on mentor/mentee (FM)
            {
                requestID: 1,
                requestType:"FE",
                eventID: 2,
                eventName: "Catchup",
                indexID: 0
            },
            {
                requestID: 2,
                requestType: "FM",
                mentorID: 4,
                mentorName: "Bill",
                indexID: 1
            },
            {
                requestID: 3,
                requestType: "M",
                requesteeID: 7,
                requesteeName: "Mary",
                indexID:2
            }
        ]
        for(let i=0;i<this.requests.length;i++) {
            this.showModal.push(false);
            this.requests.indexID = i;
        }
        this.schedule = [
            // Date in YYYY-MM-DD
            // type: w (workshop), m (meeting), g (group session)
            {
                eventID: 1,
                eventName: "Meeting with Bill",
                date: "2022 02 22",
                startTime: "11:00",
                endTime: "13:00",
                location: "CS35.1",
                type: "m"
            },
            {
                eventID: 2,
                eventName: "Meeting with Harry",
                date: "2022 02 22",
                startTime: "16:00",
                endTime: "17:00",
                location: "CS36.2",
                type: "m"
            },
            {
                eventID: 3,
                eventName: "Python Workshop for Beginners",
                date: "2022 02 23",
                startTime: "10:00",
                endTime: "12:00",
                location: "T35",
                type: "w"
            },
            {
                eventID: 4,
                eventName: "Group Session - Mentoring Support",
                date: "2022 02 24",
                startTime: "14:00",
                endTime: "15:00",
                location: "MS Teams",
                type: "g"
            },
            {
                eventID: 5,
                eventName: "Meeting with Harry",
                date: "2022 02 28",
                startTime: "16:00",
                endTime: "17:00",
                location: "CS36.2",
                type: "m"
            },
        ]
    }
    };
</script>

<style scoped>
    #schedule {
        padding: 2rem;
        color: white;
    }
    #requests {
        margin-left: 2rem;
        background-color: #0A102C;
        padding: 1rem;
        float: left;
        width: 47%;
    }
    #requestMeetingDiv {
        text-align: center;
        justify-content: center;
        width: 47%;
        padding: 1rem;
        margin: 1rem;
        display: inline-block
    }
    #meetingDateTime {
        background-color: white;
        color: black;
        border: solid 2px black;
    }
    .feedbackForm {
        margin-bottom: 10px;
    }
    .FMRequest, .FERequest, .MRequest {
        padding-left: 0;
        padding-bottom: 1rem;
        font-style: italic;
    }
    .requestGone, .respondToRequest {
        float: right;
        background-color: #0A102C;
        color: #243B6F;
        border: 0px;
        font-weight: bold;
    }
    .respondToRequest {
        padding-top: 5px;
    }
    .modal-overlay {
        position: absolute;
        top: 0;
        left:0;
        right:0;
        bottom:0;
        z-index: 98;
        background-color: rgba(0,0,0,0.3);
    }
    .modal {
        position: fixed;
        display: block;
        max-height: 40%;
        height: auto;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 99;
        width: 100%;
        max-width: 600px;
        background-color: #FFF;
        font-style: normal;
        color: black;
        border-radius: 16px;
        padding: 25px;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 0.5s;
    }

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    .slide-enter-active,
    .slide-leave-active {
        transition: transform .5s;
    }

    .slide-enter,
    .slide-leave-to {
        transform: translateY(-50%) translateX(100vw);
    }
    textarea {
        border: solid 2px black;
    }
</style>