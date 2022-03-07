<template>
  <Navbar />
  <div id="grpevents">
    <h1>Group Events</h1>
    <h3>Event schedule</h3>
    <hr />

    <div class="your-grpevents">
      <div class="sort">
        <button>Filter</button>
        <button>Sort by date</button>
        <input type="text" v-model="search" placeholder="Search all events">
      </div>
      <br>
      <br>
      <div class="list-tips">
        <div>Event:</div>
        <div>Date:</div>
        <div>Time:</div>
        <div>Host:</div>
      </div>

      <div i v-for="event in filteredEvents" :key="event.id" class="collapse-card">
        <div class="collapse-list" data-bs-toggle="collapse" :data-bs-target="'#collapse_' + random + event.id" aria-expanded="false">
          <div>
            <svg
              viewBox="64 64 896 896"
              focusable="false"
              data-icon="right"
              class="arrow"
              width="1em"
              height="1em"
              fill="#2b3d75"
              aria-hidden="true"
              style=""
            >
              <path
                d="M765.7 486.8L314.9 134.7A7.97 7.97 0 00302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 000-50.4z"
              ></path>
            </svg>
            &nbsp; {{ event.eventname }}
          </div>
          <div style="color: #bdc9e3">{{ event.date }}</div>
          <div style="color: #bdc9e3">{{ event.time }}</div>
          <div style="color: #bdc9e3">{{ event.host }}</div>
        </div>
        <div class="collapse collapse-content" :id="'collapse_' + random + event.id">
          {{ event.description }}
          <router-link to="/schedule" class="view">
            <button>Add to schedule</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
import Navbar from "../components/Navbar.vue";
export default {
  name: "GroupEvents",
  components: {
    Navbar,
  },
  data() {
    return {
      Groupevents: [],
      search: ''
    };
  },
  created() {
    this.Groupevents = [
      {
        id: 1,
        eventname: "Learn Python",
        date: "3 March 2022",
        time: "12:00 - 14:00",
        host: "Ben",
        description: "to be filled and button to be added",
      },
      {
        id: 2,
        eventname: "Learn Vue",
        date: "4 March 2022",
        time: "12:00 - 14:00",
        host: "John",
        description: "to be filled and button to be added",
      },
      {
        id: 3,
        eventname: "Learn Java",
        date: "5 March 2022",
        time: "12:00 - 14:00",
        host: "Jay",
        description: "to be filled and button to be added",
      },
      {
        id: 4,
        eventname: "Dance Party",
        date: "2 March 2022",
        time: "12:00 - 14:00",
        host: "Jay",
        description: "to be filled and button to be added",
      },
      {
        id: 5,
        eventname: "Charity Bazaar",
        date: "5 March 2022",
        time: "12:00 - 14:00",
        host: "Jay",
        description: "to be filled and button to be added",
      },
      {
        id: 6,
        eventname: "Charity Dance",
        date: "1 March 2022",
        time: "12:00 - 14:00",
        host: "Jay",
        description: "to be filled and button to be added",
      },
    ];
  },
  computed: {
    filteredEvents: function(){
      return this.Groupevents.filter((event) => {
        return event.eventname.toLowerCase().match(this.search.toLowerCase())
      })
      /* this function below sorts the page automatically*/
    .sort(function(a, b) {
        return new Date(a.date) - new Date(b.date);
      });
    }
  }
}
</script>

<style scoped>
#grpevents {
  padding: 2rem;
  background-color: #00001a;
  color: white;
  font-size: small;
}
#grpevents h3 {
  margin-top: 35px;
}
#grpevents hr {
  color: #2b3d75;
  opacity: 1;
  height: 2px;
  margin-top: 0px;
}
.your-grpevents {
  font-size: 14px;
}
.list-tips {
  color: #243b6f;
  font-style: italic;
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.list-tips > div {
  width: 33%;
}
.collapse-card {
  border: 3px solid #110f32;
  padding: 10px 0;
  color: #bdc9e3;
}
.collapse-card + .collapse-card {
  border-top: none;
}
.collapse-list {
  display: flex;
  justify-content: space-between;
}
.collapse-list > div {
  width: 33%;
}
.collapse-list[aria-expanded="true"] .arrow {
  transition: transform 0.24s;
  color: #2b3d75;
  font-weight: 900;
  transform: none;
}
.collapse-list[aria-expanded="true"] .arrow {
  transition: transform 0.24s;
  transform: rotate(90deg);
}
.collapse-content {
  margin-left: 26px;
  color: #bdc9e3;
}
.view {
  margin-top: 0px;
  display: block;
  float: right;
}
.view button {
  border-radius: 5px;
  border: solid #bdc9e3 0.1rem;
  color: #bdc9e3;
  background-color: #00001a;
}
.sort {
  float: right;
}
.sort button {
  border-radius: 5px;
  border: solid #bdc9e3 0.1rem;
  color: #bdc9e3;
  background-color: #00001a;
}
.sort button:hover{
     background: #2b3d75;
}
.sort input {
  border-radius: 5px;
  border: solid #bdc9e3 0.1rem;
  color: #bdc9e3;
  background-color: #00001a;
  font-weight: lighter;
}
::placeholder {
  color: #bdc9e3;
  font: default;
  font-weight: lighter;
}
</style>