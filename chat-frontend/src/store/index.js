import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const socketBase = "ws://127.0.0.1:8000/ws/chat/";
const AUTHBASEURL = "http://localhost:8000/chat/auth/";

export default new Vuex.Store({
  state: {
    user : {
      username : null,
    },
   
    currentChatRoom: {
        id:"1/",
        totalUsers:"",
        onlineUsers:"",
    },

   AUTHBASEURL:AUTHBASEURL,
    
    
  },
  getters :{
    socketURL: state => {
      return socketBase+state.currentChatRoom.id;
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
