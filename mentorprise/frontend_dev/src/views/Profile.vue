<template>
    <Navbar />
    <div id="profile">
        <h1>Profile</h1>
        <h3>Personal Settings</h3>
        <hr>
    </div>
</template>

<script>
    import Navbar from "../components/Navbar.vue";

    export default {
        name: "Profile",
        props: {},
        components: {
            Navbar
        }
    }
</script>

<style scoped>
    #profile {
        padding: 2rem;
    }
</style>
