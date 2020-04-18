import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/loginpage.vue'
import Homepage from '../views/homepage.vue'
import Gossippage from '../views/gossippage.vue'
import Logoutpage from '../views/logoutpage.vue'

import store from '../store'
//import axios from  'axios'



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


router.beforeEach((to, from, next) => {
  console.log('in router : username = '+store.state.user.username);
  if ((typeof store.state.user === 'undefined' || store.state.user.username === null) && to.path !==  '/') {
  
    next('/')
  }
   else {
      
    next()
      // if(verifyToken() || to.path === '/logout' )
      // next()
      // else
      // {
      // console.log('error')
      // next('/logout')
      // }
    }

 
})

// function verifyToken()
// {
//   if (typeof store.state.user === 'undefined') {
//     return false
// }


//   axios.get(store.state.AUTHBASEURL+'verify/?user='+JSON.stringify(store.state.user))
//   .then(response=>{
//       if(response.data.verified)
//       return true;
//       else return false;
//   })
//   .catch(error=>{
//     console.log(error)
//     return false;
//   })  

// }


export default router
