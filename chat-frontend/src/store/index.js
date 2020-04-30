import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const socketBase = "ws://127.0.0.1:8000/ws/chat/";
const BASEURL = "http://127.0.0.1:8000/chat/";

var AUTHBASEURL = BASEURL + 'auth/';

//guestUsers
// var guest = { 
//               'login' : AUTHBASEURL +'login/',
//               'logout' : AUTHBASEURL + 'logout/',
//               'verify' : AUTHBASEURL+'token/verify/'
//             };

// var registered = {
//                   login : AUTHBASEURL+'token/login/',
//                   logout : AUTHBASEURL+'token/logout/',
//                   me : AUTHBASEURL+'users/me/',
//                   }
var general = {
              loadChat : BASEURL+'preload/',
              getRooms : BASEURL+'get-rooms/'
}





export default new Vuex.Store({
  state: {
    user : {
      username : null,
      key:null,
      verified:false,
    },
  
   
    currentChatRoom: {
      
        name:'Campus chat room',
        uri:'9601a4cff33949b',
    },

   AUTHBASEURL:AUTHBASEURL,

   URLS : { 
    login : AUTHBASEURL +'temp-login/',
    logout : AUTHBASEURL + 'logout/',
    verify : AUTHBASEURL+'token/verify/'
        },
    
    general : general,
 
    
  },
  getters :{
    socketURL: state => {
      return socketBase+state.currentChatRoom.uri;
    }
  },
  mutations: {
    updateChatRoom(state,chatRoom)
    {
      state.currentChatRoom = chatRoom
    },

    updateUser(state,user){
      state.user = user;
   
    },

  },
  actions: {
  },
  modules: {
  }
})
