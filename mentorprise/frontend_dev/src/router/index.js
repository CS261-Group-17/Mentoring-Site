import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Profile from "../views/Profile.vue";
import Register from "../views/Register.vue"
import IndPOA from "../views/IndPOA.vue"
import GroupEvents from "../views/GroupEvent.vue"
import POA from "../views/POA.vue"
import Schedule from "../views/Schedule.vue"
import IndEvent from "../views/IndEvent.vue"
import Feedback from "../views/Feedback.vue"
import Reset from "../views/Reset.vue"

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: Dashboard
  },
  {
    path: "/Profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/Register",
    name: "Register",
    component: Register
  },
  {
    path: "/IndPOA",
    name: "IndPOA",
    component: IndPOA
  },
  {
    path: "/GroupEvent",
    name: "GroupEvent",
    component: GroupEvents
  },
  {
    path:"/POA",
    name:"POA",
    component: POA
  },
  {
    path: "/Schedule",
    name: "Schedule",
    component: Schedule
  },
  {
    path: "/IndEvent",
    name: "IndEvent",
    component: IndEvent
  },
  {
    path: "/Feedback",
    name: "Feedback",
    component: Feedback
  },
  {
    path: "/Reset",
    name: "Reset",
    component: Reset
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
