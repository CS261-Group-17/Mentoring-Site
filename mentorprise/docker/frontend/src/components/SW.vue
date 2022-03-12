<template>
    <select v-model="point.val">
        <option disabled value="">Nothing Selected</option>
        <option v-for="option in categories.options" :value="option.text" :key="option.text">
            {{ option.text }}
        </option>
    </select>
</template>

<!--
    point: {
        id: Number,
        val: String
    }
-->
<script>
export default {
    name: "SW",
    props: {
        point: Object
    },
    data() {
        return {
            categories: {}
        }
    },
    created() {
        this.categories =  {
            options: [
                { value:"tennis", text: "Tennis"},
                { value:"team", text: "Teamwork"},
                { value:"communication", text: "Communication"},
                { value:"friendly", text: "Friendly"}
            ]
        }
    }
}
</script>