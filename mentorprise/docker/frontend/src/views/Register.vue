<template>
    <div class="cont-register">
        <div class="register">
            <div class="register-content">
            <img class="logo" src="../assets/logo.png" alt="Logo" />
            <div class="title">Register</div>

            <form class="form" @submit="submit">
                <input type="text" id="first" name="FirstName" placeholder="First Name" />
                <input type="text" id="last" name="LastName" placeholder="Last Name" />
                <input type="text" id="user" name="UserName" placeholder="Username" />
                <input type="email" id="email" name="Email" placeholder="Email" />
                <input type="email" id="confirmEmail" name="ConfirmEmail" placeholder="Confirm Email" />
                <input type="password" id="password" name="Password" placeholder="Password" />
                <input
                id="confirmPassword"
                type="password"
                name="ConfirmPassword"
                placeholder="Confirm Password"
                /><br><br>
                <select name="businessArea" id="businessArea">
                    <option disabled selected value="">Business Area</option>
                    <option value="dev">Software Development</option>
                    <option value="marketing">Marketing</option>
                    <option value="retail">Retail</option>
                    <option value="manage">Management</option>
                </select>
                <input type="text" id="jobTitle" name="jobTitle" placeholder="Job Title" />
                <input type="number" id="time" name="time" placeholder="Time you can commit to mentoring" />
                <br><br><textarea id="bio" rows=4 cols=38 placeholder="Tell us here about you..."></textarea>



                <div class="form-check">
                <input id="keepLogin" type="checkbox" value="keep" name="keepLogin" checked />
                <label for="keepLogin"> Keep me logged in </label>
                </div>

                <button type="submit" class="btn btn-outline-light">Register</button>
                <div>
                    <br>
                    <span class="have-account">Already have an account? </span>
                    <router-link to="/" class="to-login">Click here to login.</router-link>
                </div>
            </form>

            </div>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        async submit(e) {
            e.preventDefault();
            //alert(document.getElementById("time").value)
            if(document.getElementById("email").value != document.getElementById("confirmEmail").value) {
                alert("Emails are not matching")
            }
            else if(document.getElementById("password").value != document.getElementById("confirmPassword").value) {
                alert("Passwords are not matching")
            }
            else {
                let register = {
                    email: document.getElementById("email").value,
                    username: document.getElementById("user").value,
                    first_name: document.getElementById("first").value,
                    last_name: document.getElementById("last").value,
                    password: document.getElementById("password").value,
                    //keepLogin: document.getElementById("keepLogin").value,
                    profile: {
                        biography: document.getElementById("bio").value,
                        business_area: document.getElementById("businessArea").value,
                        job_title: document.getElementById("jobTitle").value,
                        mentor: false,
                        time_available: document.getElementById("time").value
                    }
                }
                if(register.profile.businessArea == "") {
                    alert("Need to select a business area")
                }
                else if(register.username == "") {
                    alert("Username cannot be empty")
                }
                else if(register.first_name == "") {
                    alert("First name cannot be empty")
                }
                else if(register.last_name == "") {
                    alert("Last name cannot be empty")
                }
                else if(register.profile.job_title == "") {
                    alert("Job title cannot be empty")
                }
                else if(register.profile.time_available == "") {
                    alert("You must give an estimate of the number of hours you can commit to the system")
                }
                else {
                    const res = await fetch("backend/api/users/register/", {
                        method: "POST",
                        headers: {
                            "Content-type": "application/json"
                        },
                        body: JSON.stringify(register)
                    })
                    const status = await res.json()
                    if(status.email != undefined) {
                        //register worked
                        const loginRes = await fetch("backend/api/users/login/", {
                            method: "POST",
                            headers: {
                                "Content-type": "application/json"
                            },
                            body: JSON.stringify({
                                username: register.username,
                                password: register.password
                            })
                        })
                        const loginStatus = await loginRes.json()
                        if(loginStatus.token != null) {
                            this.$router.push("Dashboard?t="+loginStatus.token)
                        }
                        else {
                            alert("Unexpected failure")
                        }
                    }
                    else {
                        alert("Failed to login")
                    }
                }
            }
        },
    },
};
</script>
<style scoped>
    #businessArea {
        width:18.9rem;
        height: 1.7rem;
    }
    .register {
        display: inline-block;
        justify-content: center;
        margin: auto;
        background-color: #0a102c;
        margin-top: 3%;
        padding-left: 1rem;
        padding-right: 1rem;
        border-bottom: solid 2rem #00001A;
    }
    .cont-register {
        text-align: center;
        background-color: #00001A;
    }
    .register-content {
        width: 350px;
        padding-top: 50px;
        margin: auto;
        text-align: center;
    }
    .title {
        color: #fff;
        font-size: 40px;
        font-weight: 600;
    }
    .logo {
        height: 80px;
    }
    .form {
        margin-bottom: 60px;
    }
    .form > input {
        margin-top: 30px;
        width: 300px;
        color: black;
    }
    .form-check {
        margin-top: 30px;
        color: #8faae3;
        text-align: left;
    }
    .form-check > input {
        margin-right: 10px;
    }
    .register > input {
        border: 1px solid #00001a;
        background-color: #00001a;
    }
    .register .check {
        margin-top: 40px;
        color: #8faae3;
    }
    .register button {
        margin-top: 10px;
        width: 300px;
    }
    ::placeholder {
        color: #222a4d;
        opacity: 1;
    }
    input:focus-visible {
        outline: 0;
    }
    .have-account {
        color: #8faae3;
    }
    .to-login {
        color: #fff;
        text-decoration: none;
    }
</style>