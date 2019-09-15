<template>
  <div>
      <!-- 废弃 -->
    <!-- <h1>我是课程页面</h1>
    <ul>
      <li v-for="(item,index) in courseList" :key="index">
        <router-link :to="{name:'detail',params:{id:item.id}}">{{item.title}}</router-link>
      </li>
    </ul> -->
    <h1>我是课程页面</h1>
    <el-row>
      <el-col :span="18" class="el-col el-col-offset-3">
        <div >
          <el-row>
              <!-- 每行6span 显示3 快 -->
            <el-col :span="6" v-for="(o, index) in courseList" :key="index" :offset="index%3 !== 0 ? 2 : 0" :class="{dd:1}">
              <el-card :body-style="{ padding: '10px'}" shadow="hover">
                <img
                  src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                  class="image"
                />
                <div style="padding: 14px;">
                  <span>{{o.title}}</span>
                  <div class="bottom clearfix">
                    <time class="time">{{ o.level }}</time>
                    <!-- <router-link :to="{name:'detail',params:{id:o.id}}">{{o.title}}</router-link> -->
                    <el-button type="text" class="button">查看详情</el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default {
  name: "Lcourse",
  data() {
    return {
      courseList: [
        //    {"id":1,"title":'Python全栈'},
        //       {"id":2,"title":'Linux运维'},
        //       {"id":3,"title":'金融分析'},
      ]
    };
  },
  mounted: function() {
    //vue页面刚加载时自动执行
    this.initCourse();
  },
  methods: {
    initCourse() {
      var that = this;
      this.$axios
        .request({
          url: "http://127.0.0.1:8005/api/v2/course/",
          method: "GET"
        })
        .then(function(ret) {
          //ajax请求发送成功后执行函数
          console.log(ret.data);
          that.courseList = ret.data.data;
        })
        .catch(function(ret) {
          //失败后执行函数
        });
    }
  }
};
</script>

<style  scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
/* 每个card 添加间隔 */
.dd{
    margin-bottom: 10px;
}
</style>