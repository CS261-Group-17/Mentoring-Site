<template>
    <ol>
        <li v-for="sw in swlist" :key="sw.id">
            <select v-model="sw.text">
                <option disabled value="">Nothing Selected</option>
                <option v-for="option in categories.options" :value="option.value" :key="option.value">
                    {{ option.text }}
                </option>
            </select> 
        </li>
    </ol>
</template>

<script>
export default {
    name:"SWList",
    props: {
        swlist: Array,
        givenSWs: Array
    },
    components: {},
    data() {
        return {
            categories: {}
        }
    },
    created() {
        this.categories =  {
            options: this.givenSWs
        }
    },
}
</script>

<style> 
    ol {
        margin-bottom: 0rem !important;
    }
</style>