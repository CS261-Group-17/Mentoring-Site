<template>
  <div class="cont-login">
    <div class="login">
      <div class="login-content">
        <img class="logo" src="../assets/logo.png" alt="Logo" />
        <div class="header">Login</div>

        <form @submit="onSubmit" class="form">
          <input id="username" type="text" name="Username" placeholder="Username" />
          <input id="password" type="password" name="Password" placeholder="Password" />

          <div class="form-check">
            <input type="checkbox" value="keep" name="keepLogin" checked />
            <label for="keepLogin"> Keep me logged in </label>
          </div>
          <button type="submit" class="btn btn-outline-light">Login</button>
          <div>
            <br>
            <span class="have-account">Already have an account? </span>
            <router-link to="/register" class="to-register">Click here to register.</router-link>
          </div>
          <hr>
          <p class="have-account">By logging in, you consent to storing necessary cookies.</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  methods: {
    async onSubmit(e) {
      e.preventDefault();
      let login = {"username": document.getElementById("username").value, "password": document.getElementById("password").value}
      
      const res = await fetch("backend/api/users/login/", {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(login)
      })

      const status = await res.json()
      if(status.token != null) {
        //alert("Login successful")
        this.$router.push("Dashboard?t="+status.token)
      }
      else if(status.non_field_errors != null) {
        alert(status.non_field_errors)
      }
      else {
        alert("Please try logging in again")
      }
      //alert(status.token + ", " + status.non_field_errors)
      //let userToken = status.token
      //alert(username + ", " + password)
      //this.$router.push("Dashboard")
    },
  },
};
</script>

<style scoped>
.login {
  display: inline-block;
  justify-content: center;
  margin: auto;
  background-color: #0a102c;
  margin-top: 3%;
  padding-left: 1rem;
  padding-right: 1rem;
}
.cont-login {
  text-align: center;
  background-color: #00001A;
}
.login-content {
  width: 350px;
  padding-top: 50px;
  margin: auto;
  text-align: center;
}
.logo {
  height:80px;
}
.header {
  color: #fff;
  font-size: 40px;
  font-weight: 600;
}
.form {
  margin-bottom: 60px;
}
.form > input {
  margin-top: 30px;
  width: 300px;
  color: black;
}
.form-check {
  margin-top: 30px;
  color: #8faae3;
  text-align: left;
}
.form-check > input {
  margin-right: 10px;
}
.login > input {
  border: 1px solid #00001a;
  background-color: #00001a;
}
.login .check {
  margin-top: 40px;
  color: #8faae3;
}
.login button {
  margin-top: 10px;
  width: 300px;
}
::placeholder {
  color: #222a4d;
  opacity: 1;
}
input:focus-visible {
  outline: 0;
}
.have-account {
  color: #8faae3;
}
.to-register {
  color: #fff;
  text-decoration: none;
}
</style>
