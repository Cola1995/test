<template>
    <h1>课程详细页面</h1>
</template>
<script>
export default {
    name:"detail",
    data(){
        return {

        }
        
    }
    ,
    mounted(){
        console.log(this.$route.params.id)
    }
}
</script>
<style scoped>

</style>