import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/loginpage.vue'
import Homepage from '../views/homepage.vue'
import Gossippage from '../views/gossippage.vue'

import store from '../store'

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
    name : 'Logout'
  }
 
]

const router = new VueRouter({
  routes,
  mode:'history'
})


router.beforeEach((to, from, next) => {
  if (store.state.user.username === null && to.path !==  '/') {
  
    next('/')
  }
   else {
    
      next()
  }

 
})




export default router
