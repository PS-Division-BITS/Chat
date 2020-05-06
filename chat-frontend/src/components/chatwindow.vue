<template>
    <div id="chatwindow"  class="container-fluid m-0 p-0 ">
         
       <STATS
       
       :userList="this.userList"
       :username="this.username"
        id="stats"
        @emitUsername="onSenderClick"
       />
         
       
       <div class="container-fluid m-0 p-0" id="wrapper">
           
           <sidebar-menu id="sidebar" style="z-index:2; top:20%!important; text-align:center !important;" :rtl="true" :collapsed="collapseUserDiv" :showOneChild="true" :width="'60%'" :widthCollapsed="'45px'" :relative="true" :hideToggle="false" :theme="'white-theme'" :menu="menu" >

              
                  <span slot="toggle-icon">
                        <font-awesome-icon  v-if="collapseUserDiv" :icon="['fas', 'user-secret']" />
                       
                  </span>

            </sidebar-menu>
        
            <div class=" p-0 pb-5 px-1" id="messagesBox">
             
                <div v-for="data in chat" :key="data.id" class="m-0 p-0 container-fluid " >
                 
                        <div id="wrapperInside" class=" container-fluid py-1 m-0 p-0 pr-1">
                        
                                <div id="messageInfo"  class="m-0 align-content-center" :class="{'notification': data.msg_type === 'notification','sent': data.sender&& username === data.sender, 'recieved' : (data.sender && username !== data.sender), 'ghost' : data.sender === 'Ghost' }">   
                                
                                    <span  v-if="data.sender!==username" id="sender">
                                        <span @click="onSenderClick(data.sender)" >{{data.sender}}
                                             <span v-if="data.verified" class="pl-2 verified">
                                            </span>
                                        </span>   
                                            <span v-if="data.msg_type !== 'notification'" class="text-secondary mx-2" :style="data.sender === username ? 'float:left;':'float:right'">{{data.time}}   
                                            </span>
                                    </span>
                                    <span v-else>
                                              <span v-if="data.msg_type !== 'notification'" class="text-secondary mx-2" :style="'float:left'">{{data.time}}   
                                            </span> <br>
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


            <div id="sendBox" @click="scrollBottom(true)"  class="input-group d-flex container-fluid align-content-end m-0 p-0   ">
                      <div class="input-group">
                     <span class="input-group-prepend">
                        <button @click="muted=!muted" class="btn btn-light container" type="button" >
                          <font-awesome-icon v-if="!muted"  :icon="['fas', 'volume-up']" />
                           <font-awesome-icon v-if="muted" :icon="['fas', 'volume-mute']" />
                        </button>
                      </span>
                   
                    <input ref="message" id="message" maxlength="100"  type="text" v-model="message" @keyup.enter="sendMessage()" class="form-control"  placeholder="Enter Text Message ...">
                    <span class="input-group-append">
                        <button class="btn btn-light container" type="button"  @click="sendMessage()">
                            <img class="img img-fluid" src="@/assets/paper-plane-solid.svg"/>
                        </button>
                      </span>
                     </div>
            </div>

        </div>
      
    </div>
</template>

