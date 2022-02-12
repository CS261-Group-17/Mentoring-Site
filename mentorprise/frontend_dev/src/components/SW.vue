<template>
    {{point.swdesc}}
</template>

<!--
    point: {
        id: Number,
        swnum: Number
        swdesc: String
    }
-->
<script>
export default {
    name: "SW",
    props: {
        point: Object
    }
}
</script>