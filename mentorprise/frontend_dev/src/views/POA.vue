<template>
  <Navbar :token="this.token"/>
  <div id="poa">
    <h1>Plan of Action</h1>
    <h3>Your POA</h3>
    <hr />

    <div class="your-poa">
      <div class="list-tips">
        <div>Upcoming milestones:</div>
        <div>Complete by:</div>
        <div>Time remaining:</div>
      </div>
      <Collapse :list="yourPOA" random="your-poa" />
    </div>

    <router-link :to="'/IndPOA?t='+this.token" class="view">
      <button class="ownPOA">View your POA</button>
    </router-link>

    <br /><br />
    <h3>Your Mentees' POAs</h3>
    <hr />
    <div class="your-mentees-poa" v-for="(v, i) in yourMenteesPOA" :key="i">
      <div class="list-tips">
        <div>{{ v.name }}</div>
        <div>Complete by:</div>
        <div>Time remaining:</div>
        <div class="view-full-poa">
          <router-link :to="v.jump">
            <button class="ownPOA">View full POA</button>
          </router-link>
        </div>
      </div>
      <Collapse :list="v.poa" :random="'your-mentees-poa-' + i" />
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Collapse from "../components/Collapse.vue";

export default {
  name: "IndPOA",
  components: {
    Navbar,
    Collapse,
  },
  data() {
    return {
      yourPOA: [],
      yourMenteesPOA: [],
      token: {}
    };
  },
  created() {
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
    this.yourPOA = [
      {
        id: 1,
        upcoming_milestones: "Learn Python",
        comoplete_by: "March 31 2022",
        time_remaining: "20 days left",
        content:
          "For the group project",
      },
      {
        id: 2,
        upcoming_milestones: "Help Bill find a job",
        comoplete_by: "March 25 2022",
        time_remaining: "14 days left",
        content:
          "Need to organise a meeting with him",
      },
    ];

    this.yourMenteesPOA = [
      {
        name: "Bill",
        jump: "/Dashboard?t="+this.token,
        poa: [{
          id:1,
          upcoming_milestones: "Get a better job",
          comoplete_by: "March 23 2022",
          time_remaining: "12 days left",
          content: "Organise a meeting with mentor"
        }]
      },
      {
        name: "Harry",
        jump: "/Dashboard?t="+this.token,
        poa: [{
          id: 1,
          upcoming_milestones: "Improve my networking skills",
          comonplete_by: "April 1 2022",
          time_remaining: "21 days left",
          content: "Go to seminars on networking, try and meet influential people"
        },
        {
          id: 2,
          upcoming_milestones: "Talk to boss about lack of motivation",
          comoplete_by: "March 9 2022",
          time_remaining: "2 days late",
          content: "Feeling a bit burnt out, need to arrange a meeting with the boss"
        }]
      },
      {
        name: "Mr Mentee2",
        jump: "/Dashboard?t="+this.token,
        poa: [{
          id:1,
          upcoming_milestones: "Learn how to be a better mentee",
          comoplete_by: "March 23 2022",
          time_remaining: "12 days left",
          content: "Talk to my mentor more"
        }]
      },
    ];
  },
};
</script>

<style scoped>
#poa {
  padding: 2rem;
  background-color: #00001a;
  color: white;
  font-size: small;
}

#poa h3 {
  margin-top: 35px;
}

#poa hr {
  color: #2b3d75;
  opacity: 1;
  height: 2px;
  margin-top: 0px;
}

.ownPOA:hover {
  color: black !important;
  background-color: white !important;
}

.your-poa {
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

.your-mentees-poa .list-tips {
  padding: 10px 14px;
  margin-bottom: 0;
  font-style: unset;
  background-color: #110f32;
}
.your-mentees-poa > .list-tips div:first-child {
  color: #fff;
}
.your-mentees-poa .view-full-poa {
  height: 0;
  width: 0;
  position: relative;
  left: -110px;
  top: -4.5px;
}
.your-mentees-poa .view-full-poa button {
  width: 110px;
  border-radius: 6px;
  border: 1px solid #2b3e75;
  color: #2b3e75;
  background-color: transparent;
  padding: 4px;
}

.view {
  margin-top: 20px;
  display: block;
  float: right;
}

.view button {
  border-radius: 5px;
  border: solid white 0.1rem;
  color: white;
  background-color: #00001a;
  width: 8rem;
  height: 2.5rem;
}
</style>
