<template>
    <Navbar />
    <div id="Feedback">
        <h1>System Feedback</h1>
        <br>
        <textarea id="sysFeedback" name="sysFeedback" rows="10" cols="70"></textarea>
        <br><br>
        <button id="submit" @click="submitFeedback()">
            Submit System Feedback
        </button>
    </div>
</template>

<script>
    import Navbar from "../components/Navbar.vue";

    export default {
        name: "Feedback",
        props: {},
        components: {
            Navbar
        },
        methods: {
            submitFeedback() {
                alert("Thank you for the feedback")
            }
        }
    }
</script>


<style scoped>
    #Feedback {
        text-align: center;
        color: white;
        margin: 5%;
    }
    #sysFeedback {
        border: solid 10px #424E76;
    }
    #submit {
        padding: 0.5rem;
        background-color: #00001A;
        color: #424E76;
        border: solid 5px #424E76;
        font-weight: bold;
    }
    #submit:hover {
        color: #00001A;
        background-color: #424E76;
    }
</style>