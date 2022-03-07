<template>
    <NavBar />
    <div id="privacy">
        <h1>Privacy</h1>
        <hr>
        <p>We have many privacy rules</p>
    </div>
</template>

<script>
    import NavBar from "../components/Navbar.vue"
    export default {
        name: "privacy",
        components: {
            NavBar
        }
    }
</script>

<style scoped>
    h1 {
        font-weight: 800;
    }
    #privacy {
        color: white;
        padding: 5%;
    }
    hr {
        border: solid 2px white;
    }
</style>