<template>
  <div class="login">
    <img class="logo" src="../assets/logo.png" alt="Logo" />
    <LoginHeader title="Login" />
    <LoginForm />
    <LoginForgotPassword />
    <LoginToRegister />
    <router-link to="/Dashboard">Dashboard</router-link>
  </div>
</template>

<script>
import LoginHeader from "../components/LoginHeader";
import LoginForm from "../components/LoginForm";
import LoginForgotPassword from "../components/LoginForgotPassword";
import LoginToRegister from "../components/LoginToRegister";

export default {
  name: "Login",
  components: {
    LoginHeader,
    LoginForm,
    LoginForgotPassword,
    LoginToRegister,
  },
};
</script>

<style>
#app {
  height: 100%;
  vertical-align: middle;
  text-align: center;
  background-color: #00001A;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  padding: 1px 20px;
}
</style>