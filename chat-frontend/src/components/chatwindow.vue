<template>
    <div id="chatwindow" class="container-fluid m-0 p-0 ">
         
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
            <div class=" p-0 pb-5 px-1" id="messagesBox">
             
                <div v-for="data in chat" :key="data.id" class="m-0 p-0 container-fluid " >
                 
                        <div id="wrapperInside" class=" container-fluid py-1 m-0 p-0 pr-1">
                        
                                <div id="messageInfo"  :class="{'notification': data.type === 'notification','sent': data.sender&& username === data.sender, 'recieved' : (data.sender && username !== data.sender) }">   
                                
                                    <span id="sender">
                                        {{data.sender}}
                                            
                                            <!-- verified symbol -->
                                            <span v-if="data.verified" class="verified">

                                            </span>
                                                <!-- timespan display -->
                                            <span v-if="data.type !== 'notification'" class="text-secondary mx-2" :style="data.sender === username ? 'float:left;':'float:right'">{{data.time}}
                                                
                                            </span>
                                        
                                    </span>
                                    <hr style="width:10%" class="m-0 p-0">
                                    <div class="container-fluid m-0 p-0">
                                    <span id="messageValue" class="w-100">
                                        {{data.message}}
                                    </span>
                                    </div>

                                </div>
                        </div>
                 
                </div>
            
            </div>


            <div id="sendBox" @click="scrollBottom(true)"  class="input-group d-flex container-fluid align-content-end m-0 py-2  ">
                   
                    <input id="message" maxlength="100"  type="text" v-model="message" @keyup.enter="sendMessage()" class="form-control" placeholder="Enter Text Message ...">
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
                 {'sender':'admin','verified':true,'message':'777777777777777777777777777777777777777777777777777'},
                {'sender':'ritiktaneja','verified':true,'message':'!  '},
                 {'type':'notification','message':'! haina mast '},
                 {'sender':'ritiktaneja','verified':true,'message':'!  '},
                 {'sender':"ritiktaneja",'verified':true,'message':'Hii Guys,Welcome to BITS Goa\'s campus wide chat room!  '},
                  {'sender':'ritiktaneja','verified':true,'message':'Hii Guys,Welcome to BITS Goa\'s campus wide chat room!  '},
                    {'sender':'admin','verified':true,'message':'H  ii Guys,Welcome to BITS Goa\'s campus wide chat room!  '},
              {'sender':'admin','verified':true,'message':'Hii Guys,Welcome to BITS Goa\'s campus wide chat room!  '},
            
                    

            ],
            chatSocket: WebSocket,
            chatRoom : this.$store.state.currentChatRoom
        }
    },
    mounted: function(){

                this.loadChat()
                this.setupConnection()
                this.scrollBottom(false)
                
                this.chatSocket.onmessage = (m)=>{
                   
                    this.messageReceived(JSON.parse(m.data))
                }
                
                this.chatSocket.onclose = function() {
                    this.chatSocket=null;
                    console.log('retrying connection...')
                    setTimeout(this.setupConnection(),5000)
                }
    },
    methods:{
        loadChat()
        {
             this.$axios({
                method : 'get',
                url : this.$store.state.URLS.general.loadChat+'?uri='+this.$store.state.currentChatRoom.uri
                
            })
            .then(response=>{
                    response = response.data; 
                    var r;  
                    for (r in response)
                    response[r].time = response[r].timestamp.substr(12,5)
                    this.chat = response;
                    console.log(response,"preloaded chat")
            })
            .catch(error=>{
                console.log(error)
              
            })  
        },

        setupConnection()
        {               
                        this.chatSocket=null;
                       this.chatSocket= new WebSocket(this.$store.getters.socketURL)
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
                       // this.chat.push({sender:this.username,message:this.message}) //dev
                   }

                   
                    this.message="";

                    
                }
                catch (e)
                {
                    console.log('Error : '+e)
                }
                
            }

            this.scrollBottom(true);
           // document.getElementById("message").blur();
            
        },
        
        
        messageReceived(messageData){
                
                var container = this.$el.querySelector("#messagesBox"); 
                if(this.username !== messageData.sender || (container.scrollHeight) - container.scrollTop  > 600 )
                {   
                
                var audio = new Audio(require('@/assets/new message.mp3'));
                document.title = "New Message @ "+messageData.sender
                 audio.play();
                  setTimeout (function(){ document.title=this.$store.state.currentChatRoom.name;},5000)
                }
                // if (promise !== undefined) {
                //     promise.then(function() {
                        
                //         // Autoplay started!
                //     }).catch(error => {
                //         console.log(error+"Audio error")
                //         // Autoplay was prevented.
                //         // Show a "Play" button so that user can start playback.
                //     });
                // }
                
                messageData.time = messageData.timestamp.substr(12,5)
                this.chat.push(messageData);
                
        },


         scrollBottom :function (b) {
            
           
           
            var container = this.$el.querySelector("#messagesBox"); 
             var x =container.scrollHeight - container.scrollTop -container.clientHeight
            if(x<250 || b)
                 container.scrollTop =  container.scrollHeight + container.clientHeight   ;
           

          //  container.scrollIntoView(false);
            //console.log('Scrolled to : '+container.scrollHeight)
           
        }
    },
    updated : function() {
        
        this.scrollBottom(false)
    }
    
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
    width: 100% !important;
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

#sendBox {
      
 
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


#sender {

        font-size:90%;
        width:auto;
        padding:8px 2px 3px 2px;
         font-family: 'Comic Neue', cursive;
}
#messageValue {
    word-wrap: break-word;
    display: block;
}


#wrapperInside {
    overflow: hidden;
    margin:0 !important;
    padding-right: 4px;
    
    
}


#messageInfo{

font-size: 80%;
z-index: 1;
max-width: 60%;

padding: 3px 4px 3px 4px ;


        @media  only screen and (min-width: 992px) {
            max-width: 60%;
             padding:2px 5px 1px 5px;

        }
}

.recieved {
    margin-right: auto !important;
    text-align: left;   
    float:left;
    
    margin-left:0px;
    border-radius: 15px 18px 18px 5px;
      box-shadow:darkgray 2px 3px;
    background-color:rgba(83, 147, 241, 0.2);
    hr {
        margin-right: auto;
        
    }
}

.sent {
   
    text-align: right;
    float:right;
    margin-left: auto;
   
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