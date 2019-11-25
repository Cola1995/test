<template>
<h1>:{{title}}</h1>    
</template>
<script>
import { isMethod } from 'babel-types'
export default {
    name:"Ljob",
    data(){

        return{
        title:null
        
        }
    },
    mounted(){
        this.initjob()
    },
    methods:{
    
        initjob(){
            var that = this;
            this.$axios.request({

                url:this.$store.state.apilist.job,
                method:"GET",
                params:{
                    token:this.$store.state.token
                }
            }).then(function(ret){
                if (ret.data.code===1000){
                    that.title = ret.data.title
                }

            }).catch(function(){



            })
               


            
            
        }
    }
}
</script>

<style>

</style>