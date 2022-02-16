<template>
    <ul>
        <li v-for="poa in poaList" :key="poa.id" class="milestone">
            <p class="poaTitle">{{poa.title}}</p>
            <p class="poaDate">{{dateToString(poa.deadline)}}</p>
            <p class="poaTimeLeft">{{calculateTimeLeft(poa.deadline)}}</p>
            <button class="poaEdit"><fa icon="pencil" size="1x"/>&nbsp;Edit</button>
            <button @click="this.$emit('complete-milestone', poa.id)" class="poaComplete">Complete</button>
            <br>
            <p class="poaUndertext">{{poa.desc}}</p>
        </li>
    </ul>
</template>

<script>
export default {
  name: "POAList",
  props: {
      poaList: Array
  },
  components: {},
  methods: {
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
      }
  },
  emits: ['complete-milestone'],
}
</script>

<style scoped>
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
    .poaEdit {
        float: right;
        background-color: #00001A;
        color: #243B6F;
        border: solid #243B6F 0.2rem;
        width: 4rem;
        height: 2rem;
        font-weight: bold;
    }
</style>