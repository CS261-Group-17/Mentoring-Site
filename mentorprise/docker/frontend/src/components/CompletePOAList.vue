<template>
    <ul>
        <li v-for="poa in poaList" :key="poa.id" class="milestone">
            <p class="poaTitle">{{poa.title}}</p>
            <button class="poaGone" @click="onDelete(poa.id)"><fa icon="xmark" size="2x"/></button>
            <button class="poaUndo" @click="this.$emit('undo-milestone', poa.id)">Undo</button>
            <br>
            <p class="poaUndertext">{{poa.description}}</p>
        </li>
    </ul>
    <p id="anyComplete">{{anyComplete()}}</p>
</template>

<script>
export default {
  name: "CompletePOAList",
  props: {
      poaList: Array
  },
  components: {},
  methods: {
      onDelete(id) {
          this.$emit("delete-cancelled", id)
      },
      anyComplete() {
          if(this.poaList.length == 0) {
              return "You appear to have no completed milestones"
          }
          return ""
      }
  },
  emits: ["delete-cancelled", "undo-milestone"]
}

</script>

<style scoped>
    #anyComplete {
        /* color: #243B6F;
        font-weight: bold; */
        font-size: medium;
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
    .poaUndertext {
        color: #BDC9E3;
        font-weight: 500;
    }
    .poaTitle, .poaUndertext {
        margin-bottom: 0.2rem;
        display: inline-block;
    }
    .poaUndo {
        padding-top: 0.3rem;
    }
    .poaGone, .poaUndo {
        float: right;
        background-color: #00001A;
        color: #243B6F;
        border: 0px;
        font-weight: bold;
    }
</style>