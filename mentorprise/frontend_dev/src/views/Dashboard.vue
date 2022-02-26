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
          </div>
          <div class="part_connections_item">
            <div class="part_connections_item_title">Mentees</div>
            <Collapse :list="mentees_data" random="mentees" />
          </div>
        </div>
      </div>
      <div>
        <div class="part_title">
          <!-- pro icon can't use  https://fontawesome.com/icons/message-lines?s=thin-->
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
      mentor_data: [
        {
          upcoming_milestones: "James Archbold",
          content: "content...",
        },
      ],
      mentees_data: [
        {
          upcoming_milestones: "Bill",
          content: "content...",
        },
        {
          upcoming_milestones: "Harry",
          content: "content...",
        },
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
    };
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
  height: 70vh;
  color: #fff;
  display: grid;
  grid-template-columns: 49% 49%;
  grid-template-rows: 50% 50%;
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
  margin-bottom: 10px;
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
</style>
