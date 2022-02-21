<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <input type="text" v-model="email" name="email" placeholder="Email" />
    </div>
    <div class="form-control">
      <input
        type="text"
        v-model="password"
        name="password"
        placeholder="Password"
      />
    </div>
    <div class="form-control form-control-check">
      <label>
        <input type="checkbox" v-model="loggedin" name="loggedin" /> Keep me
        logged in
      </label>
    </div>

    <input type="submit" value="Login" class="btn-block" />
  </form>
</template>

<script>
export default {
  name: "user",
  data() {
    return {
      text: "",
      password: "",
      loggedin: false,
    };
  },
};
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 2px;
  font-family: Arial, Helvetica, sans-serif;
  padding: 1px;
}
.form-control input {
  width: 22%;
  height: 20px;
  margin: 5px;
  padding: 5px 10px;
  font-size: 14px;
  background-color: #00001a;
  color: #5e70a8;
  border: none;
}
.form-control ::placeholder {
  color: #1a2448;
}
.form-control-check {
  padding: 10px;
  color: #5e70a8;
  font-weight: bold;
  font-size: 14px;
  font-family: Arial, Helvetica, sans-serif;
  position: relative;
  display: block;
  padding-left: 15px;
  text-indent: -215px;
}
.form-control-check input {
  width: 15px;
  height: 15px;
  padding: 0;
  margin: 0;
  vertical-align: bottom;
  position: relative;
  top: -1px;
  cursor: pointer;
}
.btn-block {
  font-size: 17px;
  border: 2px solid white;
  border-radius: 4px;
  background-color: transparent;
  color: white;
  padding: 10px 11%;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 12px;
}
</style>