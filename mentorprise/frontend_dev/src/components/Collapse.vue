<template>
  <div v-for="(v, i) in list" :key="i" class="collapse-card">
    <div
      class="collapse-list"
      data-bs-toggle="collapse"
      :data-bs-target="'#collapse_' + random + i"
      aria-expanded="false"
    >
      <div :style="!v.complete_by ? 'width:auto' : 'width:33%'">
        <svg
          viewBox="64 64 896 896"
          focusable="false"
          data-icon="right"
          class="arrow"
          width="1em"
          height="1em"
          fill="#2b3d75"
          aria-hidden="true"
        >
          <path
            d="M765.7 486.8L314.9 134.7A7.97 7.97 0 00302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 000-50.4z"
          ></path>
        </svg>
        &nbsp; {{ v.upcoming_milestones }}
      </div>
      <div v-if="v.complete_by" style="color: #bdc9e3; width: 33%">
        {{ v.complete_by }}
      </div>
      <div v-if="v.time_remaining" style="color: #bdc9e3; width: 33%">
        {{ v.time_remaining }}
      </div>
      <button v-if="v.showButton" class="end" @click="this.$emit('end_relationship', v.username)">
        End Relationship
      </button>
    </div>
    <div class="collapse collapse-content" :id="'collapse_' + random + i">
      {{ v.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Collapse",
  props: {
    list: Array,
    random: String,
  },
  emits: ['end_relationship']
};
</script>

<style scoped>
.collapse-card {
  border: 3px solid #110f32;
  padding: 10px 0;
}
.collapse-card + .collapse-card {
  border-top: none;
}
.collapse-list {
  display: flex;
  justify-content: space-between;
}
.collapse-list[aria-expanded="true"] .arrow {
  transition: transform 0.24s;
  color: #2b3d75;
  font-weight: 900;
  transform: none;
}
.collapse-list[aria-expanded="true"] .arrow {
  transition: transform 0.24s;
  transform: rotate(90deg);
}
.collapse-content {
  margin-left: 26px;
  color: #bdc9e3;
}
.end {
  color: white;
  border: solid white 2px;
  background-color: #00001a;
  margin-right: 1rem;
}
.end:hover {
  color: black;
  background-color: white;
}
</style>
