<template>
    <div id="navbar">
        <img id="logo" src="../assets/logo.png" alt="Logo">
        <span>
            <ul id="navcontent">
                <li class="nav-item"><router-link class="nav-link" to="/Dashboard">Dashboard</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/POA">Plans Of Action</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/Schedule">Schedule</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/GroupEvents">Group Events</router-link></li>
            </ul>
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><router-link class="dropdown-item" to="/Profile">Profile</router-link></li>
                    <li><router-link class="dropdown-item" to="/Feedback">Feedback</router-link></li>
                    <li><router-link class="dropdown-item" to="/">Sign out</router-link></li>
                </ul>
            </div>
            <!-- <span class="endIcons"><fa icon="sort-down" size="2x"/></span> -->
            <span class="endIcons"><fa icon="bell" size="2x"/></span>
        </span>
    </div>
</template>

<script>
export default {
    name: "Navbar",
    props: {}
}
</script>

<style scoped>
    #navbar {
        color: whitesmoke;
        background-color: #0A102C;
    }
    #logo {
        width: 7rem;
        float: left;
        display: inline;
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
</style>