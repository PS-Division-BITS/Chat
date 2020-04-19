import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/loginpage.vue'
import Homepage from '../views/homepage.vue'
import Gossippage from '../views/gossippage.vue'
import Logoutpage from '../views/logoutpage.vue'

import store from '../store'
import axios from  'axios'



Vue.use(VueRouter,store)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path : '/chat',
    component: Homepage,
    name : 'Homepage'
  },
  {
    path : '/rooms',
    component: Gossippage,
    name :'Chatrooms'
  },
  {
    path : '/logout',
    component : Logoutpage,
    name : 'Logout'
  
  }
 
]

const router = new VueRouter({
  routes,
  mode:'history'
})


router.beforeEach= function(to, from, next)
{
    
      console.log('in router : username = %s to.path = %s',store.state.user.username,to.path);
  
      if(to.path!== '/' && verifyToken() === false)
      next('/logout')
 }







function verifyToken()
{
  
  var flag = false;

  if(typeof store.state.user == 'undefined' || store.state.user.username == null || store.state.user.key == null)
  return false
  console.log('here')
  axios.get(store.state.AUTHBASEURL+'verify/?user='+JSON.stringify(store.state.user))
  .then(response=>{
      flag = response.data.verified;
  })
  .catch(error=>{
    console.log(error)
    flag = false;
  })  
  flag = true;

  return flag;

}


export default router
