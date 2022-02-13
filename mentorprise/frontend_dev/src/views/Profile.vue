<template>
    <Navbar />
    <div id="profile">
        <h1>Profile</h1>

        <h3>Personal Settings</h3>
        <hr>
        <p class="undertext">This information will be visible to your mentor/mentees.</p>
        <label for="fname">First Name</label><br>
        <input type="text" id="fname" name="fname" size="40" :value="profile.first"><br>
        <label for="lname">Last Name</label><br>
        <input type="text" id="lname" name="lname" size="40" :value="profile.last"><br>
        <label for="email">Email</label><br>
        <input type="email" id="email" name="email" size="40" :value="profile.email"><br>
        <label for="jobTitle">Job Title</label><br>
        <input type="text" id="jobTitle" name="jobTitle" size="40" :value="profile.jobTitle"><br>
        <button class="saveChanges">Save Changes</button>
        <br>

        <h3>Mentorship Settings</h3>
        <hr>
        <p class="undertext">This information will be used to match you with potential mentors/mentees.</p>
        <label for="businessArea">Business Area</label><br>
        <select name="businessArea" id="businessArea" v-model="profile.businessArea_type">
            <option disabled value="">Nothing Selected</option>
            <option v-for="businessArea in options.businessArea" :key="businessArea.value" :value="businessArea.value">
                {{ businessArea.text }}
            </option>
        </select><br><br>
        <p>Strengths</p>
        <SWList :swlist="profile.ss"/>
        <button id="newStrength">+ New Strength</button>
        <br><br><p>Weaknesses</p>
        <SWList :swlist="profile.ws"/>
        <button id="newWeakness">+ New Weakness</button>
        <br>
        <button class="saveChanges">Save Changes</button>
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
                profile : {},
                options: {}
            }
        },
        created() {
            // ran when page loaded
            this.profile = {
                first: "Ben",
                last:  "Lewis",
                email: "u2003284@warwick.live.ac.uk",
                jobTitle: "Student",
                businessArea_type: "dev",
                ss: [{
                        id: 1,
                        val: "tennis",
                    },
                    {
                        id: 2,
                        val: "team"
                    }
                ],
                ws: [{
                        id: 1,
                        val: "communication"
                    },
                    {
                        id: 2,
                        val: "friendly"   
                    }                
                ]
            }
            this.options = {
                businessArea: [
                    {value: "dev", text: "Software Dev"},
                    {value: "marketing", text: "Marketing"},
                    {value: "retail", text: "Retail"},
                    {value: "manage", text: "Management"}
                ]
            }
        }
    }
</script>

<style>
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
    .saveChanges {
        float: right;
        border: solid white 0.2rem;
        color: white;
        background-color: #00001A;
        font-weight: bold;
        width: 7rem;
        height: 2.5rem;
    }
    #newStrength, #newWeakness {
        color: #243B6F;
        background-color: #00001A;
        border: 0px;
        font-weight: bold;
        padding-left: 1rem;
    }
</style>
