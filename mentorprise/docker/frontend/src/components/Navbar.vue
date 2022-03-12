<template>
    <div id="navbar">
        <img id="logo" src="../assets/logo.png" alt="Logo">
        <span>
            <ul id="navcontent">
                <li class="nav-item"><router-link class="nav-link" :to="'/Dashboard?t='+this.token">Dashboard</router-link></li>
                <li class="nav-item"><router-link class="nav-link" :to="'/POA?t='+this.token">Plans Of Action</router-link></li>
                <li class="nav-item"><router-link class="nav-link" :to="'/Schedule?t='+this.token">Schedule</router-link></li>
                <li class="nav-item"><router-link class="nav-link" :to="'/GroupEvents?t='+this.token">Group Events</router-link></li>
            </ul>
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><router-link class="dropdown-item" :to="'/Profile?t='+this.token">Profile</router-link></li>
                    <li><router-link class="dropdown-item" :to="'/Feedback?t='+this.token">Feedback</router-link></li>
                    <li><router-link class="dropdown-item" :to="'/tos?t='+this.token">Terms of Service</router-link></li>
                    <li><router-link class="dropdown-item" :to="'/privacy?t='+this.token">Privacy</router-link></li>
                    <li><router-link class="dropdown-item" to="/">Sign out</router-link></li>
                </ul>
            </div>
            <!-- <span class="endIcons"><fa icon="sort-down" size="2x"/></span> -->
            <div class="dropdown">
                <button id="bellButton" data-bs-toggle="dropdown" aria_expanded=false><fa id="bell" icon="bell" size="2x"/></button>
                <ul class="dropdown-menu" aria-labelledby="bellButton">
                    <li v-for="notif in this.notifications" :key="notif.id"><span class="dropdown-item">{{ notif.message }}</span></li>
                </ul>
            </div>
            <!-- <div class="dropdown">
                <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                    <fa icon="bell" size="2x"/>
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><router-link class="dropdown-item" to="/Profile">Profile</router-link></li>
                    <li><router-link class="dropdown-item" to="/Feedback">Feedback</router-link></li>
                    <li><router-link class="dropdown-item" to="/">Sign out</router-link></li>
                </ul>
            </div> -->
        </span>
    </div>
</template>

<script>
export default {
    name: "Navbar",
    props: {
        token: String
    },
    data() {
        return {
            notifications: []
        }
    },
    methods: {
        async getNotifications() {
            const res = await fetch("backend/api/notifications/", {
                method: "GET",
                headers: {
                    "Content-type": "application/json",
                    "Authorization": "Token "+this.token
                }
            })

            const notifs= await res.json()
            this.notifications = notifs
            if(this.notifications.length == 0)
            {
                this.notifications = [{
                    id: 1,
                    message: "No notifications"
                }]
            }
            //console.log(this.notifications[0].message)
            return this.notifications
        }
    },
    created() {
        this.notifications = this.getNotifications();
    }
}
</script>

<style scoped>
    #navbar {
        color: whitesmoke;
        background-color: #0A102C;
    }
    #logo {
        width: 5rem;
        height: 5.7rem;
        float: left;
        display: inline;
    }
    #bell:hover {
        color: grey;
    }
    .nav-link {
        color: whitesmoke;
    }
    #navcontent {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        display: inline-block;
        width: auto;
    }
    .nav-item {
        float: left;
    }
    .nav-item a {
        display: block;
        color: white;
        text-align: center;
        padding: 2rem 1rem;
        text-decoration: none;
    }
    li a:hover {
        color: grey;
    }
    .endIcons {
        display: inline;
        float:right;
        padding-top: 1.8rem;
        padding-right: 0.4rem;
    }
    .dropdown {
        display: inline;
        float: right;
        padding-top: 1.8rem;
        padding-right: 0.4rem;
        padding-left: 0.4rem;
    }
    button {
        height: 3rem;
    }
    #bellButton {
        background-color: #0A102C;
        border: solid 2px #0A102C;
        color: white;
    }
</style>