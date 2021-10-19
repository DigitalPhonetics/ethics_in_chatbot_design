<template>
  <fragment>
    <div id="wrapper">
      <br><br>
      <h1>Data Collection Policy</h1>
      <b><u>Please consider this information carefully before deciding whether to accept this task.</u></b>
      <br><br>
      <b>TITLE OF RESEARCH:</b> On the Perception and Ethical Considerations of Affective Language in Text-Based Conversational Agents
      <br><br>
      <b>PURPOSE OF RESEARCH:</b> To examine how people perceive affective language in text-based conversational agents and what ethical implications this might have.
      <br><br>
      <b>WHAT YOU WILL DO:</b> You will pretend you are student in need of guidence about exam regulations. Based on the scenario laid out on the next page, you will 
      conduct a dialog with our chatbot to get the information you need.
      <br><br>
      <b>TIME REQUIRED:</b> Participation will take approximately 15 minutes.
      <br><br>
      <b>RISKS:</b> There are no anticipated risks associated with participating in this study. The effects of participating should be comparable to those you would 
      experience from viewing a computer monitor for 15 minutes and using a mouse and keyboard.
      <br><br>
      <b>LIMITATIONS:</b> This task is suitable for all people who can read from and input text to a computer.
      <br><br>
      <b>CONFIDENTIALITY:</b> Your participation in this study will remain confidential. Your responses will be assigned a code number. You will NOT be asked to provide 
      your name. You will be asked to provide your age and gender and the country you have spent most time in. Throughout the experiment, we may collect data such 
      as your textual input, and your feedback in form of a questionnaire. The records of this study will be kept private. In any sort of report we make public we 
      will not include any information that will make it possible to identify you without your explicit consent. Research records will be kept in a locked file; only 
      the researchers will have access to the records.
      <br><br>
      <b>PARTICIPATION AND WITHDRAWAL:</b> Your participation in this study is voluntarily, and you may withdraw at any time.
      <br><br>
      <b>DATA REGULATION:</b> Your data will be processed for the following purposes:
      <ul>
        <li>Analysis of the respondents' evaluations of the dialog and their experience</li>
        <li>Analysis of potential influencing factors for individual behavior of the participants in the interaction with the dialog system</li>
        <li>Scientific publication based on the results of the above analyses</li>
      </ul>
      Your data will be processed on the basis of Article 6 paragraph 1 subparagraph 1 letter a GDPR. Data, which is related to your person, will be deleted by 
      30.06.2021 at the latest.
      You are entitled to the following rights (for details see  <a href="https://www.uni-augsburg.de/de/impressum/datenschutz/#ix-rechte-der-betroffenen-person6393">here</a>)
      <ul>
        <li>You have the right to receive information about the data stored about your person.</li>
        <li>Should incorrect personal data be processed, you have the right to correct it.</li>
        <li>Under certain conditions, you can demand the deletion or restriction of the processing as well as object to the processing.</li>
        <li>In general, you have a right to data transferability.</li>
        <li>Furthermore, you have the right of appeal to the Baden-Württemberg State Commissioner for Data Protection.</li>
      </ul>
      You can revoke your consent for the future at any time. The legality of the data processing carried out on the basis of the consent until revocation is not 
      affected by this.
      <br><br>
      <b>COMPENSATION</b>: Upon completion of this task, you will receive a code to enter on the Amazon Mechanical Turk task page.
      <br><br>
      <b>CONTACT:</b> This study is conducted by researchers at the University of Stuttgart. If you have any questions or concerns about 
      this study, please contact Michael Neumann neumanml@ims.uni-stuttgart.de or Lindsey Vanderlyn, vanderly@ims.uni-stuttgart.de       


      <br><br>

      <div id="navigation_buttons">
        <div id="next_button">
          <b-button
            variant="success"
            @click="next_page"
          >
            Agree and Continue
          </b-button>              
        </div>
      </div>
      <br><br> 
      <div class="header">
        <a href="impressum.html">Impressum</a>
      </div>         
    </div>
  </fragment>
</template>

<style scoped>

#next_button {
    float: right;
}

#wrapper{
    width: 80%;
    height: 97%;
    margin: auto;
    overflow: auto;
}
.header {
  position:absolute;
  top: 0px;
  width: 80%;
  height: 3%;
  text-align: right;
  padding-right: 10px;
}

</style>

<script>
import { mapState } from "vuex";

export default {
    name: 'DataAgreement',
    computed: {
      
      ...mapState(["token"]),
    },
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/ws?token=" + this.token);
        this.socket.onopen = (event) => {
          //this.startDialog();
        };
      };
    },    
    methods:{
        has_token: function() {
            return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
        },        
        next_page(){
        if (this.has_token()){
            this.socket.send(JSON.stringify({
                topic: "user_consented",
                access_token: this.token,
            }));
            this.$router.push({
                name: 'Chat',
            });
            // this.$router.go()

          };
        },
    },
}

</script>