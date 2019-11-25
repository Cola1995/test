// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'     /*引入element */
import 'element-ui/lib/theme-chalk/index.css'   /* 全局引入element-ui样式 */
import store from './vuex/store'   //引入vuex中store
import { Message, Select } from 'element-ui';  //引入element ui 组件

//在vue的全局变量中设置了$axios=axios
//在每个组件中使用：this.$axios
Vue.prototype.$axios = axios

Vue.config.productionTip = false
Vue.use(ElementUI)
// Vue.use(Message)
// Vue.use(Select)
Vue.prototype.$message = Message;   //全局设置消息组件

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',

  // render: h => h(App)
});
//拦截器
router.beforeEach((to, from, next) => {
  if(to.meta.requireAuth) { // 如果路由项需要权限校验
    /* 
      从Vuex拿出token码，说明已登陆
     （前端的token可伪造，所以这并不是完全靠谱，后面继续说）
    */
    if (store.state.token) { 
      next() // 正常跳转页面
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}  
        /* 将跳转的路由地址作为参数带给登陆页，登录成功后跳转回该页面 */
      })
    }
  } else { // 如果不需要权限校验，直接进入路由页面
      next();
  }
})
