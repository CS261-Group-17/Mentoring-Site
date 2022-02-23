import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Profile from "../views/Profile.vue";
import Register from "../views/Register.vue"
import IndPOA from "../views/IndPOA.vue"
import GroupEvents from "../views/GroupEvent.vue"
import POA from "../views/POA.vue"

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
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
