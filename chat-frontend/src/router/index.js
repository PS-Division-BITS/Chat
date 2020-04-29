import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/loginpage.vue'
import Homepage from '../views/homepage.vue'
import Gossippage from '../views/gossippage.vue'
import Logoutpage from '../views/logoutpage.vue'
import Register from '../views/register.vue'

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
  
  },
  {
    path :'/register',
    component: Register,
    name : 'Register'
  }
 
]

const router = new VueRouter({
  routes,
  mode:'history'
})


router.beforeEach((to, from, next) =>
{
    
      console.log('in router : username = %s to.path = %s',store.state.user.username,to.path);
  
      if(to.path!== '/' && tokenExist() == false)
      {
      console.log('redirecting to /')
      next('/')
      }
      if(to.path!== '/logout' && tokenExist() && verifyToken() === false)
      { 
        console.log('Invalid token, redirecting to logout...')
        console.log('redirecting to /logout')
        next('/logout')
      }
        console.log('CURRENT PATH = '+to.path)
      next();
 })




function tokenExist(){
  if(typeof store.state.user == 'undefined' || store.state.user.username == null || store.state.user.key == null)
 {
  console.log('token does not exist') 
  return false
}
console.log('Token exists')
  return true
}


async function verifyToken ()
{
  
  var flag;

 
  console.log('Verifying token ...')
  const params = new URLSearchParams()
  params.append('username',store.state.user.username)
  params.append('token',store.state.user.key)

  await axios.post(store.state.URLS.verify, params)
  .then(response=>{
      
      flag = response.data.verified;
     
      console.log("Token verified : "+flag)
    
      return flag;
  })
  .catch(error=>{
    console.log('in router',error)
    return false;
  })  
 

  

}


export default router
