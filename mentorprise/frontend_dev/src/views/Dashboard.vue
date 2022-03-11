<template>
  <Navbar :token="this.token"/>
  <div class="dashboard">
    <h1>Dashboard</h1>

    <div class="content">
      <div id="connectionsDiv">
        <div class="part_title">
          <fa icon="network-wired" />
          Connections
        </div>
        <div class="part_content">
          <div class="part_connections_item">
            <template v-if="this.mentor_data.length != 0">
              <div
                class="part_connections_item_title"
                style="display: flex; justify-content: space-between"
              >
                <span>Mentor</span>
                <router-link :to="'/Schedule?t='+this.token">
                  <button class="mentor_button">Request meeting</button>
                </router-link>
              </div>
              <Collapse :list="mentor_data" random="mentor" />
            </template>
            <template v-else>
              <template v-if="!wait_request_mentor_choose">
                <template v-if="!request_mentor_choose">
                  <div class="part_connections_item_select">
                    <div v-if="hasNoMentor()" class="title">You don't have a mentor yet!</div>
                    <div v-if="hasNoMentor()" style="display: flex">
                      <div style="padding-right: 30px; color: #8faae3">
                        Mentoring can help build up skills and develop life long relationships,
                        click here to find a mentor
                      </div>
                      <div>
                        <button
                          class="part_title_button"
                          style="width: 140px; transform: translateY(5px)"
                          @click="getMentorsList()"
                        >
                          Request mentor
                        </button>
                      </div>
                    </div>
                  </div>
                </template>
                <div v-else> <!-- Will show if looking for mentor -->
                  <div style="background-color: #0a102c; padding: 8px 6px">
                    Choose a mentor:
                  </div>
                  <div
                    style="
                      border: 1px solid #0a102c;
                      border-top: none;
                      padding: 4px 6px;
                    "
                    v-for="mentor in request_mentor_choose_data"
                    :key="mentor.name"
                  >
                    <div>
                      {{ mentor.name }}
                      <span
                        style="
                          font-size: 12px;
                          color: #2b3e75;
                          margin-left: 10px;
                        "
                        v-if="mentor.recommend"
                        >Recommended</span
                      >
                    </div>
                    <div
                      style="
                        display: flex;
                        margin-top: 5px;
                        font-size: 14px;
                        justify-content: space-between;
                        color: #8faae3;
                      "
                    >
                      <div style="width: 30%">{{ mentor.info }}</div>
                      <div>{{ mentor.status }}</div>
                      <div>
                        <button
                          @click="request(mentor.name)"
                          style="
                            border-radius: 4px;
                            color: #2b3e75;
                            border: 1px #213260 solid;
                            background-color: transparent;
                            margin-right: 8px;
                            padding: 4px 10px;
                            font-size: 12px;
                            transform: translateY(-10px);
                          "
                          class ="mentorBut"
                        >
                          Choose mentor
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
              <div style="background-color: #09102c; padding: 10px" v-else>
                <div style="margin-bottom: 15px">
                  You have requested {{ wait_request_mentor_choose_data }} as
                  your mentor
                </div>
                <div
                  style="
                    display: flex;
                    justify-content: space-between;
                    margin-right: 8px;
                  "
                >
                  <div style="color: #93a8dd">
                    Awaiting a response from
                    {{ wait_request_mentor_choose_data }}
                  </div>
                  <div>
                    <button
                      @click="
                        wait_request_mentor_choose = false;
                        request_mentor_choose = true;
                      "
                      style="
                        background-color: transparent;
                        border: 1px solid #2b3f73;
                        color: #2b3f73;
                        font-size: 12px;
                        padding: 4px 14px;
                        border-radius: 4px;
                      "
                      class ="mentorBut"
                    >
                      Change request
                    </button>
                  </div>
                </div>
              </div>
            </template>
          </div>
          <div class="part_connections_item">
            <template v-if="mentees_data.length != 0"> <!-- if you have mentees -->
              <div class="part_connections_item_title">Mentees</div>
              <Collapse :list="mentees_data" random="mentees" />
            </template>
            <template v-if="mentees_data.length < 3 && !looking_for_mentees"> <!-- Looking for more mentees -->
              <div class="part_connections_item_select">
                <div class="title">Find a mentee</div>
                <div style="display: flex">
                  <div style="padding-right: 40px; color: #8faae3">
                    You can start searching for a mentee right now, just click the button to find suitable students
                  </div>
                  <div>
                      <button
                        class="part_title_button"

                        style="width: 140px; transform: translateY(5px)"

                        @click = "getPotMentees()"
                      >
                        Start searching
                      </button>
                  </div>
                </div>
              </div>
            </template>
            <template v-if="looking_for_mentees">
                <ul id="lookingForMentee">
                  <li class="potentialMentees" v-for="pot in potential_mentees" :key="pot.id">
                    <p>
                      <b>{{pot.name}}</b><br>
                      {{pot.busArea}} <button class="acceptMentee"><span v-if="!mentee_to_confirm[pot.id]">Accept</span><span v-if="mentee_to_confirm[pot.id]">Waiting</span></button><br>
                      {{pot.bio}}
                    </p>
                  </li>
                </ul>
            </template>
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <fa icon="circle-exclamation" />
          Requests
        </div>

        <div v-for="(v, i) in requests_data" :key="{ i }">
          <div class="triangle"></div>
          <div class="request">
            <span class="request_content">{{ v.content }}</span>
            <!-- <span class="request_button" v-if="v.type === 'st'">
              Select times >
            </span>
            <span class="request_button" v-if="v.type === 'gf'">
              Give feedback >
            </span> -->
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <span>
            <fa icon="clock" />
            Today
          </span>
          <router-link :to="'/Schedule?t='+this.token">
            <button class="part_title_button">View full schedule</button>
          </router-link>
        </div>

        <div
          v-for="(v, i) in today_data"
          :key="i"
          class="today_item"
          :style="'border-color:' + v.color"
        >
          <div
            class="today_item_left"
            :style="`border-color:${v.color};background-color:${v.bg_color};`"
          ></div>
          <div class="today_item_right">
            <div class="today_item_title">{{ v.title }}</div>
            <div class="today_item_content">
              <span>{{ v.time }}</span>
              <span>{{ v.room }}</span>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <span>
            <fa icon="flag" />
            Milestones
          </span>

          <span>
            <router-link :to="'/IndPOA?t='+this.token">
              <button class="part_title_button">View Plans of Action</button>
            </router-link>
          </span>
        </div>

        <div
          v-for="(v, i) in milestones_data"
          :key="i"
          class="milestones_item"
        >
          <div class="milestones_item_title">{{ v.title }}</div>
          <div class="milestones_item_content">
            <span>{{ v.content }}</span>
            <span :style="v.warning ? 'color:#ff4655' : 'color:#fff'">{{
              v.time
            }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Collapse from "../components/Collapse.vue";
export default {
  name: "Dashboard",
  components: {
    Navbar,
    Collapse,
  },
  data() {
    return {
      token: {},
      requests_data: [
        {
          content: "Bill has requested a meeting",
          type: "st",
        },
        {
          content: 'Give feedback for "Meeting with Bill"',
          type: "gf",
        },
      ],
      mentor_data: [],
      mentees_data: [
         { upcoming_milestones: "Bill", content: "content..." },
         { upcoming_milestones: "Harry", content: "content..." },
      ],
      today_data: [
        {
          title: "Meeting with Bill",
          time: "11:00-13:00",
          room: "CS35.1",
          color: "#1e2d50",
          bg_color: "#001934",
        },
        {
          title: "Meeting with Harry",
          time: "16:00-17:00",
          room: "CS36.2",
          color: "#232364",
          bg_color: "#160046",
        },
      ],
      milestones_data: [
        {
          title: "You",
          content: "Learn Python",
          time: "20 days left",
          warning: false,
        },
        {
          title: "Bill",
          content: "Get a better job",
          time: "12 days left",
          warning: false,
        },
      ],
      request_mentor_choose: false, // whether you are requesting a mentor
      request_mentor_choose_data: [],
      potential_mentees: [
        {
          id: 0,
          name: "Edmund Goodman",
          busArea: "Software Development",
          bio: "Always looking to learn more"
        },
        {
          id: 1,
          name: "Mogus Bogus",
          busArea: "Retail",
          bio: "A young entrepreneur looking to learn how to code"
        }
      ],
      mentee_to_confirm: [ true, false ],
      // request_mentor_choose_data: [
      //   {
      //     name: "James Archbold",
      //     recommend: true,
      //     info: "Software Engineering",
      //     status: "Available",
      //   },
      //   {
      //     name: "Nathan Griffiths",
      //     recommend: false,
      //     info: "Marketing",
      //     status: "Available",
      //   },
      // ],
      wait_request_mentor_choose: false, // waiting for mentor to respond to request
      wait_request_mentor_choose_data: "", // stores name of mentor that we have requested
      looking_for_mentees: false
    };
  },
  async created() {
    //alert(document.URL.split("?")[1])
    let splitURL = document.URL.split("?")
    let failed = true
    if(splitURL.length > 1) {
      let urlParams = new URLSearchParams("?" + splitURL[1])
      if(urlParams.has("t")) {
        this.token = urlParams.get("t")
        //alert(this.token)
        failed = false
      }
    }
    if(failed) {
      this.$router.push("/")
    }

    //getting mentor
    const mentorRes = await fetch("backend/api/mentoring/mentor/", {
      method: "GET",
      headers: {
        "Content-type": "application/json",
        "Authorization": "Token "+this.token
      }
    })
    //const mentorRep = await mentorRes.json()
    if(mentorRes.status >= 200 && mentorRes.status < 300) {
      alert("Worked")
    }
    else {
      alert("Could not load mentor")
    }
  },
  methods: {
    request(name) {
      this.request_mentor_choose = false;
      this.wait_request_mentor_choose = true;
      this.wait_request_mentor_choose_data = name;
      // setTimeout(() => {
      //   this.mentor_data = [
      //     {
      //       upcoming_milestones: "James Archbold",
      //       content: "content...",
      //     },
      //   ];
      // }, 2000);
    },
    hasNoMentor() {
      return this.mentor_data.length == 0
    },
    async getMentorsList() {
      this.request_mentor_choose = true
      const res = await fetch("backend/api/mentoring/proposed_mentors/", {
        method: "GET",
        headers: {
          "Content-type": "application/json",
          "Authorization": "Token "+this.token
        }
      })
      //const mentorsList = await res.json()
      const status = await res.status
      if(status >= 200 && status < 300) {
          //alert("Hey Ben")
          this.request_mentor_choose_data= [
          {
            name: "James Archbold",
            recommend: true,
            info: "Software Engineering",
            status: "Available",
          },
          {
            name: "Nathan Griffiths",
            recommend: false,
            info: "Marketing",
            status: "Available",
          },
        ]
      }
      else {
        this.request_mentor_choose = false
        alert("Error collecting mentors")
      }
    },
    getPotMentees() {
      this.looking_for_mentees = true
    }
  },
};
</script>
<style scoped>
.potentialMentees {
  list-style-type: none;
}
.acceptMentee {
  float: right;
}
.dashboard {
  padding: 2rem;
}
#connectionsDiv {
  margin-bottom: 2rem;
}
.dashboard > h1 {
  color: #fff;
  font-weight: 800;
  margin-bottom: 1.5rem;
}
.content {
  height: 67vh;
  color: #fff;
  display: grid;
  grid-template-columns: 49% 49%;
  grid-template-rows: 30rem auto;
  gap: 2%;
  margin-bottom: 2rem solid #00001a;
}
.part_title {
  color: #8faae3;
  padding-bottom: 6px;
  border-bottom: 1px solid #2b3e75;
  margin-bottom: 16px;
}
.part_title svg {
  margin-right: 4px;
}
#lookingForMentee {
  margin-top: 1rem;
}
.acceptMentee {
  color: white;
  background-color: #00001a;
  border: solid 2px white;
}
.acceptMentee:hover {
  color: black;
  background-color: white;
}
.mentor_button {
  background-color: transparent;
  border: 2px solid #2b3e75;
  border-radius: 6px;
  color: #28396e;
  margin-right: 6px;
  padding: 4px 6px;
  font-size: 14px;
}
.mentorBut:hover {
  background-color: white !important;
  color: black !important;
}
.part_connections_item_title {
  background-color: #0a102c;
  padding: 8px 0 8px 10px;
}
.part_connections_item {
  margin-bottom: 18px;
}
.part_connections_item :last-child {
  border-width: 1px;
}
.part_title_button {
  float: right;
  background-color: transparent;
  border: 1px solid #fff;
  border-radius: 4px;
  color: #fff;
  margin-right: 6px;
  padding: 6px;
  font-size: 12px;
  transform: translateY(-12px);
}
.part_title_button:hover {
  color: #00001a;
  background-color: white;
  border: solid 2px #00001a;
}
.today_item {
  border: 1px solid #1e2d50;
  margin-bottom: 12px;
  border-radius: 8px;
  display: flex;
}
.today_item_title {
  margin-bottom: 12px;
}
.today_item_content {
  font-size: 12px;
}
.today_item_content :first-child {
  margin-right: 40px;
}
.today_item_left {
  width: 10px;
  height: 90px;
  border: #fff solid 1px;
  border-radius: 8px;
  border-left: none;
}
.today_item_right {
  padding-top: 15px;
  margin-left: 20px;
}
.milestones_item {
  border: 1px solid #0a102c;
  border-radius: 8px;
}
.milestones_item + .milestones_item {
  margin-top: 12px;
}
.milestones_item_title {
  background-color: #0a102c;
  padding: 10px 8px;
}
.milestones_item_content {
  padding: 10px 8px;
  display: flex;
  justify-content: space-between;
}
.request {
  border: #213260 1px solid;
  border-radius: 0 6px 6px 6px;
  line-height: 50px;
  background-color: #0a102c;
  margin-top: 30px;
  margin-bottom: 14px;
}
.triangle {
  content: "";
  width: 0;
  height: 0;
  border-left: 4px solid #213260;
  border-right: 4px solid transparent;
  border-top: 4px solid transparent;
  border-bottom: 4px solid #213260;
  position: absolute;
  transform: translate(0, -8px);
  background-color: #00001a;
}
.triangle::before {
  content: "";
  border-left: 3px solid #0a102c;
  border-right: 3px solid transparent;
  border-top: 3px solid transparent;
  border-bottom: 3px solid #0a102c;
  position: absolute;
  transform: translate(-3px, -1px);
  background-color: transparent;
}
.request_content {
  padding-left: 10px;
}
.request_button {
  color: #2b3e75;
  font-size: 12px;
  float: right;
  width: 130px;
  text-align: center;
  border-left: 1px solid #213260;
  cursor: pointer;
  background-color: #00001a;
  border-radius: 0 6px 6px 0;
}
.request_button:hover {
  color: #00001a;
  background-color: #2b3e75;
}
.part_connections_item_select {
  background-color: #0a102c;
  padding: 10px;
  font-size: 14px;
}
.part_connections_item_select > .title {
  margin-bottom: 20px;
}
</style>