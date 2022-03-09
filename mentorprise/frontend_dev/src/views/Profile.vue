<template>
    <Navbar :token="this.token"/>
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
        <p>Email: {{ profile.email }}</p>
        <p>Username: {{ profile.username }}</p>
        <label for="jobTitle">Job Title</label><br>
        <input type="text" id="jobTitle" name="jobTitle" size="40" :value="profile.jobTitle"><br>
        <label for="timeCommit">Time commitment to the system (in hours per week)</label><br>
        <input type="number" id="timeCommit" name="timeCommit" size="40" :value="profile.time_available"><br>
        <label for="bio">Bio</label><br>
        <textarea v-model="profile.biography" id="bio" rows=4 cols=50>
        </textarea>
        <button class="saveChanges" @click="saveChanges()">Save Changes</button>
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
                token: {},
                profile : {},
                options: {}
            }
        },
        async created() {
            // ran when page loaded
            // currently not implemented gives a 500 error
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
            const res = await fetch("backend/api/users/profile/", {
                method: "GET",
                headers: {
                    "Content-type": "application/json",
                    "Authorization": "Token "+this.token
                }
            })

            const profileStatus = await res.json()
            if(profileStatus.profile != undefined) {
                // this gets us the profile but not the account
                const accRes = await fetch("backend/api/users/account/", {
                    method: "GET",
                    headers: {
                        "Content-type": "application/json",
                        "Authorization": "Token "+this.token
                    }
                })
                const accStatus = await accRes.json()
                if(accStatus.username == undefined) {
                    this.$router.push("/")
                }
                else {
                    // when strengths api works then come back
                    this.profile = {
                        first: accStatus.first_name,
                        last: accStatus.last_name,
                        email: accStatus.email,
                        username: accStatus.username,
                        biography: profileStatus.profile.biography,
                        isMentor: profileStatus.profile.mentor,
                        businessArea_type: profileStatus.profile.business_area,
                        jobTitle: profileStatus.profile.job_title,
                        time_available: profileStatus.profile.time_available,
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
                    //alert(this.profile.jobTitle)
                }
            }  
            else {
                this.$router.push("/")
            }

            // this.profile = {
            //     first: "Ben",
            //     last:  "Lewis",
            //     email: "u2003284@warwick.live.ac.uk",
            //     username: "BennyBoy",
            //     jobTitle: "Student",
            //     biography: "I am in pain",
            //     isMentor: true,
            //     businessArea_type: "dev",
            //     password: "CompSci",
            //     ss: [{
            //             id: 1,
            //             val: "tennis",
            //         },
            //         {
            //             id: 2,
            //             val: "team"
            //         }
            //     ],
            //     ws: [{
            //             id: 1,
            //             val: "communication"
            //         },
            //         {
            //             id: 2,
            //             val: "friendly"   
            //         }                
            //     ]
            // }
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
            async saveChanges() {
                const changeRes = await fetch("backend/api/users/account/", {
                    method: "PATCH",
                    headers: {
                        "Content-type": "application/json",
                        "Authorization": "Token "+this.token
                    },
                    body: JSON.stringify({
                        "first_name": document.getElementById("fname").value,
                        "last_name": document.getElementById("lname").value
                    })
                })

                const changeStatus = await changeRes.status
                if(changeStatus >= 200 && changeStatus < 300) {
                    this.profile.first = document.getElementById("fname").value
                    this.profile.last = document.getElementById("lname").value
                    const profRes = await fetch("backend/api/users/profile/", {
                        method: "PATCH",
                        headers: {
                            "Content-type": "application/json",
                            "Authorization": "Token "+this.token
                        },
                        body: JSON.stringify({
                            //"profile" : {
                                "biography": document.getElementById("bio").value,
                                "job_title": document.getElementById("jobTitle").value,
                                "time_available": document.getElementById("timeCommit").value
                            //}
                        })
                    })

                    const profStatus = await profRes.status
                    if(profStatus >= 200 && profStatus < 300) {
                        this.profile.jobTitle = document.getElementById("jobTitle").value
                        this.profile.biography = document.getElementById("bio").value
                        this.profile.time_available = document.getElementById("timeCommit").value
                    }
                    else {
                        alert("Failed to update successfully")
                    }
                } 
                else {
                    alert("Failed to update correctly")
                }
            },
            async checkPassword() {
                const res = await fetch("backend/api/users/login/", {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: JSON.stringify({
                        "username": this.profile.username,
                        "password": document.getElementById("password").value
                    })
                }) 
                const status = await res.json()
                return status.token != null

            },
            async deleteAccount() {
                if(this.checkPassword()) {
                    const deleteRes = await fetch("backend/api/users/delete/", {
                        method: "DELETE",
                        headers: {
                            "Content-type": "application/json",
                            "Authorization": "Token "+this.token
                        }
                    })

                    const deleteStatus = await deleteRes.status
                    if(deleteStatus >= 200 && deleteStatus < 300) {
                        alert("Account deletion successful, going back to the login page")
                        this.$router.push("/")
                    }
                    else {
                        alert("Account deletion failed")
                    }
                }
                else {
                    alert("Wrong password, enter in correct password")
                    document.getElementById("password").value = ""
                }
            },
            async passwordReset() {
                if(!this.checkPassword()) {
                    alert("Wrong password, enter in correct password")
                }
                else {
                    alert("Correct password, password reset email sent")
                }
                document.getElementById("password").value = ""
            },
            async emailChange() {
                // var enteredPass = document.getElementById("password");
                // if(this.profile.password != enteredPass.value) {
                //     alert("Wrong password, enter in correct password")
                // }
                // else {
                //     alert("Correct password, email changed")
                //     this.profile.email = document.getElementById("newEmail").value;
                // }
                // enteredPass.value = ""
                if(this.checkPassword()) {
                    //change email
                    const emailRes = await fetch("backend/api/users/account/", {
                        method: "PATCH",
                        headers: {
                            "Content-type": "application/json",
                            "Authorization": "Token " +this.token 
                        },
                        body: JSON.stringify({
                            "email": document.getElementById("newEmail").value
                        })
                    })
                    const emailStatus = await emailRes.status
                    if(emailStatus >= 200 && emailStatus < 300) {
                        alert("Email changed")
                        this.profile.email = document.getElementById("newEmail").value
                    }
                    else {
                        alert("Email change unexpectedly fail")
                    }
                }
                else {
                    alert("Password is not correct")
                }
                document.getElementById("password").value = ""
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
    #bio {
        background-color: #00001A;
        color: #424E76;
        border: #424E76 solid 0.2rem;
        margin-top: 0.2rem;
        font-weight: bold;
    }
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
    .saveChanges:hover {
        color: #00001A;
        border: solid #00001A;
        background-color: white;
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
    .dangerButton:hover {
        color: #00001A;
        background-color: #FF4655;
        border: solid 2px #00001A;
        font-weight: 500;
    }
</style>
