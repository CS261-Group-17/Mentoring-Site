<template>
    <Navbar />
    <div id="profile">
        <h1>Profile</h1>

        <h3>Personal Settings</h3>
        <hr>
        <p class="undertext">This information will be visible to your mentor/mentees.</p>
        <label for="fname">First Name</label><br>
        <input type="text" id="fname" name="fname" size="40"><br>
        <label for="lname">Last Name</label><br>
        <input type="text" id="lname" name="lname" size="40"><br>
        <label for="email">Email</label><br>
        <input type="email" id="email" name="email" size="40"><br>
        <label for="jobTitle">Job Title</label><br>
        <input type="text" id="jobTitle" name="jobTitle" size="40"><br>
        <button>Save Changes</button>
        <br>

        <h3>Mentorship Settings</h3>
        <hr>
        <p class="undertext">This information will be used to match you with potential mentors/mentees.</p>
        <label for="businessArea">Business Area</label><br>
        <select name="businessArea" id="businessArea">
            <option value="marketing">Marketing</option>
            <option value="retail">Retail</option>
            <option value="dev" selected>Software Dev</option>
            <option value="manage">Management</option>
        </select>
        <p>Strengths</p>
        <SWList :swlist="sws"/>
    </div>
</template>

<script>
    import Navbar from "../components/Navbar.vue";
    import SWList from "../components/SWList.vue"

    export default {
        name: "Profile",
        props: {
        },
        components: {
            Navbar,
            SWList
        },
        data() {
            return {
                sws: []
            }
        },
        created() {
            // ran when page loaded
            this.sws = [{
                id: 1,
                swnum: 1,
                swdesc: "Tennis"
            }]
        }
    }
</script>

<style scoped>
    #profile {
        padding: 2rem;
        background-color: #00001A;
        color: white;
        font-size: small;
    }
    .undertext {
        color: #BDC9E3;
    }
    input, select {
        margin-bottom: 0.9rem;
        margin-top: 0.3rem;
        background-color: #00001A;
        border: #424E76 solid 0.2rem;
        color: #424E76;
        font-weight: bold;
    }
    button {
        float: right;
        border: solid white 0.2rem;
        color: white;
        background-color: #00001A;
        font-weight: bold;
        width: 7rem;
        height: 2.5rem;
    }
</style>
