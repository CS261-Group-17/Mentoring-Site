<template>
    <NavBar />
    <div id="schedule">
        <h1>Schedule</h1>
        <Calendar :events="this.schedule"/>
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
            profile: {},
            requests: [],
            schedule: []
        }
    },
    created() {
        this.profile = {
                first: "Ben",
                last:  "Lewis",
                email: "u2003284@warwick.live.ac.uk",
                jobTitle: "Student",
                isMentor: true,
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
                eventName: "Catchup"
            },
            {
                requestID: 2,
                requestType: "FM",
                mentorID: 4,
                mentorName: "Bill"
            },
            {
                requestID: 3,
                requestType: "M",
                requesteeID: 7,
                requesteeName: "Mary"
            }
        ]
        this.schedule = [
            // Date in YYYY-MM-DD
            // type: w, m, g
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
</style>