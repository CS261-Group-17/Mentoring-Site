<template>
  <Navbar />
  <div class="dashboard">
    <h1>Dashboard</h1>

    <div class="content">
      <div>
        <div class="part_title">
          <fa icon="network-wired" />
          Connections
        </div>
        <div class="part_content">
          <div class="part_connections_item">
            <template v-if="mentor_data.length != 0">
              <div
                class="part_connections_item_title"
                style="display: flex; justify-content: space-between"
              >
                <span>Mentor</span>
                <router-link to="/">
                  <button class="mentor_button">Request meeting</button>
                </router-link>
              </div>
              <Collapse :list="mentor_data" random="mentor" />
            </template>
            <template v-else>
              <template v-if="!wait_request_mentor_choose">
                <template v-if="!request_mentor_choose">
                  <div class="part_connections_item_select">
                    <div class="title">You don't have a mentor yet!</div>
                    <div style="display: flex">
                      <div style="padding-right: 30px; color: #8faae3">
                        Benefits of having a mentor here,maybe say if you click
                        on the button then you will be paired with a mentor
                      </div>
                      <div>
                        <button
                          class="part_title_button"
                          style="width: 140px; transform: translateY(5px)"
                          @click="request_mentor_choose = true"
                        >
                          Request mentor
                        </button>
                      </div>
                    </div>
                  </div>
                </template>
                <div v-else>
                  <div style="background-color: #0a102c; padding: 8px 6px">
                    Choose a mentor:
                  </div>
                  <div
                    style="
                      border: 1px solid #0a102c;
                      border-top: none;
                      padding: 4px 6px;
                    "
                    v-for="(v, i) in request_mentor_choose_data"
                    :key="i"
                  >
                    <div>
                      {{ v.name }}
                      <span
                        style="
                          font-size: 12px;
                          color: #2b3e75;
                          margin-left: 10px;
                        "
                        v-if="v.recommend"
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
                      <div style="width: 30%">{{ v.info }}</div>
                      <div>{{ v.status }}</div>
                      <div>
                        <button
                          @click="request(v.name)"
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
                    >
                      Change request
                    </button>
                  </div>
                </div>
              </div>
            </template>
          </div>
          <div class="part_connections_item">
            <template v-if="mentees_data.length != 0">
              <div class="part_connections_item_title">Mentees</div>
              <Collapse :list="mentees_data" random="mentees" />
            </template>
            <template v-else>
              <div class="part_connections_item_select">
                <div class="title">You don't have any mentees</div>
                <div style="display: flex">
                  <div style="padding-right: 40px; color: #8faae3">
                    Something about whether or not you are currently visibile to
                    prospective mentees,go to profile to change
                  </div>
                  <div>
                    <router-link to="/Profile">
                      <button
                        class="part_title_button"
                        style="width: 140px; transform: translateY(5px)"
                      >
                        Change on profile
                      </button>
                    </router-link>
                  </div>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <!-- pro icon can't use  https://fontawesome.com/icons/message-lines?s=thin -->
          <fa icon="message-lines" />
          Requests
        </div>

        <div v-for="(v, i) in requests_data" :key="{ i }">
          <div class="triangle"></div>
          <div class="request">
            <span class="request_content">{{ v.content }}</span>
            <span class="request_button" v-if="v.type === 'st'">
              Select times >
            </span>
            <span class="request_button" v-if="v.type === 'gf'">
              Give feedback >
            </span>
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <span>
            <fa icon="clock" />
            Today
          </span>
          <router-link to="/Schedule">
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
            Milestiones
          </span>

          <span>
            <router-link to="/POA">
              <button class="part_title_button">View Plans of Action</button>
            </router-link>
          </span>
        </div>

        <div
          v-for="(v, i) in milestiones_data"
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
          time: "14:00-15:00",
          room: "R1.03",
          color: "#1e2d50",
          bg_color: "#001934",
        },
        {
          title: "Meeting with Harry",
          time: "14:00-15:00",
          room: "R1.03",
          color: "#232364",
          bg_color: "#160046",
        },
      ],
      milestiones_data: [
        {
          title: "You",
          content: "Learn Python",
          time: "38 days late",
          warning: true,
        },
        {
          title: "Bill",
          content: "Get a better job",
          time: "12 days late",
          warning: false,
        },
      ],
      request_mentor_choose: false,
      request_mentor_choose_data: [
        {
          name: "James Archbold",
          recommend: true,
          info: "Software Engineering",
          status: "Rating",
        },
        {
          name: "Nathan Griffiths",
          recommend: false,
          info: "Business area",
          status: "Rating",
        },
      ],
      wait_request_mentor_choose: false,
      wait_request_mentor_choose_data: "",
    };
  },
  methods: {
    request(name) {
      this.request_mentor_choose = false;
      this.wait_request_mentor_choose = true;
      this.wait_request_mentor_choose_data = name;

      setTimeout(() => {
        this.mentor_data = [
          {
            upcoming_milestones: "James Archbold",
            content: "content...",
          },
        ];
      }, 2000);
    },
  },
};
</script>
<style scoped>
.dashboard {
  padding: 2rem;
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
  grid-template-rows: 360px auto;
  gap: 2%;
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
.mentor_button {
  background-color: transparent;
  border: 2px solid #2b3e75;
  border-radius: 6px;
  color: #28396e;
  margin-right: 6px;
  padding: 4px 6px;
  font-size: 14px;
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
.part_connections_item_select {
  background-color: #0a102c;
  padding: 10px;
  font-size: 14px;
}
.part_connections_item_select > .title {
  margin-bottom: 20px;
}
</style>
