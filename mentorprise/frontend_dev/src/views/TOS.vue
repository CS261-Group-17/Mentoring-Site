<template>
    <NavBar />
    <div id="tos">
        <h1>Terms Of Service</h1>
        <hr>
        <p>We have many rules</p>
    </div>
</template>

<script>
    import NavBar from "../components/Navbar.vue"
    export default {
        name: "TOS",
        components: {
            NavBar
        }
    }
</script>

<style scoped>
    h1 {
        font-weight: 800;
    }
    #tos {
        color: white;
        padding: 5%;
    }
    hr {
        border: solid 2px white;
    }
</style>