<template>
  <el-row>
    <el-col :span="8" class="el-col-offset-8">
      <div class>
        <h2>登录</h2>
        <el-input v-model="username" placeholder="请输入用户名"></el-input>

        <el-input v-model="password" placeholder="请输入密码" class="password" show-password></el-input>

        <el-button type="primary" @click="login()">登录</el-button>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
        username:"",
        password:""
    }
    
  },



  methods:{

      login(){
        this.$axios
        .request({
          url: "http://127.0.0.1:8005/api/v2/auth/",
          method: "POST",
          data:{
              username:this.username,
              password:this.password
          },
          headers:{
              "Content-Type":"application/json"}
          
        })
        .then(function(ret) {
          //ajax请求发送成功后执行函数
          console.log(ret.data);
          
        })
        .catch(function(ret) {
          //失败后执行函数
        });


      }
  }
};
</script>

<style>
.password {
  margin-top: 10px;
}
</style>