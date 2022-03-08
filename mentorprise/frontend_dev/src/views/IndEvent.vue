<template>
  <Navbar :token="this.token"/>
  <div class="content">
    <div
      v-if="state == 'participant' || state == 'events_done' || state == 'host'"
      class="event_title"
    >
      Event: Introduction to Python
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
              <input style="width: 100%" placeholder="Introduction to Python" />
            </div>
            <div>
              <div class="event_info_form_title">Event type</div>
              <div style="margin-top: 8px">
                <input type="radio" id="gm" name="et" value="gm" checked />
                <label style="margin-left: 8px; color: #7d95c9" for="gm"
                  >Group Meeting</label
                >
              </div>
              <div style="margin-top: 8px">
                <input type="radio" id="wh" name="et" value="wh" />
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
                placeholder="description the event"
              />
            </div>
            <div style="display: flex">
              <div>
                <div class="event_info_form_title">Start time</div>
                <input type="date" />
              </div>
              <div style="margin-left: 14px">
                <div class="event_info_form_title">End time</div>
                <input type="date" />
              </div>
            </div>
            <div>
              <div class="event_info_form_title">Event capacity</div>
              <input type="number" placeholder="Set a capacity" />
            </div>
            <div class="event_info_form_button">
              <button>Update event</button>
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
    <div v-if="state == 'participant' || state == 'events_done'">
      <div class="event_info">
        <div class="event_info_title">Event info</div>
      </div>
      <div class="participant_list">
        <div>
          <div>Event Hosts:</div>
          <div>{{ event_info.host }}</div>
        </div>
        <div>
          <div>Event Type:</div>
          <div>{{ event_info.type }}</div>
        </div>
        <div>
          <div>Description:</div>
          <div>{{ event_info.description }}</div>
        </div>
        <div>
          <div>Date:</div>
          <div>{{ event_info.date }}</div>
        </div>
        <div>
          <div>Time:</div>
          <div>{{ event_info.time }}</div>
        </div>
      </div>
      <button class="cancel_btn" v-if="state == 'participant'">
        Unattend event
      </button>
    </div>
    <div v-if="state == 'events_done'">
      <div class="event_content">
        <div class="event_info">
          <div class="event_info_title">Event feedback</div>
          <div
            class="events_done_feedback_list"
            v-for="(v, i) in events_done_feedback_data"
            :key="i"
          >
            <div>
              <span
                v-for="(v, i) in v.progress"
                :key="i"
                class="white_circle"
              ></span>
              <span
                v-for="(v, i) in 5 - v.progress"
                :key="i"
                class="blue_circle"
              ></span>
            </div>
            <div>{{ v.title }}</div>
            <div style="color: #213260">{{ v.time }}</div>
            <div style="color: #8faae3">{{ v.content }}</div>
          </div>
        </div>
        <div class="event_attendees">
          <div class="event_attendees_title">Leave feedback</div>
          <div style="margin-top: 8px">Feedback title</div>
          <input class="input_blue" type="text" />
          <div style="margin-top: 8px">Feedback title</div>
          <textarea class="input_blue" type="text" />
          <button class="white_btn">Submit feedback</button>
        </div>
      </div>
    </div>
    <div v-if="state == 'tutor' || state == 'mentee' || state == 'all_done'">
      <div class="event_title">Meeting: Quarterly Review</div>
      <div class="event_info">
        <div class="event_info_title">Meeting info</div>
      </div>
      <div class="participant_list">
        <div>
          <div>Mentee:</div>
          <div>{{ meeting_info.mentee }}</div>
        </div>
        <div>
          <div>Description:</div>
          <div>{{ meeting_info.description }}</div>
        </div>
        <div>
          <div>Date:</div>
          <div>{{ meeting_info.date }}</div>
        </div>
        <div>
          <div>Time:</div>
          <div>{{ meeting_info.time }}</div>
        </div>
      </div>
      <button class="blue_btn" v-if="state == 'tutor' || state == 'mentee'">
        Rearrange meeting
      </button>
      <button class="cancel_btn" v-if="state == 'mentee'">
        Cancel meeting
      </button>
    </div>
    <div v-if="state == 'all_done'">
      <div class="event_content">
        <div class="event_info">
          <div class="event_info_title">Meeting review</div>
          <div
            class="meeting_review_list"
            :key="i"
            v-for="(v, i) in meeting_review_data"
          >
            <div>{{ v.title }}</div>
            <div>{{ v.time }}</div>
            <div>{{ v.content }}</div>
          </div>
        </div>
        <div class="event_attendees">
          <div class="event_attendees_title">Leave feedback</div>
          <div style="margin-top: 8px">Feedback body</div>
          <textarea
            class="input_blue"
            type="text"
            style="border-radius: 6px; margin-top: 10px"
            placeholder="Give your feedback here"
          />
          <button style="float: left" class="white_btn">Submit feedback</button>
        </div>
      </div>
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
      state: "host", //host participant events_done tutor mentee all_done
      event_attendees_data: [
        "Ben lewis",
        "Ben lewis",
        "Ben lewis",
        "Ben lewis",
        "Ben lewis",
        "Ben lewis",
        "Ben lewis",
      ],
      event_info: {
        host: "Nathan Griffiths",
        type: "Workshop",
        description:
          "description description description description description description",
        date: "22-01-2022",
        time: "13:00-15:00",
      },
      meeting_info: {
        mentee: "Bill",
        description:
          "description description description description description description",
        date: "22-01-2022",
        time: "13:00-15:00",
      },
      events_done_feedback_data: [
        {
          progress: 2,
          title: "not very good",
          content: "content content content",
          time: "23-01-2022 11:53",
        },
        {
          progress: 4,
          title: "good overall",
          content: "content content content",
          time: "23-01-2022 11:53",
        },
      ],
      meeting_review_data: [
        {
          title: "James Archblod",
          time: "25-01-2022 01:54",
          content: "good talk,le's do it again sometime",
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
  }
};
</script>
<style scoped>
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