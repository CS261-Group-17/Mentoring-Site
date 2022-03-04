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
        <!-- <label for="email">Email</label><br>
        <input type="email" id="email" name="email" size="40" :value="profile.email"><br> -->
        <br><p>Email: {{ profile.email }}</p>
        <label for="jobTitle">Job Title</label><br>
        <input type="text" id="jobTitle" name="jobTitle" size="40" :value="profile.jobTitle"><br>
        <button class="saveChanges">Save Changes</button>
        <br><br>

        <h3>Mentorship Settings</h3>
        <hr>
        <p class="undertext">This information will be used to match you with potential mentors/mentees.</p>
        <label for="mentorship">Would you like to be a mentor?</label>
        &nbsp;<input type="checkbox" v-model="profile.isMentor" name="mentorship" id="mentorship"><br><br>
        <label for="businessArea">Business Area</label><br>
        <select name="businessArea" id="businessArea" v-model="profile.businessArea_type">
            <option disabled value="">Nothing Selected</option>
            <option v-for="businessArea in options.businessArea" :key="businessArea.value" :value="businessArea.value">
                {{ businessArea.text }}
            </option>
        </select><br><br>
        <p>Strengths</p>
        <SWList :swlist="profile.ss"/>
        <button id="newStrength" @click="addStrength()">+ New Strength</button>
        <br><br><p>Weaknesses</p>
        <SWList :swlist="profile.ws"/>
        <button id="newWeakness" @click="addWeakness()">+ New Weakness</button>
        <br>
        <button class="saveChanges">Save Changes</button>
        
        <br><br>
        <h3 id="dangerZoneTitle">Danger Zone</h3><hr>
        <p class="undertext">Warning: This section edits important parts of your account.</p>
        <div id="dangerZone">
            <label for="password">Password required to change this section:&nbsp;&nbsp;</label>
            <input type="password" id="password" name="password" placeholder="Password" size=30>
            <hr>
            <label for="newEmail">Change your email:&nbsp;&nbsp;</label>
            <input type="email" id="newEmail" name="newEmail" :value="profile.email" size=30>
            &nbsp;&nbsp;&nbsp;<button @click="emailChange()" type="button" class="dangerButton">Confirm Email Change</button><br>
            <br><button @click="passwordReset()" type="button" class="dangerButton">Request an password reset</button><br>
            <br><button @click="deleteAccount()" type="button" class="dangerButton">Delete Account</button>
            <span class="undertext">&nbsp;&nbsp;This cannot be undone!</span>
        </div>
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
                isMentor: true,
                businessArea_type: "dev",
                password: "CompSci",
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
        },
        methods: {
            deleteAccount() {
                var enteredPass = document.getElementById("password");
                if(this.profile.password != enteredPass.value) {
                    alert("Wrong password, enter in correct password")
                }
                else {
                    alert("Correct password, account deleted")
                }
                enteredPass.value = ""
            },
            passwordReset() {
                var enteredPass = document.getElementById("password");
                if(this.profile.password != enteredPass.value) {
                    alert("Wrong password, enter in correct password")
                }
                else {
                    alert("Correct password, password reset email sent")
                }
                enteredPass.value = ""
            },
            emailChange() {
                var enteredPass = document.getElementById("password");
                if(this.profile.password != enteredPass.value) {
                    alert("Wrong password, enter in correct password")
                }
                else {
                    alert("Correct password, email changed")
                    this.profile.email = document.getElementById("newEmail").value;
                }
                enteredPass.value = ""
            },
            addStrength() {
                if(this.profile.ss.length < 5) {
                    this.profile.ss.push({
                        id: this.profile.ss.length+1,
                        value:""
                    })
                }
                else {
                    alert("Cannot have more than 5 strengths")
                }
            },
            addWeakness() {
                if(this.profile.ws.length < 5) {
                    this.profile.ws.push({
                        id: this.profile.ws.length+1,
                        value:""
                    })
                }
                else {
                    alert("Cannot have more than 5 weaknesses")
                }
            }
        }
    }
</script>

<style scoped>
    #dangerZoneTitle {
        color: #FF4655;
    }
    #profile {
        padding: 2rem;
        background-color: #00001A;
        color: white;
        font-size: small;
        margin-left: 5%;
        margin-right: 5%;
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
    ::placeholder {
        color: #424E76;
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
    #dangerZone {
        border: solid 2px #FF4655;
        border-radius: 25px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .dangerButton {
        background-color: #00001A;
        color: #FF4655;
        border: solid 2px #FF4655;
        border-radius: 10px;
    }
</style>
