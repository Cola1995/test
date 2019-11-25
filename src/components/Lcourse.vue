<template>
  <div>
    <!-- 废弃 -->
    <!-- <h1>我是课程页面</h1>
    <ul>
      <li v-for="(item,index) in courseList" :key="index">
        <router-link :to="{name:'detail',params:{id:item.id}}">{{item.title}}</router-link>
      </li>
    </ul>-->
    <h1></h1>

    <!-- 课程图标 -->

    <div class="counter">
      <div class="icon-course">
        <i class="el-icon-notebook-1">课程</i>
      </div>
      <!-- 课程子类列表 -->
      <div class="course_list">
        <ul>
          <li
            
            v-for="(csub,index) in coursesub_List"
            :key="index"
            
            :class="{check:csub.id===checked}"
            @click="test(csub.id)"
          >{{csub.name}}</li>
        </ul>
      </div>
      <!-- 课程图片 -->
      <div class="courseimg">
        <el-row>
          <el-col
            :span="4"
            v-for="(o, index) in course_List"
            :key="index"
            :offset="index%5 !== 0? 1 : 0 "
            :class="{dd:1}"
          >
            <el-card :body-style="{ padding: '0px' }">
              <img
                src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image"
              />
              <div style="padding: 14px;">
                <span>{{o.name}}</span>
                <div class="bottom clearfix">
                  <time class="time">{{ o.level }}</time>
                  <el-button type="text" class="button">
                    <router-link :to="{name:'detail',params:{id:o.id}}">查看详情</router-link>
                    </el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Lcourse",
  data() {
    return {
      coursesub_List: [
        // {
        //   name: "Python"
        // },
        // {
        //   name: "Java"
        // },
        // {
        //   name: "Go语言"
        // },
        // {
        //   name: "VUE"
        // }
      ],
      course_List: [
        // {
        //   id: 1,
        //   name: "python基础",
        //   course_img: "111",
        //   level: "初级"
        // },
        // {
        //   id: 2,
        //   name: "pycahram使用密集",
        //   course_img: "111",
        //   level: "中级"
        // },
        // {
        //   id: 3,
        //   name: "java面向对象编程",
        //   course_img: "2222",
        //   level: "中级"
        // }
      ],
      checked:-1,
    };
  },
  mounted: function() {
    //vue页面刚加载时自动执行
    this.initCourse(); // 加载课程子类列表
    this.initallCourseList(); //加载所有课程
  },
  methods: {
    initCourse() {
      var that = this;
      this.$axios
        .request({
          url: this.$store.state.apilist.course,
          method: "GET"
        })
        .then(function(ret) {
          //ajax请求发送成功后执行函数
          // console.log(ret.data);
          that.coursesub_List = ret.data.data;
        })
        .catch(function(ret) {
          //失败后执行函数
        });
    },
    // 加载所有课程列表
    initallCourseList(){
      var that = this;
      this.$axios.request({
        url:this.$store.state.apilist.course_list,
        method:"GET"
      }).then(function(ret){
          //成功执行函数
      that.course_List = ret.data.data;
      }).catch(function(ret){
        //异常执行函数

      });

      

    },
    // 筛选子类课程函数
    test(id) {
      var that = this
      this.checked=id
      // alert(id);
      this.$axios.request({
        url:this.$store.state.apilist.course_list,
        method:"GET",
        params:{
          pk:id
        }
      }).then(function(ret){
        that.course_List = ret.data.data

      }).catch(function(){

      })
    }
  }
};
</script>

<style  scoped>
/* 布局样式 */
/* .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  } */
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

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
.dd {
  margin-bottom: 15px;
}

.icon-course {
  padding-left: 0px;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 30px;
}
.course_list {
  padding: 20px 0px;
}
.course_list ul li {
  float: left;
  margin-right: 20px;
  list-style: none;
  cursor: pointer; /**鼠标移动变小手 */
  
}
.counter {
  margin-left: 20px;
}
.courseimg {
  clear: both;
  padding: 20px;
  /* background: yellow; */
}
.firstli {
  margin-left: -36px !important;
}
.check{
  color:rgb(235,168,68);
}
</style>