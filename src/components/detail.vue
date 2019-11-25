<template>
  <div>
    <el-main>
      <div class="tiao">
        <div class="back-href">返回课程主页</div>
        <div class="course">
          <div class="course_title">Pyhton21天入门</div>课程小结：87小节时长：19小时 16661人在学
        </div>
        <div class="course_route">
          <!-- <div class="route" ><span >课程详情</span></div>
          <div class="route"><span>讨论提问（159）</span></div>
          <div class="route"><span>课件下载</span></div> -->

             <div class="radio-group">   
        <span 
           v-for="(tab ,index) in tabs" 
           :key=index
           :class="{cur:iscur==index}" 
           @click="iscur=index,tabChange('select' + (index + 1))" >
             
            {{tab.name}}
             
        </span>  
        <!-- <span v-else>

        </span> -->
      </div>  
        </div>
        <!-- <div :is = "zuajian" keep-alive></div> -->

      </div>
    
      <div style="margin:10px 0;"></div>  
      <keep-alive>   
        <component v-bind:is="tabView"></component>  
      </keep-alive> 
      <div class="teacher">

      </div>
    </el-main>
  </div>
</template>
<script>

import select1 from '@/components/zujian1'
import select2 from '@/components/zujian2'
import select3 from '@/components/zujian3'
export default {
  name: "detail",
  data() {
    return {
      detail: {
        id: null,
        title: null,
        why: null,
        slogon: null,
        recommends: [],
        chapter: [],

      },
      tabView: 'select1',
          iscur: 0,   
          tabs: [{name:"课程详情"}, {name: "讨论提问"} ,{name: "课件下载"}]
      // zujian:"zujian1",
    };
  },

  
   components:{
      select1,
      select2,
      select3
    },
  mounted() {
    // console.log(this.$route.params.id)\
    var cid = this.$route.params.id;
    this.initDeatil(cid);
  },
  methods: {
    initDeatil(cid) {
      var that = this;
      // console.log(that.$store.state.apilist.detail+cid+"/")
      this.$axios
        .request({
          url: that.$store.state.apilist.detail + cid + "/",
          method: "GET"
        })
        .then(function(ret) {
          //ajax请求发送成功后执行函数
          console.log(ret.data);
          that.detail = ret.data.data;
        })
        .catch(function(ret) {
          //失败后执行函数
        });
    },
    changedetail(id) {
      // alert(id)
      this.initDeatil(id);
      this.$router.push({ name: "detail", params: { id: id } }); //解决推荐课程路由切换问题
    },
    // course_detail(){
    //   alert("ok")
    // }
    // tab(m){
    //   this.zujian = m;
    // }

    tabChange:function(tab){  
      this.tabView = tab;  
    }  


  }
};
</script>
<style scoped>
.tiao {
  background: rgb(90, 60, 71);
  height: 300px;
  width: 100%;
  margin-top: 20px;
}

* {
  margin: 0px;
  padding: 0px;
}
.back-href {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 15px;
  color: white;
  padding: 15px 0px;
  margin-left: 20px;
  /* line-height: 10px; */
}
.course {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 15px;
  color: white;
  margin-left: 20px;
}
.course_title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 30px;
  padding: 5px;
}
.course_route{
  margin-top: 140px;
  /* background:red; */
  height: 30px;
}
.cur{
   font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 16px;
  /* float: left; */
  padding-bottom: 5px;
  color: white;
  /* border-style: dashed; */
  /* margin-left: 10px; */
  border-bottom: 2px seashell solid;
  
}
.radio-group{
  clear: both;
  margin-top: 10px;
   font-family: Helvetica Neue,Helvetica,Microsoft YaHei,Arial,sans-serif;
    
  font-size: 16px;
  color: white;
}
.radio-group span{
  margin-left: 16px;
  cursor: pointer;
}

.teacher{
  width: 380px;
  height: 525px;
  background-color: chartreuse;
  position:absolute;
  top: 140px;
  left: 1455px;
  box-shadow: 0 2px 4px 0 #f3f3f3;
  border-radius: 6px;
}
</style>