<template>
    <NavBar />
    <div id="schedule">
        <h1>Schedule</h1>
        <Calendar :events="this.upcoming(this.schedule)"/>
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
                                <div class="starRating">
                                    <label>
                                        <input type="radio" name="stars" value="1" />
                                        <span class="icon">★</span>
                                    </label> 
                                    <label>
                                        <input type="radio" name="stars" value="2" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="3" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>   
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="4" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="5" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                </div>
                                <br>
                                <label for="feedback">Event Feedback:</label>
                                <textarea name="feedback" id="eventFeedback" rows="3" cols="60"></textarea>
                            </div>
                            <div v-if="request.requestType == 'FM'" class="feedbackForm">
                                <!-- Current implementation of stars does not allow 0 -->
                                <div class="starRating">
                                    <label>
                                        <input type="radio" name="stars" value="1" />
                                        <span class="icon">★</span>
                                    </label> 
                                    <label>
                                        <input type="radio" name="stars" value="2" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="3" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>   
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="4" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                    <label>
                                        <input type="radio" name="stars" value="5" />
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                        <span class="icon">★</span>
                                    </label>
                                </div>
                                <br>
                                <label for="www">What Went Well:</label>
                                <textarea name="www" id="www" rows="3" cols="60"></textarea>
                                <label for="www">What could the mentor have improved:</label>
                                <textarea name="www" id="www" rows="3" cols="60"></textarea>
                                <br>
                                <label>Biggest Improvement Area:&nbsp;</label>
                                <select name="improvement" id="improvement">
                                    <option>None</option>
                                    <option v-for="w in profile.ws" :key="w.id">{{capitalise(w.val)}}</option>
                                </select>
                            </div>
                            <div v-if="request.requestType == 'M'" class="feedbackForm">
                                <p>Choose 3 dates for the mentee to choose from.</p>
                                <label for="chooseDate">Date 1:</label> &nbsp;
                                <input name="chooseDate" class="meetingDateTime" type="datetime-local" :min="setMin()"/>
                                <br><br><label for="chooseDate">Date 2:</label> &nbsp;
                                <input name="chooseDate" class="meetingDateTime" type="datetime-local" :min="setMin()"/>
                                <br><br><label for="chooseDate">Date 3:</label> &nbsp;
                                <input name="chooseDate" class="meetingDateTime" type="datetime-local" :min="setMin()"/>
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
        <div id="pastEvents">
            <h3>Past Events</h3>
            <ul>
                <li v-for="event in pastEvents(schedule)" :key="event.eventID" :class="'past' + event.type">
                    <b>{{event.eventName}}</b><br>
                    {{event.date}}, {{event.location}}
                    <button :class="'seeFeedback'+event.type">See Feedback</button>
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
            //when we get the star rating we have to find the selected one

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
        },
        setMin() {
            // need it in YYYY-MM-DDThh:mm:ss
            let now = new Date()
            let currentMonth = now.getMonth()+1
            if(currentMonth < 10) {
                currentMonth = "0" + currentMonth
            }
            return now.getFullYear()+"-"+currentMonth+"-"+now.getDate()+"T"+now.getHours()+":"+now.getMinutes()+":"+now.getSeconds()
        },
        upcoming(events) {
            let now = Date.now();
            let upcomingEvents  = [];
            for(let i =0;i<events.length;i++) {
                //alert(now)
                //alert(events[i].date + "T" + events[i].startTime)
                let other = Date.parse(events[i].date.replaceAll(" ", "-") + "T" + events[i].startTime)
                //alert(events[i].date.replaceAll(" ", "-") + "T" + events[i].startTime)
                if(now <= other) {
                    upcomingEvents.push(events[i])
                }
            }
            return upcomingEvents
        },
        pastEvents(events) {
            let now = Date.now();
            let prevEvents  = [];
            for(let i =0;i<events.length;i++) {
                let other = Date.parse(events[i].date.replaceAll(" ", "-") + "T" + events[i].startTime)
                if(now > other) {
                    prevEvents.push(events[i])
                }
            }
            return prevEvents
        },
        capitalise(word) {
            let options= [
                { value:"tennis", text: "Tennis"},
                { value:"team", text: "Teamwork"},
                { value:"communication", text: "Communication"},
                { value:"friendly", text: "Friendly"}
            ]
            for(let i =0;i<options.length;i++) {
                if(options[i].value == word) {
                    return options[i].text
                }
            }
            return ""
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
                date: "2022 02 25",
                startTime: "11:00",
                endTime: "13:00",
                location: "CS35.1",
                type: "m"
            },
            {
                eventID: 2,
                eventName: "Meeting with Harry",
                date: "2022 02 25",
                startTime: "16:00",
                endTime: "17:00",
                location: "CS36.2",
                type: "m"
            },
            {
                eventID: 3,
                eventName: "Python Workshop for Beginners",
                date: "2022 02 26",
                startTime: "10:00",
                endTime: "12:00",
                location: "T35",
                type: "w"
            },
            {
                eventID: 4,
                eventName: "Group Session - Mentoring Support",
                date: "2022 02 27",
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
            {
                eventID: 6,
                eventName: "Meeting with Barry",
                date: "2022 02 15",
                startTime: "13:00",
                endTime: "15:00",
                location: "CS242",
                type: "m"
            },
            {
                eventID: 7,
                eventName: "Learning JS",
                date: "2022 02 15",
                startTime: "13:00",
                endTime: "15:00",
                location: "CS262",
                type: "w"
            }
        ]
    }
    };
