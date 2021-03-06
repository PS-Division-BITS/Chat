import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/axios'
import './plugins/bootstrap-vue'
import App from './App.vue'
import store from './store'
import router from './router'
Vue.config.productionTip = false

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret,faVolumeUp, faVolumeMute, faWindowClose} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
 
library.add(faUserSecret)
library.add(faVolumeUp)
library.add(faVolumeMute)
library.add(faWindowClose)
 
Vue.component('font-awesome-icon', FontAwesomeIcon)

import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
Vue.use(VueSidebarMenu)


import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
Vue.use(SequentialEntrance);

import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
Vue.use(Loading)

//import VueEvents from 'vue-events' // to be uninstalled
// import VueSocketIO from 'vue-socket.io'
// import SocketIO from "socket.io-client"




// const options = { path: '/my-app/' };

// Vue.use(new VueSocketIO({
//   debug: true,
//   connection: SocketIO('http://metinseylan.com:1992', options), //options object is Optional
//   vuex: {
//     store,
//     actionPrefix: "SOCKET_",
//     mutationPrefix: "SOCKET_"
//   }
// })
// );


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
