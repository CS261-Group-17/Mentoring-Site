<template>
    <ul>
        <li v-for="poa in poaList" :key="poa.id" class="milestone">
            <p class="poaTitle">{{poa.title}}</p>
            <p class="poaDate">{{dateToString(poa.deadline)}}</p>
            <p class="poaTimeLeft">{{calculateTimeLeft(poa.deadline)}}</p>
            <button class="poaEdit" @click="editMileStone(poa.id, true)"><fa icon="pencil" size="1x"/>&nbsp;Edit</button>
            <transition name="fade" appear>
                <div class="modal-overlay" v-if="checkToShow(poa.id)" @click="editMileStone(poa.id, false)"></div>
            </transition>
            <transition name="slide" appear>
                <div class="modal" v-if="checkToShow(poa.id)">
                    <h1>Edit Milestone</h1>
                    <label for="title">Title:&nbsp;</label>
                    <input :id="'title' + poa.id" name="title" v-model="poa.title"/>
                    <p id="descLabel">Description: </p>
                    <textarea :id="'desc' + poa.id" name="desc" rows=3 cols= 40 v-model="poa.description"></textarea>
                    <br>
                    <label for="chooseDate">Deadline:&nbsp;</label>
                    <input :id="'chooseDate' + poa.id" name="chooseDate" type="datetime-local" :min="setMin()" v-model="poa.deadline" />
                    <br><br>
                    <button class="btn btn-primary" type="button" @click="submitEdits(poa.id)">
                        Submit Form
                    </button>
                    &nbsp;&nbsp;
                    <button class="btn btn-danger" type="button" @click="closeForm(poa.id)">
                        Close Form
                    </button>
                </div>
            </transition>
            <button @click="this.$emit('complete-milestone', poa.id)" class="poaComplete">Complete</button>
            <br>
            <p class="poaUndertext">{{poa.description}}</p>
        </li>
    </ul>
</template>

<script>
export default {
  name: "POAList",
  props: {
      poaList: Array
  },
  data() {
      return {
          showModal: []
      }
  },
  created() {
      for(let i=0;i<this.poaList.length;i++) {
          this.showModal.push(false)
      }
  },
  components: {},
  methods: {
        setMin() {
            // need it in YYYY-MM-DDThh:mm:ss
            let now = new Date()
            let currentMonth = now.getMonth()+1
            if(currentMonth < 10) {
                currentMonth = "0" + currentMonth
            }
            return now.getFullYear()+"-"+currentMonth+"-"+now.getDate()+"T"+now.getHours()+":"+now.getMinutes()+":"+now.getSeconds()
        },
        // setCurrent(currentDate) {
        //     let currentMonth = currentDate.getMonth()+1
        //     if(currentMonth < 10) {
        //         currentMonth = "0" + currentMonth
        //     }
        //     return currentDate.getFullYear()+"-"+currentMonth+"-"+currentDate.getDate()+"T"+currentDate.getHours()+":"+currentDate.getMinutes()+":"+currentDate.getSeconds()
        // },
        calculateTimeLeft(deadline) {
            let today = new Date();
            let ourDate = new Date(deadline);
            if(today > ourDate) {
                let diff = today.getTime() - ourDate.getTime();
                let days = Math.ceil(diff / (1000*3600*24))
                return days + " days late"
            }
            else if(today == ourDate) {
                return "Due today"
            }
            else {
                let diff = ourDate.getTime() - today.getTime();
                let days = Math.ceil(diff / (1000*3600*24))
                return days + " days left"
            }
        },
        dateToString(ourDate) {
            let dateDate = new Date(ourDate);
            return dateDate.toString().substring(4, 15)
        },
        checkToShow(id) {
            for(let i=0;i<this.showModal.length;i++) {
                if(this.poaList[i].id == id) {
                    //alert(this.poaList[i].deadline.substring(0, this.poaList[i].deadline.length-4))
                    return this.showModal[i]
                }
            }
            return false
        },
        closeForm(id) {
            // for(let i=0;i<this.poaList.length;i++) {
            //     if(this.poaList[i].id == id) {
            //         //alert(this.poaList[i].title)
            //         if(this.poaList[i].title == "") {
            //             this.poaList[i].title = "Default Title"
            //         }
            //         if(this.poaList[i].description == "") {
            //             this.poaList[i].description = "Default Description"
            //         }
            //     }
            // }
            this.editMileStone(id, false)
        },
        editMileStone(id, newVal) {
            this.showModal = []
            for(let i=0;i<this.poaList.length;i++) {
                    this.showModal.push(false)
            }
            for(let i=0;i<this.showModal.length;i++) {
                    if(this.poaList[i].id == id) {
                    this.showModal[i] = newVal
                    //alert(this.showModal[i])
                }
            }
        },
        submitEdits(id) {
            this.$emit("edit-milestone", id, document.getElementById("title"+id).value, document.getElementById("desc"+id).value, document.getElementById("chooseDate"+id).value)
            for(let i=0;i<this.showModal.length;i++) {
                if(this.poaList[i].id == id) {
                    this.showModal[i] = false
                    return null
                }
            }
        }
  },
  emits: ['complete-milestone', "edit-milestone"],
}
</script>

<style scoped>
    input, textarea {
        border: solid black 3px;
        font-size: medium;
    }
    #descLabel {
        margin-bottom: 0;
    }
    .milestone {
        border: 5px solid #110F32;
        border-collapse: collapse;
        list-style-type: none;
        padding: 0.2rem;
        padding-top: 0.4rem;
    }
    .poaTitle {
        font-size: medium;
        font-weight:400;
        width: 20rem;
    }
    .poaDate, .poaTimeLeft {
        width: 10rem;
    }
    .poaUndertext, .poaDate, .poaTimeLeft {
        color: #BDC9E3;
        font-weight: 500;
    }
    .poaTitle, .poaUndertext, .poaDate, .poaTimeLeft {
        margin-bottom: 0.2rem;
        display: inline-block;
    }
    .poaComplete {
        float: right;
        margin-right: 1rem;
        border: solid white 0.2rem;
        color: white;
        background-color: #00001A;
        font-weight: bold;
        width: 5rem;
        height: 2rem;
    }
    .poaComplete:hover {
        color: #00001A;
        background-color: white;
    }
    .poaEdit:hover {
        color: #00001A;
        background-color: #243B6F;
    }
    .poaEdit {
        float: right;
        background-color: #00001A;
        color: #243B6F;
        border: solid #243B6F 0.2rem;
        width: 4rem;
        height: 2rem;
        font-weight: bold;
    }
    .modal-overlay {
        position: absolute;
        top: 0;
        left:0;
        right:0;
        bottom:0;
        z-index: 98;
        background-color: rgba(0,0,0,0.3);
    }
    .modal {
        position: fixed;
        display: block;
        max-height: 80%;
        height: auto;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 99;
        width: 100%;
        max-width: 600px;
        background-color: #FFF;
        font-style: normal;
        font-size: medium;
        color: black;
        border-radius: 16px;
        padding: 25px;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 0.5s;
    }

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    .slide-enter-active,
    .slide-leave-active {
        transition: transform .5s;
    }

    .slide-enter,
    .slide-leave-to {
        transform: translateY(-50%) translateX(100vw);
    }
</style>