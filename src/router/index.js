import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Lheader from '@/components/Lheader'
import Lindex from '@/components/Lindex'
import Lcourse from '@/components/Lcourse'
import Ljob from '@/components/Ljob'
import Lscience from '@/components/Lscience'
import detail from '@/components/detail'
import Login from '@/components/Login'



Vue.use(Router)
var course_detail = {
  template:"<h1>课程详细</h1>"
}
export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Lheader',
    //   component: Lheader,
    // },
    {
      path:"/",
      name:"Lindex",
      component:Lindex,
    },
    {
      path:"/course",
      name:"Lcourse",
      component:Lcourse
    },
    {
      path:"/job",
      name:"Ljob",
      component:Ljob,
      meta:{
        requireAuth:true,  //该路由需要权限验证
      }
    },
    {
      path:"/lscience",
      name:"Lscience",
      component:Lscience
    },
     {
      path:"/detail/:id",
      name:"detail",
      component:detail
    },
    {
      path:"/login",
      name:"Login",
      component:Login
    },
    {
      path:"/course_detail",
      component:course_detail
    }

  ],
  mode:"history", //去掉url中# 号
})
