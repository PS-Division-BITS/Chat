import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
const ip = "www.bpgc.in";
const socketBase = "ws://"+ip+"/ws/chat/";
const BASEURL =  "http://"+ip+"/chat/";

var AUTHBASEURL = BASEURL + 'auth/';

const GITREPO = 'https://github.com/PS-Division-BITS/Chat/'

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
              getRooms : BASEURL+'get-rooms/',
              getStats : BASEURL+'get-stats/'
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
    errorMessage:"",

   URLS : { 
    login : AUTHBASEURL +'temp-login/',
    logout : AUTHBASEURL + 'logout/',
    verify : AUTHBASEURL+'token/verify/',
    general :general
        },
    GITREPO:GITREPO    
    
  
 
    
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
