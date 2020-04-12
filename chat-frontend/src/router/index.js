import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/loginpage.vue'
import Homepage from '../views/homepage.vue'
import Gossippage from '../views/gossippage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Loginpage',
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
    path : '/home',
    component: Homepage,
    name : 'Homepage'
  },
  {
    path : '/rooms',
    component: Gossippage,
    name : 'Gossippage'
  }
 
]

const router = new VueRouter({
  routes,
  mode:'history'
})


// router.beforeEach((to, from, next) => {
//   if (sessionStorage.getItem('authToken') !== null || to.path === '/') {
//     next()
//   }
//    else {
//     next('/')
//   }
// })



export default router
