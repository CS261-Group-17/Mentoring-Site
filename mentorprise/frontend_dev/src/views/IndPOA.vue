<template>
    <Navbar :token="this.token"/>
    <div id="IndPOA">
        <h1>{{ profile.fname }}'s Plan of Action</h1>
        <h3>Current Milestones</h3>
        <hr>
        <POAList @complete-milestone="completeMileStone" @edit-milestone="editMileStone" :poaList="getUndone(milestones)"/>
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
                token: {},
                milestones: [],
                profile: {},
            }
        },
        async created() {
            this.profile = {
                fname: "Tommy"
            }
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

            const res = await fetch("backend/api/plans_of_action/", {
                method: "GET",
                headers: {
                    "Content-type": "application/json",
                    "Authorization": "Token "+this.token
                }
            })
            const poa = await res.json()
            this.milestones = poa
            // this.milestones = [
            //     { //Needs to be in YYYY-MM-DD
            //         id: 1,
            //         title: "Learn Python",
            //         description: "Learn how to use Python 3.x",
            //         deadline: "2022-01-09",
            //         complete: false
            //     },
            //     {
            //         id: 2,
            //         title: "Complete mentoring course",
            //         description: "Reach the end and pass the DB mentoring course",
            //         deadline: "2022-02-28",
            //         complete: false
            //     },
            //     {   
            //         id: 3,
            //         title: "Find a new house",
            //         description: "Get a new place to live",
            //         deadline: "2022-01-09",
            //         complete: false
            //     }, 
            //     {
            //         id: 4,
            //         title: "Done done",
            //         description: "This is finished",
            //         deadline: "2022-05-05",
            //         complete: true
            //     }
            // ]
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
            async addMilestone() {
                let today = new Date()
                this.milestones.push({
                    id: this.milestones.length+1,
                    title: "New Milestone",
                    description: "New Milestone Desc",
                    deadline: today.getFullYear() +"-"+String(today.getMonth() + 1).padStart(2, '0') + "-"+ String(today.getDate()).padStart(2, '0'),
                    creation_datetime: today.getFullYear() +"-"+String(today.getMonth() + 1).padStart(2, '0') + "-"+ String(today.getDate()).padStart(2, '0'),
                    complete: false,
                    urgency: 1
                })
                const res = await fetch("backend/api/plans_of_action/milestones/", {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        "Authorization": "Token "+this.token
                    },
                    body: JSON.stringify(this.milestones[this.milestones.length-1])
                })

                const status = await res.status
                if(status >= 300) {
                    alert("Milestone failed to be added")
                    this.milestones = this.milestones.slice(-1)
                }
            },
            async deleteCancelled(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        const res = await fetch("backend/api/plans_of_action/milestones/", {
                            method: "DELETE",
                            headers: {
                                "Content-type": "application/json",
                                "Authorization": "Token "+this.token
                            },
                            body: JSON.stringify({
                                milestone: id,
                            })
                        })

                        const status = await res.status
                        if(status >= 300) {
                            alert("The delete did not occur properly")
                        }
                        else {
                            this.milestones.splice(i,1)
                        }
                        return null
                    }
                }
            },
            async completeMileStone(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        this.milestones[i].complete = true
                        const res = await fetch("backend/api/plans_of_action/milestones/", {
                            method: "PATCH",
                            headers: {
                                "Content-type": "application/json",
                                "Authorization": "Token "+this.token
                            },
                            body: JSON.stringify({
                                milestone: id,
                                complete: true
                            })
                        })

                        const status = await res.status
                        if(status >= 300) {
                            alert("Update did not occur properly")
                            this.milestones[i].complete = false
                        }
                        return null
                    }
                }
            },
            async undoMileStone(id) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        this.milestones[i].complete = false
                        const res = await fetch("backend/api/plans_of_action/milestones/", {
                            method: "PATCH",
                            headers: {
                                "Content-type": "application/json",
                                "Authorization": "Token "+this.token
                            },
                            body: JSON.stringify({
                                milestone: id,
                                complete: false
                            })
                        })

                        const status = await res.status
                        if(status >= 300) {
                            alert("Update did not occur properly")
                            this.milestones[i].complete = true
                        }
                        return null
                    }
                }
            },
            async editMileStone(id, newTitle, newDesc, newDate) {
                for(let i=0;i<this.milestones.length;i++) {
                    if(this.milestones[i].id == id) {
                        const res = await fetch("backend/api/plans_of_action/milestones/", {
                            method: "PATCH",
                            headers: {
                                "Content-type": "application/json",
                                "Authorization": "Token "+this.token
                            },
                            body: JSON.stringify({
                                milestone: id,
                                title: newTitle,
                                description: newDesc,
                                deadline: newDate
                            })
                        })

                        const status = await res.status
                        if(status >= 300) {
                            alert("Update did not occur properly")
                        }
                        else {
                            this.milestones[i].title = newTitle
                            this.milestones[i].description = newDesc
                            this.milestones[i].deadline = newDate
                        }
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
        margin-left: 5%;
        margin-right: 5%;
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