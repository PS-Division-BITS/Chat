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
            username :"rt",
            message :"",
            chat :[{'sender':'rt','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'rt','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'rt','message':'Hii Guys, this is my UI design of a chat window'},
                    {'sender':'Anupama','message':'Hii Guys, this is my UI design of a chat window'}

            ]
        }
    },
    methods:{
        
        sendMessage(){
            this.chat.push({'sender':this.username,'message':this.message});
            this.message="";
            
            
        }

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
    height: 85%;
    overflow-x: scroll;
    
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