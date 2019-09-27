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
      username: "",
      password: ""
    };
  },

  methods: {
    login() {
      var that = this;
      this.$axios
        .request({
          url: "http://127.0.0.1:8005/api/v2/auth/",
          method: "POST",
          data: {
            username: this.username,
            password: this.password
          },
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(ret) {
          //ajax请求发送成功后执行函数
          if (ret.data.code === 1000) {
            //登陆成功弹窗
            that.$message({    
              message: "恭喜你，登陆成功",
              type: "success"
            });

            // console.log(ret.data.token);
            // console.log(that.$store.state.username);

            that.$store.state.token = ret.data.token; //设置token
            that.$store.state.username = that.username; //设置username 注意内层函数this要写that
           
            // 执行mutations自定义方法
            that.$store.commit("saveToken", {
              token: ret.data.token,
              username: that.username
            });
          } else {
             that.$message.error("用户名或密码错误");
            // alert(ret.data.error);
          }
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