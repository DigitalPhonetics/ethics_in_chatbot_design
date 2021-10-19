<template>
  <div class="pagelayout">
    <div class="content">
      <div class="left">
        <div v-if="has_token">
          <b-button
            variant="warning"
            @click="startDialog"
          >
            Start Dialog
          </b-button>
        </div>
        <div
          v-if="has_token"
          class="messagebox"
          ref="messagebox"
        >
          <chatmessage
            v-for="(msg, index) in messages"
            :key="index"
            :party="msg.party"
            :message="msg.message"
          />
        </div>
        <div
          v-if="has_token"
          class="input"
        >
          <input 
            ref="usermsg"
            id="usermsg"
            placeholder="Enter your message here"
            v-model="userMessage"
            @keyup.enter="sendMessage"
            style="flex:1; display:block;"
          >
          <b-button
            variant="primary"
            :disabled="!connected"
            @click="sendMessage"
          >
            Send
          </b-button>
        </div>
        <b-modal
          id="connectionalert"
          hide-footer
        >
          <template v-slot:modal-title>
            No valid connection to server
          </template>
          <div>
            Login expired (or connection problem) - please try to log in again!
          </div>
          <b-button
            @click="$router.replace('/')"
            block
            variant="danger"
          >
            Login
          </b-button>
        </b-modal>
        <b-modal
          id="dialog_complete"
          hide-footer
        >
          <template v-slot:modal-title>
            Thank you for participating!
          </template>
          <div>
            Please click the butoon below to be redirected to the survey
            <br>
          </div>
          <b-button
            @click="$router.replace('/bippidyboop')"
            block
            variant="primary"
          >
            Take Survey
          </b-button>
        </b-modal>        
      </div>
      <div class="right">
        <h2 style="text-align: center">
          Instructions
        </h2>
        <p>
          <b><br>PLEASE pay attention to the <u>sysem responses</u> and your <u>reactions/feelings</u>. You will be asked about them in the survey after the interaction.</b><br><br>
          For this dialog, assume that you are a current student in need of information about your exams this semester. To get the information you need, 
          you will chat (type) with the dialog agent on the left.
        </p>
        <p>
          Below is a list of the information you plan to tell the system and the questions you should ask. <b>Please use this information and this order when chatting  
            with the dialog system, inputting one prompt per turn. As you fulfill goals, they will be marked green. Make sure to do all 10.</b>
        </p>
        <p>
        <p>
          <b>If the chatbot's response shows it didn't understand you, try using the <u>underlined</u> words in your answer. 
            If something goes wrong, you can restart the dialog by clicking the restart dialog button.</b>
        </p>
        <!-- <h3 style="text-align: center"> Scenario </h3> -->
        <ol>
          <li v-bind:class="{ greentext: completed_goals > 0}"><b>Information:</b><br>You need some <u><b>information</b></u> about your <u><b>requirements module</b></u>. </li>
          <li v-bind:class="{ greentext: completed_goals > 1}"><b>Information:</b><br>You have to <u><b>register</b></u> for your requirements module but you don't know how.</li>
          <li v-bind:class="{ greentext: completed_goals > 2}">
            <b>Question:</b><br>Since the date has not yet been announced, you are afraid you won't have enough time to prepare for the requirements module. 
            You want to know if you can also <b><u>withdraw</u></b> from your requirements module if needed.
          </li>
          <li v-bind:class="{ greentext: completed_goals > 3}"><b>Question:</b><br>You also want to know when the current <b><u>winter semester registration period</u></b> is.</li>
          <li v-bind:class="{ greentext: completed_goals > 4}">
            <b>Question:</b><br>You just noticed that you have <b><u>missed the registration period</u></b> and don't know what to do.
          </li>
          <li v-bind:class="{ greentext: completed_goals > 5}"><b>Information:</b><br>Additionally, you have some <u><b>questions</b></u> about your <u><b>master thesis</b></u>.</li>
          <li v-bind:class="{ greentext: completed_goals > 6}"><b>Information:</b><br>You <u><b>missed enrolling</b></u> for your master thesis too.</li>
          <li v-bind:class="{ greentext: completed_goals > 7}"><b>Question:</b><br>You want to know what exactly you have to do to <u><b>register</b></u> for your master thesis.</li>
          <li v-bind:class="{ greentext: completed_goals > 8}">
            <b>Question:</b><br>You are currently also unhappy with your thesis topic so you want to know if it is also possible to <u><b>change</b></u> a 
            <u><b>thesis topic</b></u>.
          </li>
          <li>
            <b>End Session:</b><br>Once you have gotten through all of the topics, you can type <u><b>bye</b></u> to end the dialog. The dialog will only end once all 
            goals outlined here have been fulfilled.
          </li>
        </ol>
      </div>
    </div>

    <div class="footer">
      <a href="impressum.html">Impressum</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Chatmessage from './chatmessage.vue';
