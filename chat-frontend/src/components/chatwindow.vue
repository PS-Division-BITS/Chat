<template>
    <div id="chatwindow" class=" container-fluid m-0 p-0">
        <div class="mb-2 p-3 container-fluid" id="messagesBox">
               
            <div v-for="data in chat" :key="data.id" class="rounded m-1 p-1" id="messageInfo" :class="{'sent': username === data.sender, 'recieved' : username !== data.sender}">
               
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

              this.setupConnection()
                this.scrollBottom()
                
                this.chatSocket.onmessage = (m)=>{
                    this.messageReceived(JSON.parse(m))
                }
    },
    methods:{
        
        setupConnection()
        {
             //Establishing Connection
                try {
                        this.chatSocket.onopen = () => {
                           
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
                   
                   this.chatSocket.send(JSON.stringify({'message':this.message}))
                    console.log('Message Sent to the server');
                    this.chat.push({sender:this.username,message:this.message})
                    this.message="";
                    
                }
                catch (e)
                {
                    console.log('Error : '+e)
                }
                
            }
            
        },
        
        
        messageReceived(messageData){
                console.log(messageData)
                this.chat.push(messageData);
        },


        scrollBottom(){
            var container = this.$el.querySelector("#messagesBox"); 
            container.scrollTop = container.scrollHeight;
           
        }
    },
    updated :function() {
        this.scrollBottom()
    },
    
}
</script>

<style lang="scss">
#chatwindow {
    position: absolute;
    height:100%;
    
}

#messagesBox {
   
    position: relative;
    max-height: 80%;
    padding-bottom: 10px;
    overflow-y:scroll;
    
}

#sendBox 
{
    margin-top:10px;
    position: fixed ;
    bottom : 0px;
    height:auto;
  
    width:inherit;
}

#messageInfo{
width:80%;
}


#sender{

}

#sendBox {
input{
overflow-x: scroll;   
}
}

.recieved {
    margin-right: auto !important;
    text-align: left;

    background-color:linen;
    hr {
        margin-right: auto;
    }
}

.sent {
    margin-left: auto !important;
    text-align: right;
    background-color:lightblue;
     hr {
        margin-left: auto !important;
    }
}
</style>