import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Lheader from '@/components/Lheader'
import Lindex from '@/components/Lindex'
import Lcourse from '@/components/Lcourse'
import Ljob from '@/components/Ljob'
import Lscience from '@/components/Lscience'
import detail from '@/components/detail'

Vue.use(Router)

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
      component:Ljob
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
    

  ],
  mode:"history", //去掉url中# 号
})
