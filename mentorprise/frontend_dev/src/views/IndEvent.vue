<template>
  <Navbar :token="this.token"/>
  <div class="content">
    <div
      v-if="state == 'participant' || state == 'events_done' || state == 'host'"
      class="event_title"
    >
      {{this.event_name}}
    </div>
    <div v-if="state == 'host'">
      <div class="event_content">
        <div class="event_info">
          <div class="event_info_title">Event info</div>
          <div class="event_info_title_description">
            Edit the fields below and click 'Update event' to save changes
          </div>
          <div class="event_info_form">
            <div>
              <div class="event_info_form_title">Event title</div>
              <input style="width: 100%" :value="this.event_name" />
            </div>
            <div>
              <div class="event_info_form_title">Event type</div>
              <div style="margin-top: 8px">
                <input type="radio" id="wh" name="et" value="wh" :checked="this.event_info.type == 'Meeting'"/>
                <label style="margin-left: 8px; color: #7d95c9" for="wh"
                  >Meeting</label
                >
              </div>
              <div style="margin-top: 8px">
                <input type="radio" id="gm" name="et" value="gm" :checked="this.event_info.type == 'Group Meeting'" />
                <label style="margin-left: 8px; color: #7d95c9" for="gm"
                  >Group Meeting</label
                >
              </div>
              <div style="margin-top: 8px">
                <input type="radio" id="wh" name="et" value="wh" :checked="this.event_info.type == 'Workshop'"/>
                <label style="margin-left: 8px; color: #7d95c9" for="wh"
                  >Workshop</label
                >
              </div>
            </div>
            <div>
              <div class="event_info_form_title">Event description</div>
              <textarea
                style="width: 100%"
                class="event_info_form_textarea"
                :value="this.event_info.description"
              />
            </div>
            <div style="display: flex">
              <div>
                <div class="event_info_form_title">Start time</div>
                <input type="datetime-local" class="eventTimes" :value="this.event_info.date + 'T'+this.event_info.startTime"/>
              </div>
              <div style="margin-left: 14px">
                <div class="event_info_form_title">End time</div>
                <input type="datetime-local" class="eventTimes" :value="this.event_info.date + 'T' + this.event_info.endTime"/>
              </div>
            </div>
            <div>
              <div class="event_info_form_title" id="cap">Event capacity</div>
              <div class="event_info_form_title" id="loc">Location</div><br>
              <input type="number" id="capInput" :value="this.event_info.capacity" />
              <input type="text" id="locInput" :value="this.event_info.location"/>
            </div>
            <div class="event_info_form_button">
              <button class="update_btn">Update event</button>
              <button class="cancel_btn">Cancel event</button>
            </div>
          </div>
        </div>
        <div class="event_attendees">
          <div class="event_attendees_title">
            Event attendees ({{ event_attendees_data.length }})
          </div>
          <div
            class="event_attendees_content"
            v-for="(v, i) in event_attendees_data"
            :key="i"
          >
            {{ v }}
          </div>
        </div>
      </div>
    </div>
    <br><hr>
    <div id="feedbackDiv">
      <h1>Feedback</h1>
      <ul id="allFeedback">
        <li v-for="feedback in this.feedback_data" :key="feedback.id">
          <h3>{{feedback.title}} <span class="fullStars">{{ getStars(feedback.stars) }}</span><span class="emptyStars">{{ getStars(5- feedback.stars) }}</span></h3>
          <p class="feedbackContent">{{feedback.content}}</p>
          <p class="feedbackDate">Feedback Submitted on: {{feedback.time}}</p>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import Navbar from "../components/Navbar.vue";
