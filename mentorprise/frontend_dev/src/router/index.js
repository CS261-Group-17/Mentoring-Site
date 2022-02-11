import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Profile from "../views/Profile.vue";
import Register from "../views/Register.vue"

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
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
