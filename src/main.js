// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'     /*引入element */
import 'element-ui/lib/theme-chalk/index.css'   /* 全局引入element-ui样式 */


//在vue的全局变量中设置了$axios=axios
//在每个组件中使用：this.$axios
Vue.prototype.$axios = axios

Vue.config.productionTip = false
Vue.use(ElementUI)


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',

  // render: h => h(App)
})
