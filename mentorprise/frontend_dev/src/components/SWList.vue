<template>
    <ol>
        <li v-for="sw in swlist" :key="sw.id">
            <SW :point="sw"/>   
        </li>
    </ol>
</template>

<script>
import SW from "./SW.vue"
export default {
    name:"SWList",
    props: {
        swlist: Array
    },
    components: {
       SW 
    }
}
</script>