import { mapState } from "vuex";

export default {
    name: 'Chat',
    components: {
      chatmessage: Chatmessage,
    },
    computed: {
      
      ...mapState(["token"]),
    },
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/ws?token=" + this.token);
        this.socket.onopen = (event) => {
          this.startDialog();
        };
        this.socket.onmessage = (msg) => {
          var content = JSON.parse(msg.data)
          if (content['topic'] == 'sys_utterance') {
            this.messages.push({party: 'system', message: content['msg']});            
          }
          else if (content['topic'] == 'dialog_complete'){
              this.$bvModal.show('dialog_complete'); 
          }
          else if (content['topic'] == "num_completed_goals"){
            this.completed_goals = parseInt(content["msg"])
          }
        }

      }
      else {
        // don't connect - no token
      }
    },
    updated() {
      this.$nextTick(() => this.scrollToBottom()); // scroll to bottom of chat messages
      this.$refs.usermsg.focus();                  // focus chat message input
    },
    data() {
      return {
          socket: null,
          messages: [],
          userMessage: '',
          connected: false,
          domain: null,
          completed_goals: 0,
      } 
    },
    methods: {
        has_token: function() {
            return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
        },
        startDialog: function (domain_number) {
            if (this.has_token()) {
              this.started = true;
              this.messages = [];
              this.connected = true;
              this.socket.send(JSON.stringify({
                  topic: "start_dialog",
                  domain: this.domain,
                  access_token: this.token,
                }
              ));
            } else {
              this.$bvModal.show('connectionalert'); 
            }
        },       
        sendMessage: function (event) {
          event.preventDefault();

          if (this.has_token()) {
            console.log(this.userMessage)
            this.messages.push({party: 'user', message: this.userMessage});
            this.socket.send(JSON.stringify({
              access_token: this.token,
              topic: 'user_utterance',
              domain: this.domain,
              msg: this.userMessage,
            }));
            this.userMessage = '';
          } else {
            this.$bvModal.show('connectionalert');
          } 
        },
        scrollToBottom: function () {
          var container = this.$refs.messagebox;
          container.scrollTop = container.scrollHeight;
        },
    }
};
</script>

<style scoped>
.pagelayout {
  height: 100%;
  width: 100%;
}
.input
{
    position: absolute;
    bottom:0px;
    left:0px;
    right:0vw;
    height:5%;
    margin-bottom:0px;
    display: flex;
}
.footer {
  position:absolute;
  bottom: 0px;
  width: 100%;
  height: 3%;
  text-align: right;
  padding-right: 10px;
}

.messagebox
{
    padding: 35px;
    top: 5%;
    height: 90%;
    overflow-y: auto;
}

.content {
  width: 100%;
  height: 97%;
}
.left {
  position: absolute;
  left: 0;
  top: 0;
  width: 50%;
  height: 97%;
  padding: 1%;
}
.right {
  position: absolute;
  left: 50%;
  width: 50%;
  height: 97%;
  padding: 1%;
  overflow: auto;
}
.greentext{
  color: green;
}

</style>
