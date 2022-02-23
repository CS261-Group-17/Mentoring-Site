<template>
    <div id="calendar">
        <ul> 
            <li v-for="dayEvent in intoDays(calendar)" :key="dayEvent[0].date" class="dayEvents">
                <h3>{{dateToString(dayEvent[0].date)}}</h3>
                <ul>
                    <li v-for="event in dayEvent" :key="event.eventID" :class="'events'+event.type">
                        <p>
                            {{event.eventName}}<br>
                            {{event.startTime + " - " + event.endTime + ", " + event.location}}
                        </p>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Calendar",
        props: {
            events: Array
        },
        data() {
            return {
                calender: []
            }
        },
        components: {},
        methods: {
             sortByDate(currentEvents) {
                if(currentEvents.length < 2) {
                    //alert(currentEvents.length)
                    return currentEvents;
                }
                let mid = Math.ceil(currentEvents.length / 2);
                let arr1 = this.sortByDate(currentEvents.slice(0, mid));
                let arr2 = this.sortByDate(currentEvents.slice(mid, currentEvents.length));
                let newArr = [], p1 = 0, p2 = 0;
                while(newArr.length < currentEvents.length) {
                    if(p1 >= arr1.length) {
                        // finished with first list
                        newArr.push(arr2[p2]);
                        p2+=1;
                    }
                    else if (p2 >= arr2.length) {
                        // finished with second list
                        newArr.push(arr1[p1]);
                        p1+=1;
                    }
                    else if(Date.parse(arr1[p1].date + "T" + arr1[p1].startTime) >= Date.parse(arr2[p2].date + "T" + arr2[p2].startTime)) {
                        // second array is earlier
                        newArr.push(arr2[p2]);
                        p2+=1;
                    }
                    else {
                        // first array is earlier
                        newArr.push(arr1[p1]);
                        p1+=1;
                    }
                }
                return newArr
            },
            sortEventsByDate() {
                //alert("HI");
                return this.sortByDate(this.events)
            },
            intoDays(calendar) {
                if(calendar.length == 0) {
                    return calendar
                }
                let daysCalendar = [[calendar[0]]]
                let currentDay = calendar[0].date
                for(let i=1;i<calendar.length;i++) {
                    if(currentDay == calendar[i].date) {
                        daysCalendar[daysCalendar.length-1].push(calendar[i])
                    }
                    else {
                        currentDay = calendar[i].date
                        daysCalendar.push([calendar[i]])
                    }
                }
                return daysCalendar
            },
            dateToString(ourDate) {
                let dateDate = new Date(ourDate);
                let today = new Date();
                let tomorrow = new Date();
                tomorrow.setDate(today.getDate() + 1);
                if(today.getDate() == dateDate.getDate()) {
                    return "Today"
                }
                if(tomorrow.getDate() == dateDate.getDate()) {
                    return "Tomorrow"
                }
                return dateDate.toString().substring(4, 15)
            }
        },
        created() {
            this.calendar = this.sortEventsByDate();
        }
    }
</script>

<style scoped>
    #calendar {
        background-color: #0A102C;
        padding: 1rem;
        float: left;
        width: 45%;
    }
    .eventsm, .eventsg, .eventsw {
        list-style-type: none;
        padding-left: 0.5rem;
    }
    .eventsm {
        background-color: #F9B59C;
        border-left: 8px solid #F15A24;
    }
    .eventsg {
        background-color: #9196FF;
        border-left: 8px solid #101AFF;
    }
    .eventsw {
        background-color: #F798C1;
        border-left: 8px solid #ED1E79;
    }
    .dayEvents {
        list-style-type: none;
    }
    ul {
        padding: 0rem;
    }
</style>