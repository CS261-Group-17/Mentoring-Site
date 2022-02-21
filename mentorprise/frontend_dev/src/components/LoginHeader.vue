<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>

<script>
export default {
  name: "Login",
  props: {
    title: String,
  },
};
</script>

<style scoped>
header {
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>