export default {
  components: {
    Navbar,
  },
  data() {
    return {
      token: {},
      state: "host", //host participant events_done tutor mentee all_done,
      event_name: "Learn Python",
      event_attendees_data: [
        "Greed",
        "Gluttony",
        "Sloth",
        "Lust",
        "Pride",
        "Envy",
        "Wrath"
      ],
      event_info: {
        host: "Nathan Griffiths",
        type: "Workshop",
        description:
          "description description description description description description",
        date: "2022-05-12",
        startTime: "13:00",
        endTime: "15:00",
        location: "Hell",
        capacity: "100"
      },
      feedback_data: [
        {
          id: 1,
          stars: 2,
          title: "Too hot",
          content: "I was sweating the entire time",
          time: "23-01-2022 16:53",
        },
        {
          id: 2,
          stars: 4,
          title: "Very fun",
          content: "Everyone was super friendly too",
          time: "23-05-2022 18:01",
        },
      ],
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
    //alert(this.feedback_data[0].stars)
  },
  methods: {
    getStars(stars) {
      if(stars == 0) {
        return ""
      }
      else if(stars == 1) {
        return "★"
      }
      else if(stars == 2) {
        return "★★"
      }
      else if(stars == 3) {
        return "★★★"
      }
      else if(stars == 4) {
        return "★★★★"
      }
      else {
        return "★★★★★"
      }
    }
  }
};
</script>
<style scoped>
.eventTimes  {
  width: 12rem;
}
#allFeedback>li {
  list-style: none;
}
.feedbackContent {
  font-size: medium;
}
input, textarea {
  color: white;
}
#cap, #loc {
  display: inline-block;
}
#cap {
  margin-right: 7.8rem;
}
#capInput {
  margin-right: 2.8rem;
}
#capInput, #locInput {
  display: inline;
}
.emptyStars {
  color: grey;
}
.fullStars {
  color: gold;
}
.content {
  padding: 2rem;
  background-color: #00001a;
  color: white;
  font-size: small;
  margin-left: 5%;
  margin-right: 5%;
}
.event_title {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
  font-size: calc(1.375rem + 1.5vw);
}
.event_content {
  display: flex;
  justify-content: space-between;
}
.event_content > div:first-child {
  width: 55%;
}
.event_content > div:last-child {
  width: 40%;
}
.event_attendees_title {
  margin-top: 30px;
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
  color: #8faae3;
  font-size: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #2b3e75;
}
.event_info_title {
  margin-top: 30px;
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
  font-size: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #2b3e75;
}
.event_info_title_description {
  color: #aab5cf;
  margin-bottom: 10px;
}
.event_info_form_title {
  margin-top: 12px;
  margin-bottom: 6px;
}
.event_info_form input {
  padding: 4px 6px;
  color: #7d95c9;
  border: 1px solid #1b2854;
  background-color: transparent;
  color-scheme: dark;
}
.event_info_form_textarea {
  height: 150px;
  background-color: transparent;
  border: 1px solid #1b2854;
}
.event_info_form_textarea::placeholder,
.event_info_form input::placeholder {
  padding-left: 6px;
  color: #1b2854;
}
.event_info_form_button {
  display: flex;
  margin-top: 16px;
}
.event_info_form_button button:first-child {
  padding: 4px 8px;
  border: 1px solid #fff;
  border-radius: 6px;
  margin-right: 16px;
  color: #fff;
  background-color: transparent;
}
.cancel_btn {
  padding: 4px 8px;
  border: 1px solid #a32d3f;
  border-radius: 6px;
  margin-right: 10px;
  color: #a32d3f;
  background-color: transparent;
}
/* .cancel_btn, .update_btn {
  padding-right: 0.6rem !important;
} */
.cancel_btn:hover {
  color: white;
  background-color: #a32d3f;
  font-weight: bold;
}
.update_btn:hover {
  color: black !important;
  background-color: white !important;
  font-weight: bold !important;
}
.blue_btn {
  padding: 4px 8px;
  border: 1px solid #1b2854;
  border-radius: 6px;
  margin-right: 10px;
  color: #1b2854;
  background-color: transparent;
}
.event_attendees_content {
  color: #bdc9e3;
  padding-top: 8px;
}
.participant_list > div {
  margin-bottom: 8px;
  display: flex;
}
.participant_list > div :first-child {
  color: #2b3e75;
  width: 150px;
}
.participant_list > div :last-child {
  color: #bdc9e3;
}
.input_blue {
  width: 100%;
  padding: 4px 6px;
  color: #7d95c9;
  border: 1px solid #1b2854;
  background-color: transparent;
}
.events_done_feedback_list {
  border: 2px solid #2b3e75;
  margin-top: 10px;
  margin-bottom: 16px;
  padding: 16px 10px;
  display: grid;
  gap: 8px;
  grid-template-columns: 140px auto;
}
.white_circle {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 12px;
  background-color: #ffffff;
  margin-right: 10px;
}
.blue_circle {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 12px;
  background-color: #213260;
  margin-right: 10px;
}
.white_btn {
  padding: 4px 8px;
  margin-top: 8px;
  background-color: transparent;
  float: right;
  border: 1px solid #fff;
  border-radius: 4px;
  color: #fff;
}
.meeting_review_list {
  margin-top: 14px;
  border: 1px solid #1b2854;
  padding: 10px 8px;
  border-radius: 6px;
}
.meeting_review_list div:first-child {
  color: #bdc9e3;
}
.meeting_review_list div:nth-child(n + 2) {
  color: #2b3e75;
}
.meeting_review_list div:nth-child(n + 3) {
  color: #87a0d8;
}
</style>