<template>
    <div class="cont-register">
        <div class="register">
            <div class="register-content">
            <img class="logo" src="../assets/logo.png" alt="Logo" />
            <div class="title">Register</div>

            <form class="form" @submit="submit">
                <input type="text" name="FirstName" placeholder="First Name" />
                <input type="text" name="LastName" placeholder="Last Name" />
                <input type="email" name="Email" placeholder="Email" />
                <input type="email" name="ConfirmEmail" placeholder="Confirm Email" />
                <input type="password" name="Password" placeholder="Password" />
                <input
                type="password"
                name="ConfirmPassword"
                placeholder="Confirm Password"
                />

                <div class="form-check">
                <input type="checkbox" value="keep" name="keepLogin" checked />
                <label for="keepLogin"> Keep me logged in </label>
                </div>

                <button type="submit" class="btn btn-outline-light">Register</button>
                <div>
                    <br>
                    <span class="have-account">Already have an account? </span>
                    <router-link to="/" class="to-login">Click here to login.</router-link>
                </div>
            </form>

            </div>
        </div>
    </div>
</template>
<script>
export default {
  methods: {
    submit(e) {
      e.preventDefault();
      let data = e.target.jsondata;
      console.log(data);
    },
  },
  beforeMount() {
    Object.defineProperty(HTMLFormElement.prototype, "jsondata", {
      get() {
        const jsondata = {};
        const formdata = new FormData(this);
        formdata.forEach((value, key) => {
          if (!jsondata[key]) {
            jsondata[key] =
              formdata.getAll(key).length > 1
                ? formdata.getAll(key)
                : formdata.get(key);
          }
        });
        return jsondata;
      },
    });
  },
};
</script>
<style scoped>
    .register {
        display: inline-block;
        justify-content: center;
        margin: auto;
        background-color: #0a102c;
        margin-top: 3%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .cont-register {
        text-align: center;
        background-color: #00001A;
    }
    .register-content {
        width: 350px;
        padding-top: 50px;
        margin: auto;
        text-align: center;
    }
    .title {
        color: #fff;
        font-size: 40px;
        font-weight: 600;
    }
    .logo {
        height: 80px;
    }
    .form {
        margin-bottom: 60px;
    }
    .form > input {
        margin-top: 30px;
        width: 300px;
        color: #fff;
    }
    .form-check {
        margin-top: 30px;
        color: #8faae3;
        text-align: left;
    }
    .form-check > input {
        margin-right: 10px;
    }
    .register > input {
        border: 1px solid #00001a;
        background-color: #00001a;
    }
    .register .check {
        margin-top: 40px;
        color: #8faae3;
    }
    .register button {
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
    .to-login {
        color: #fff;
        text-decoration: none;
    }
</style>