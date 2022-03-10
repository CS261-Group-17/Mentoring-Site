<template>
    <ol>
        <li v-for="sw in swlist" :key="sw.id">
            <select v-model="sw.val">
                <option disabled value="">Nothing Selected</option>
                <option v-for="option in categories.options" :value="option.text" :key="option.text">
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
        swlist: Array
    },
    components: {},
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
    },
}
</script>

<style> 
    ol {
        margin-bottom: 0rem !important;
    }
</style>