import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
const ip = "localhost";
const socketBase = "ws://"+ip+":8000/ws/chat/";
const BASEURL = "http://"+ip+":8000/chat/";

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
        uri:'1',
    },
    
    error:false,
    errorMessage:"Error connecting to the server",

   URLS : { 
    login : AUTHBASEURL +'temp-login/',
    logout : AUTHBASEURL + 'logout/',
    verify : AUTHBASEURL+'token/verify/',
    general :general
        },
    
  
 
    
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
    error (state,bl,msg)
    {
    
      state.error=bl;
      state.errorMessage=msg;
    }

  },
  actions: {
  },
  modules: {
  }
})
