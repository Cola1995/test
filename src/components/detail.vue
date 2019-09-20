<template>
  <div>
    <h1>课程详细页面</h1>
    <p>{{detail.title}}</p>
    <p>口号:{{detail.slogon}}</p>
    <p>推荐课程:
        <ul>
            <li v-for="(i,index) in detail.recommends"  :key=index>
                {{i.title}}
            </li>
        </ul>


    </p>
    <p>章节:
         <ul>
            <li v-for="(i,index) in detail.chapter"  :key=index>
                {{i.name}}
            </li>
        </ul>


    </p>
    
  </div>
</template>
<script>
export default {
  name: "detail",
  data() {
    return {
      detail: {
        title: null,
        why: null,
        slogon: null,
        recommends: [],
        chapter: []
      }
    };
  },
  mounted() {
    // console.log(this.$route.params.id)\
    this.initDeatil();
  },
  methods: {
    initDeatil() {
      var that = this;
      var cid = this.$route.params.id
      this.$axios
        .request({
          url: "http://127.0.0.1:8005/api/v1/course/"+cid+"/",
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
    }
  }
};
</script>
<style scoped>


</style>