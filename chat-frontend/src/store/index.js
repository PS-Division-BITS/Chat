import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const socketBase = "ws://127.0.0.1:8000/ws/chat/";

export default new Vuex.Store({
  state: {
    user : {
      username : 'testuser',
      ip : '127.0.0.1',
      key :'abcbabcbsb',
    },
   
    currentChatRoom: {
        id:"1/",
        totalUsers:999,
        onlineUsers:123,
    },
    
    
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
