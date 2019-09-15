<template>
    <!-- <h1>我是首页</h1> -->
    <el-main>
        <el-carousel indicator-position="outside" height="600px">
    <el-carousel-item v-for="(item,index) in banerArr" :key="index">
      <!-- <h3>{{ item.src }}</h3> -->
      <img :src="item.src" alt="">
    </el-carousel-item>
  </el-carousel>
    <!-- <img src="../assets/logo.png" alt=""> -->
        
    </el-main>
</template>

<script>
export default {
    name:"Lindex",
    data(){
        return{
            banerArr:[
                {id:"1",src:"../../static/root.jpg"},
                {id:"2",src:"../../static//boy1.jpg"},
                {id:"3",src:"../../static/boy2.jpg"},
                {id:"4",src:"../../static/boy3.jpg"},

            ]

            

        }


    }
}
</script>
<style  >
.el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    /* height: 600px; */
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  body{
    background-color:#DCDFE6;
    /* padding: 0;
    margin: 0; */
  }
</style>