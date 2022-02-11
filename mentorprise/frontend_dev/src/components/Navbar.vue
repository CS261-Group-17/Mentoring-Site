<template>
    <div id="navbar">
        <img id="logo" src="../assets/logo.png" alt="Logo">
        <span>
            <ul>
                <li class="nav-item"><router-link class="nav-link" to="/Dashboard">Dashboard</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/POA">Plans Of Action</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/Schedule">Schedule</router-link></li>
                <li class="nav-item"><router-link class="nav-link" to="/GroupEvents">Group Events</router-link></li>
            </ul>
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
    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        display: block;
        width: auto;
    }
    li {
        float: left;
    }
    li a {
        display: block;
        color: white;
        text-align: center;
        padding: 2rem 1rem;
        text-decoration: none;
    }
    li a:hover {
        color: grey;
    }
</style>