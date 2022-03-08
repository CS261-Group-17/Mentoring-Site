<template>
    <NavBar :token="this.token"/>
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
        },
        data() {
            return {
                token: {}
            }
        },
        created() {
            let splitURL = document.URL.split("?")
            let failed = true
            if(splitURL.length > 1) {
            let urlParams = new URLSearchParams("?" + splitURL[1])
            if(urlParams.has("t")) {
                this.token = urlParams.get("t")
                //alert(this.token)
                failed = false
            }
            }
            if(failed) {
                this.$router.push("/")
            }
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