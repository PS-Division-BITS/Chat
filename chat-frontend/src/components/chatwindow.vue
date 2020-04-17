<template>
    <div id="chatwindow" class=" container-fluid m-0 p-0">
        <div class="mb-2 p-3 container-fluid" id="messagesBox">
               
            <div v-for="data in chat" :key="data.id" class="rounded p-1" id="messageInfo" :class="{'sent': username === data.sender, 'recieved' : username !== data.sender}">
               
                    <code id="sender"> {{data.sender}} </code> <hr style="width:10%" class="m-0 p-0">
                    <span> {{data.message}}</span>
               
            </div>
          
        </div>


        <div id="sendBox" class="container-fluid input-group d-flex align-content-end m-0 p-0  ">
            
                <input type="text" v-model="message" @keyup.enter="sendMessage()" class="form-control" placeholder="Enter Text Message ...">
                <span class="input-group-btn">
                    <button class="btn btn-light" type="submit"  @click="sendMessage()">
                          >
                    </button>
                  
  </span>
   
        </div>
    </div>
</template>

<script>
export default {
    data: function(){
        return {
            username : this.$store.state.user.username,
            message :"",
            chat :[{'sender':'testusers','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'rt','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'rt','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'}

            ],
            chatSocket: new WebSocket(this.$store.getters.socketURL),
            chatRoom : this.$store.state.currentChatRoom
        }
    },
    mounted: function(){

<<<<<<< HEAD
               this.setupConnection()
               
=======
                this.chatSocket.onmessage = function(e){ console.log(e.data); };
                this.chatSocket.onopen = () => this.chatSocket.send(JSON.stringify({'message': 'hello'}));
                this.chatSocket.onmessage = (m) => {
                this.onMessageReceive(JSON.parse(m))
            }
            //  this.sockets.on('recieveMessage', eventData => this.onMessageReceive(eventData));            

    },

    computed : {
>>>>>>> 5bd4cb68fae1cb53d6333ed404849e949e3d3894

    },
    methods:{
        
        setupConnection()
        {
             //Establishing Connection
                try {
                        this.chatSocket.onopen = () => {
                            console.log('hello');
                            this.chatSocket.send(JSON.stringify({'message':'hello'}))
                        };
                        console.log('Connection Established!')
                }
                catch(e){
                        console.log('Error Connecting to chat room with id : '+this.chatRoom.id)
                }
                finally {
                        console.log('finally..')
                }
        },

        sendMessage(){
           
          
            if(this.message !== "")
            {
                try {
                   
                   this.chatSocket.send(JSON.stringify(this.message))
                    console.log('Message Sent to the server');
                }
                catch (e)
                {
                    console.log('Error : '+e)
                }
                
            }
            this.message="";
        },
        onMessageReceive(messageData){
                
                this.chat.push(messageData);
        },

    },
    updated :function() {
        var container = this.$el.querySelector("#messagesBox");
            container.scrollTop = container.clientHeight;
    },
    
}
</script>

<style lang="scss">
#chatwindow {
    position: absolute;
    height:100%;
}

#messagesBox {
   
    position: absolute;
    max-height: 85%;
    overflow-x:hidden;
    
}

#sendBox 
{
    position: fixed ;
    bottom : 0px;
    height:auto;
    width:inherit;
}

#messageInfo{
width:80%;
}


#sender{
font-size : 12px;

}

#sendBox {
input{
overflow-x: scroll;   
}
}

.recieved {
    margin-right: auto !important;
    text-align: left;
    hr {
        margin-right: auto;
    }
}

.sent {
    margin-left: auto !important;
    text-align: right;

     hr {
        margin-left: auto !important;
    }
}
</style>