</script>

<style scoped>
    select {
        border: solid 2px black;
    }
    .starRating {
        display: inline-block;
        position: relative;
        height: 50px;
        line-height: 50px;
        font-size: 50px;
    }

    .starRating label {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        cursor: pointer;
    }

    .starRating label:last-child {
        position: static;
    }

    .starRating label:nth-child(1) {
        z-index: 5;
    }

    .starRating label:nth-child(2) {
        z-index: 4;
    }

    .starRating label:nth-child(3) {
        z-index: 3;
    }

    .starRating label:nth-child(4) {
        z-index: 2;
    }

    .starRating label:nth-child(5) {
        z-index: 1;
    }

    .starRating label input {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
    }

    .starRating label .icon {
        float: left;
        color: transparent;
    }

    .starRating label:last-child .icon {
        color: #000;
    }

    .starRating:not(:hover) label input:checked ~ .icon,
    .starRating:hover label:hover input ~ .icon {
        color: gold;
    }

    .starRating label input:focus:not(:checked) ~ .icon:last-child {
        color: #000;
        text-shadow: 0 0 5px gold;
    }

    #schedule {
        padding: 2rem;
        margin-bottom: 5rem;
        color: white;
    }
    #requests {
        margin-left: 2rem;
        background-color: #0A102C;
        padding: 1rem;
        float: left;
        width: 47%;
    }
    #requests h3, 
    #pastEvents h3 {
        border-bottom: 2px solid #8FAAE3;
    }
    #requestMeetingDiv {
        display: block;
        float:left;
        width: 47%;
    }
    #requestMeetingDiv p {
        word-break: break-all;
        white-space: normal;
    }
    #requestMeetingDiv, #pastEvents {
        justify-content: center;
        padding: 1rem;
        margin-bottom: 0;
        border-bottom:0;
    }
    #pastEvents {
        overflow-y: scroll;
        max-height: 30rem;
        width: 47%;
        float:right;
        display: block;
    }
    .meetingDateTime {
        background-color: white;
        color: black;
        border: solid 2px black;
    }
    #pastEvents ul {
        padding-left: 0;
    }
    .pastm, .pastw, .pastg {
        text-align: left;
        padding: 8px;
        list-style-type: none;
        margin: 10px;
        color: #5F71A0;
        height: auto;
    }
    .pastm {
        border: 1px solid #F15A24;
    }
    .pastw {
        border: 1px solid #ED1E79;
    }
    .pastg {
        border: 1px solid #101AFF;
    }
    .seeFeedbackm, .seeFeedbackg, .seeFeedbackw {
        background-color: #00001A;
        padding: 1rem;
        display: block;
    }
    .seeFeedbackm {
        border: 1px solid #F15A24;
        color: #F15A24;
    }
    .seeFeedbackg {
        border: 1px solid #101AFF;
        color: #101AFF;
    }
    .seeFeedbackw {
        border: 1px solid #ED1E79;
        color: #ED1E79
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
        max-height: 80%;
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