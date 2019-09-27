import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'  //引入cookies
Vue.use(Vuex)

// const state = {
//     count: 0,
    
// }

export default new Vuex.Store({
    state:{
        count:0,
        username:Cookie.get("username"),
        token:Cookie.get("token")
    },
    mutations:{
        saveToken:function(state,userInfo){
            state.username = userInfo.username;
            state.token = userInfo.token;
            Cookie.set("username",userInfo.username,"20min")
            Cookie.set("token",userInfo.token,"20min")


        },
        clearToken:function(state){
            state.username = null
            state.token = null
            Cookie.remove("username")
            Cookie.remove("token")
        },
    }
})