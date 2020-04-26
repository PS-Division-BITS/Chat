<template>
    <div id="chatwindow" class="container-fluid m-0 p-0">
        <div class="py-3" id="onlineUsers">
            <div class="">  Online users</div>
            <span class="text-secondary">Beta</span>
            <hr class="m-0 p-0">
            
            <div class="py-3">
                <div class="border my-1 mx-2" id="user" style="height:60px;">
                    <div class="img mt-2" style="float:left">
                        <img src="@/assets/paper-plane-solid.svg" class="img img-fluid" height="40px" width="40px">
                    </div>
                    <div class="desc px-3" style="float:left">
                     <div class="text-left"> Ritik  Taneja</div>
                       <hr  class="m-0 p-0">
                      <div class="text-left text-secondary"> Status Status Status Status Status</div>
                        </div>
                </div>

            </div>



        </div>
       <div class="container-fluid m-0 p-0" id="wrapper">
            <div class=" p-0 px-1" id="messagesBox">
             
                <div v-for="data in chat" :key="data.id" class=" container-fluid " >
                 
                    <div id="messageInfo" :class="{'notification': data.type === 'notification','sent': username === data.sender, 'recieved' : (username !== data.sender && data.type !== 'notification')}">   
                       
                        <span id="sender"> {{data.sender}} 
                            <span v-if="data.verified" class="verified"></span>
                                <span v-if="data.type !== 'notification'" class="text-secondary mx-2" :style="data.sender === username ? 'float:left;':'float:right'">00:00</span>
                         </span>
                        <hr style="width:10%" class="m-0 p-0">
                        <span> {{data.message}}</span>

                    </div>
                   
                 
                </div>
            
            </div>


            <div id="sendBox" class="input-group d-flex container-fluid align-content-end m-0 py-2  ">
                   
                    <input id="message" type="text" v-model="message" @keyup.enter="sendMessage()" class="form-control" placeholder="Enter Text Message ...">
                    <span class="input-group-btn">
                        <button class="btn btn-light container" type="button"  @click="sendMessage()">
                            <img class="img img-fluid" src="@/assets/paper-plane-solid.svg"/>
                        </button>
                     
                    
            </span>
              
    
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: function(){
        return {
            username : this.$store.state.user.username,
            token : this.$store.state.user.key,
            message :"",
            chat :[{'type':'notification','message':'Hii Guys, Welcome to chat.bpgc! Feel free to test this development version and report any issues directly at our git repo!'},
            {'sender':'admin','verified':true,'message':'Hii Guys,Welcome to BITS Goa\'s campus wide chat room!  '},
            {'type':'notification','message':'Abc just joined the chat!'}
                    

            ],
            chatSocket: new WebSocket(this.$store.getters.socketURL),
            chatRoom : this.$store.state.currentChatRoom
        }
    },
    mounted: function(){

                this.setupConnection()
                this.scrollBottom()
                
                this.chatSocket.onmessage = (m)=>{
                   
                    this.messageReceived(JSON.parse(m.data))
                }
    },
    methods:{
        
        setupConnection()
        {
             //Establishing Connection
                try {
                        this.chatSocket.onopen = () => {
                           
                         //   this.chatSocket.send(JSON.stringify({'message':'hello'}))
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
           
         // document.getElementById("message").blur();
            if(this.message !== "")
            {
                try {
                   
                   if(this.chatSocket.readyState == this.chatSocket.OPEN)
                   {    this.chatSocket.send(JSON.stringify({'token':this.token,'message':this.message}))
                        console.log('Message Sent to the server');
                   }
                   else {
                       console.log('Socket closed, please refresh!')
                        this.chat.push({sender:this.username,message:this.message}) //dev
                   }

                   
                    this.message="";
                    
                }
                catch (e)
                {
                    console.log('Error : '+e)
                }
                
            }
            
        },
        
        
        messageReceived(messageData){
                
             
                console.log("Web socket response : "+messageData.sender)
                messageData.sender = messageData.sender['username'];
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
    height:100% !important;
    @media only screen and (min-width: 992px)
    {
    width:100%!important;

    left: 0px;
    
    display: inline-flex;
        
    }
}

#onlineUsers{
    display:none;
   
    width:30%;
     font-family: 'Comic Neue', cursive;
    @media only screen and(min-width: 992px)
    {
        background-color:rgba(234, 240, 250, 0.8);
        display: block;
    }

    #user{
        background-color:rgba(234, 240, 250, 0.9);
    }
 
}

#wrapper {

   
  
    
    @media only screen  and (min-width: 992px){
        width:70%;
       
    }
}

#messagesBox {
   
 
    max-height: 84%;
    
  
    height:auto;
    position:absolute;  
    overflow-y:scroll !important;
  
    padding-bottom: 30px !important;
    @media only screen and (min-width: 992px) {
        max-height:80%;
    padding:0 5% 3% 5% !important ;
    margin:0px !important;
    background-color:rgba(234, 240, 250, 0.2);
    position: relative;
    min-height: 80%;
    min-width: 100%;
     
    
    }
    
}
#messagesBox::before{
    padding-bottom:12px ;
}



#sendBox 
{
      
 
    position: fixed;
    bottom: 0px;
    height:auto;
    z-index: 2;
   
    img {
        height: 23px;
        width: 20px;
       
    }
    @media only screen and (min-width: 992px) {
    
    display: block;
    
    position:relative;
    align-self: flex-end !important;
    margin:0px;
    background-color:rgba(234, 240, 250, 0.6);
    
    }
    
}

#sendBox {
input{
overflow-x: scroll;   
}
}

#messageInfo{

font-size: 80%;

max-width: 80%;
padding: 3px 4px 3px 4px ;
margin-top: 10px;
margin-bottom: 10px;

        @media  only screen and (min-width: 992px) {
            max-width: 60%;
             padding:2px 5px 1px 5px;

        }
}


#sender {

        font-size:90%;
        width:auto;
        padding:8px 2px 3px 2px;
         font-family: 'Comic Neue', cursive;
}

.recieved {
    margin-right: auto !important;
    text-align: left;   
   
    margin-left:0px;
   
    border-radius: 15px 18px 18px 5px;
    z-index: 1;
      box-shadow:darkgray 2px 3px;
    background-color:rgba(83, 147, 241, 0.2);
    hr {
        margin-right: auto;
        
    }
}

.sent {
    margin-left: auto !important;
    text-align: right;
 

    z-index: 1;
    box-shadow:darkgray 2px 3px;
     border-radius: 18px 0px 5px 5px;
    background-color:rgba(234, 240, 250, 0.4);
     hr {
        margin-left: auto !important;
    }
}

.notification{
    text-align: center;
    font-style: italic;
    font-size: 80%;
    margin:auto !important;
    hr {
        display: none;
    }
}

.verified{
  display:inline-block;

  &:after{
    /*Add another block-level blank space*/
    content: '';
    display: block;
 
    /*Make it a small rectangle so the border will create an L-shape*/
    width: 6px;
    height: 12px;
 
    /*Add a white border on the bottom and left, creating that 'L' */
    border: solid black;
    border-width: 0 2px 2px 0;
 
    /*Rotate the L 45 degrees to turn it into a checkmark*/
    transform: rotate(45deg);
  }

}
::-webkit-scrollbar {
   width: 6px;
  height: 6px;
  overflow-x: auto;
}
::-webkit-scrollbar-thumb
{
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
 background-color:rgba(83, 147, 241, 0.2);
  overflow-x: auto;
}


/* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {} 

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {} 

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {} 

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {



} 

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {}


</style>