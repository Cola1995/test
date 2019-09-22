<template>

 
<el-header >
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1"><router-link to="/" >首页</router-link></el-menu-item>
  <el-menu-item index="2"><router-link to="/course">课程</router-link></el-menu-item>
  <el-menu-item index="3"><router-link to="/job">微职位</router-link></el-menu-item>
  <el-menu-item index="4"><router-link to="/lscience"><span>深科技</span></router-link></el-menu-item>
    <el-menu-item index="5"><router-link to="/login">登录</router-link></el-menu-item>

</el-menu>
<div class="line"></div>




</el-header>
   
</template>
<script>
export default {
    name:"Lheader",
    data(){

        return{
             activeIndex: '1',
            
            
        };
    },
     methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        // this.activeIndex=key;
      },
      
    },
    created:function(){
        // alert("元素加载完成前执行");  
        //比较蠢的方法判断当前路由及下划线，后期改成动态数据方式
        console.log(this.$route.path)
        if (this.$route.path==="/lscience"){
          this.activeIndex="4"
        }else if(this.$route.path==="/"){
          this.activeIndex="1"
        }else if(this.$route.path==="/course"){
          this.activeIndex="2"
        }else{
          this.activeIndex="3"
        }
      }


}
</script>

<style scoped>


</style>