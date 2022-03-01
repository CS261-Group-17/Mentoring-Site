<template>
    <div id="emailReset">
        <h1>Reset Password</h1>
        <br>
        <label for="newP">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New Password:&nbsp;&nbsp;</label>
        <input type="password" name="newP" id="newP"> <span class="eye" @click="changeNewPassword()"><fa icon="eye" size="1x"/></span>

        <br><br>
        <label for="confirmP">Confirm Password:&nbsp;&nbsp;</label>
        <input type="password" name="confirmP" id="confirmP"> <span class="eye" @click="changeConfirmPassword()"><fa icon="eye" size="1x"/></span>
        <br><br>

        <div id="antiBot">
            <span>I am a human</span> &nbsp;
            <input type="checkbox" id="human">
        </div>
        <br><br>
        <button class="btn btn-primary" @click="resetPassword()">Reset Password</button>
    </div>
</template>

<script>
    export default {
        name: "Reset",
        methods: {
            changeNewPassword() {
                var newPass = document.getElementById("newP")
                if(newPass.type == "text") {
                    newPass.type = "password"
                }
                else {
                    newPass.type = "text"
                }
            },
            changeConfirmPassword() {
                var confirmPass = document.getElementById("confirmP")
                if(confirmPass.type == "text") {
                    confirmPass.type = "password"
                }
                else {
                    confirmPass.type = "text"
                }
            },
            resetPassword() {
                if(document.getElementById("newP").value != "" && document.getElementById("confirmP").value != "" && document.getElementById("human").checked && document.getElementById("confirmP").value == document.getElementById("newP").value) {
                    alert("Reset Ok")
                    this.$router.push("Dashboard")
                }
                else {
                    alert("Reset failed")
                }
            }
        }
    }
</script>

<style scoped>
    #emailReset {
        margin: 5%;
        text-align: center;
        color: white;
    }
    input {
        color: black;
    }
    .eye {
        color: white;
    }
    .eye:hover {
        color: grey;
    }
    #antiBot {
        background-color: white;
        border: 1rem solid #0d6efd;
        display: inline-block;
        padding: 1.5rem;
        color: black;
    }
    #human {
        width: 1.5rem;
        height: 1.5rem;
        vertical-align: -6px;
    }
</style>