<script>
import STATS from '../components/stats'
export default {
    components:{
       STATS
    },
    data: function(){
        return {
            username : this.$store.state.user.username,
            token : this.$store.state.user.key,
            message :"",
            chat :[],
                       
             menu: [
                    {
                        header: true,
                        title: 'Online Users',
                        hiddenOnCollapse: true
                    },

                    ],
            chatSocket: WebSocket,
            chatRoom : this.$store.state.currentChatRoom,
            muted:false,
            collapseUserDiv:true,
            userList:[],
        }
    },
    mounted: function(){

                this.loadChat()
                this.setupConnection()
                
                this.$refs.message.focus();
             
               
                this.chatSocket.onmessage = (m)=>{
                    
                    this.messageReceived(JSON.parse(m.data))
                }
                var ref=this;
                this.chatSocket.onclose = function() {
                    this.chatSocket=null;
                    console.log('retrying connection...')
                    setTimeout(ref.setupConnection(),5000)
                }

                if(localStorage.muted)
                this.muted=JSON.parse(localStorage.muted)

              
             
              
                
              
    },
    methods:{
        onSenderClick(sender){
            if(sender !== 'Ghost')
            this.message="@"+sender+" ";
             this.$refs.message.focus();
            
        },

        loadChat()
        {   
            var self =this;
           let loader= this.$loading.show()
             this.$axios({
                method : 'get',
                url : this.$store.state.URLS.general.loadChat+'?uri='+this.$store.state.currentChatRoom.uri
                
            })
            .then(response=>{
                    response = response.data; 
                    var r;  
                    for (r in response)
                    response[r].time = response[r].timestamp.substr(11,5)
                    this.chat = response;
                  
                  
                   
            })
            .then(function(){
              
                 self.scrollBottom(true);
                 loader.hide()
               
            })
            .catch(error=>{
                console.log(error)
                loader.hide()
              
            }) 
           

           
            
        },

        setupConnection()
        {               
                        this.chatSocket=null;
                       this.chatSocket= new WebSocket(this.$store.getters.socketURL)
             //Establishing Connection
                try {
                        this.chatSocket.onopen = () => {
                           this.chatSocket.send(JSON.stringify({'token':this.token,'command':'join'}))
                        };

                        console.log('Connection Established! with room id'+this.chatRoom.uri)
                        
                         
    
                }
                catch(e){
                        console.log('Error Connecting to chat room with id : '+this.chatRoom.id+' with error '+e)
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
                   {  
                         this.chatSocket.send(JSON.stringify({'token':this.token,'message':this.message,'command':'send'}))
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
               
               if((messageData.sender && this.username !== messageData.sender) || (container.scrollHeight) - container.scrollTop  > 600 )
                {   
                
                var audio = new Audio(require('@/assets/new message.mp3'));
                document.title = "New Message @ "+messageData.sender
                if(this.muted===false)
                {
                   
                 audio.play();
                 }// setTimeout (function(){ document.title=this.$store.state.currentChatRoom.name;},5000)
                }
                
                if(messageData.timestamp)
                messageData.time = messageData.timestamp.substr(12,5)
                
                if(messageData.msg_type==='notification' || messageData.msg_type==='message')
                this.chat.push(messageData);
                
                if(messageData.msg_type==='list')
                {
                   
                this.userList=messageData.userList
                  var ref = this;
                this.userList.forEach(function(u){
                        u.title=u.username;
                       ref.menu.push(u)
                      
                  })
                }
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
    },
   watch : {
       
       muted(){
           localStorage.muted=this.muted;
       },
     
   }
    
}
</script>

<style lang="scss">
.v-sidebar-menu{
    position:fixed!important;
    top:10% !important;
    .vsm--toggle-btn {
         background-color:rgba(120, 209, 210,.4)!important;
         border:none !important;

    }
}

.v-sidebar-menu.vsm_collapsed {
    height:10px !important;

}

.v-sidebar-menu.vsm_expanded {
    height:40% !important;
 
}
.v-sidebar-menu{
     background-color:rgba(120, 209, 210,.2)!important;

}



#chatwindow {
    position: absolute;
    height:100% !important;
    @media only screen and (min-width: 768px)
    {
        
  
    width:100%!important;

    left: 0px;
    
    display: inline-flex;
        
    #sidebar{
        display: none !important;
    }    
    }
}

#stats {
    display:none;
    width: 30%!important;
     @media only screen and(min-width: 768px)
    {  
        background-color:rgba(234, 240, 250, 0.8);
        display: block;
    }
}


#wrapper {

    
    @media only screen  and (min-width: 992px){
      
       
    }
}

#messagesBox {
   
 
    max-height: 84%;
    height:auto;
    position: absolute;
    overflow-x:scroll!important;
    overflow-y:scroll !important;
    width: 100% !important;
    
    @media only screen and (min-width: 768px) {
    height:auto;
    padding:0 5% 5% 5% !important ;
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
    
    position:fixed;
    width:inherit;
    bottom:0;
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
min-width:30%;
padding: 3px 4px 3px 4px ;

#messageValue{
    font-size:110%;
}

        @media  only screen and (min-width: 1000px) {
            max-width: 60%;
            min-width: 10%;
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
      background-color: rgba(154,183,211,.6);
   // background-color:rgba(83, 147, 241, 0.2);
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
.ghost {
    background:#d3d3d3;
  
    font-style: italic;
    
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