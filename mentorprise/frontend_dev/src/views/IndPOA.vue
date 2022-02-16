<template>
    <Navbar />
    <div id="IndPOA">
        <h1>{{ profile.fname }}'s Plan of Action</h1>
        <h3>Current Milestones</h3>
        <hr>
        <POAList @complete-milestone="completeMileStone" :poaList="getUndone(milestones)"/>
        <button id="newMilestone" @click="addMilestone()">+ New milestone</button>

        <br><br>
        <h3>Completed Milestones</h3><hr>
        <CompletePOAList  @undo-milestone="undoMileStone" @delete-cancelled="deleteCancelled" :poaList="getCompleted(milestones)" />
    </div>
</template>

<script>
    import Navbar from "../components/Navbar.vue"
    import POAList from "../components/POAList.vue"
    import CompletePOAList from "../components/CompletePOAList.vue"

    export default {
        name: "IndPOA",
        props: {},
        components: {
            Navbar,
            POAList,
            CompletePOAList
        },
        data() {
            return {
                milestones: [],
                profile: {},
            }
        },
        created() {
            this.profile = {
                fname: "Tommy"
            }
            this.milestones = [
                { //Needs to be in YYYY-MM-DD
                    id: 1,
                    title: "Learn Python",
                    desc: "Learn how to use Python 3.x",
                    deadline: "2022-01-09",
                    complete: false
                },
                {
                    id: 2,
                    title: "Complete mentoring course",
                    desc: "Reach the end and pass the DB mentoring course",
                    deadline: "2022-02-28",
                    complete: false
                },
                {   
                    id: 3,
                    title: "Find a new house",
                    desc: "Get a new place to live",
                    deadline: "2022-01-09",
                    complete: false
                }, 
                {
                    id: 4,
                    title: "Done done",
                    desc: "This is finished",
                    deadline: "2022-05-05",
                    complete: true
                }
            ]
        },
        methods: {
            getCompleted(listOfMileStones) {
                let newList = []
                for(let i =0;i<listOfMileStones.length;i++){
                    if(listOfMileStones[i].complete) {
                        newList.push(listOfMileStones[i])
                    }
                }
                return newList
            },
            getUndone(listOfMileStones) {
                let newList = []
                for(let i =0;i<listOfMileStones.length;i++){
                    if(!listOfMileStones[i].complete) {
                        newList.push(listOfMileStones[i])
                    }
                }
                return newList
            },
            addMilestone() {
                this.milestones.push({
                    id: this.milestones.length+1,
                    title: "New Milestone",
                    desc: "New Milestone Desc",
                    deadline: "2022-02-09",
                    complete: false
                })
            },
            deleteCancelled(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        this.milestones.splice(i,1)
                        return null
                    }
                }
            },
            completeMileStone(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        this.milestones[i].complete = true
                        return null
                    }
                }
            },
            undoMileStone(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        this.milestones[i].complete = false
                        return null
                    }
                }
            }
        }
    }
</script>

<style scoped>
    #IndPOA {
        padding: 2rem;
        background-color: #00001A;
        color: white;
        font-size: small;
    }
    #newMilestone {
        color: #243B6F;
        background-color: #00001A;
        border: 0px;
        font-weight: bold;
        padding-left: 1rem;
        font-size: medium;
    }
    ul {
        margin-left: 1%;
        margin-right: 1%;
    }
</style>