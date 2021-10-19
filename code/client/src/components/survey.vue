<template>
  <div class="container">
    <div class="header">
      <a href="impressum.html">Impressum</a>
    </div>      
    <b-form @submit="onSubmit" v-if="active">
      <h1 style="text-align: center">
        Post Dialog Survey
      </h1>
      <p>
        <br><b><i>Please read and answer all of the questions below. Once all questions have been answered, you may hit submit to generate your completion code for 
          Mechanical Turk.</i></b>
      </p>
      <h2 style="text-align: center">
        Demographic Information
      </h2>

      <h5>Please indicate the gender you most identify with.</h5>
      <b-form-group style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom:2%">
        <b-form-radio
          v-model="form.dem_gender_selected"
          name="dem_gender"
          value="male"
          required
        >
          Male
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_gender_selected"
          name="dem_gender"
          value="female"
          required
        >
          Female
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_gender_selected"
          name="dem_gender"
          value="other"
          required
        >
          Other
        </b-form-radio>
      </b-form-group>   

      <h5>Please indicate your age:</h5>
      <b-form-group style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom:2%">
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="20-"
          required
        >
          Less than 20
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="21-30"
          required
        >
          21-30
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="31-40"
          required
        >
          31-40
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="41-50"
          required
        >
          41-50
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="51-60"
          required
        >
          51-60
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="61-40"
          required
        >
          61-40
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="71-40"
          required
        >
          71-40
        </b-form-radio>
        <b-form-radio
          v-model="form.dem_age_selected"
          name="dem_age"
          value="81+"
          required
        >
          More than 81
        </b-form-radio>                             
      </b-form-group> 

      <h5>Please indicate which country you have lived in the longest:</h5>
      <b-form-group
        label-for="country_input"
      >
        <b-form-input
          id="country_input"
          v-model="form.dem_country"
          required
          placeholder="Enter country"
        />
      </b-form-group>
      
      <h5>Please indicate your native language(s):</h5>
      <b-form-group
        label-for="language_input"
      >
        <b-form-input
          id="language_input"
          v-model="form.dem_native_language"
          required
          placeholder="Enter language(s)"
        />
      </b-form-group>           


      <h2 style="text-align: center">
        Survey Questions
      </h2>
      <h3>1. Impressions</h3>
      <h5>1.1 Please rate your impression of the chatbot's <b>HUMANNESS</b> on the following scale:</h5>
      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Fake
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.fake_natural_selected"
                name="fake_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.fake_natural_selected"
                name="fake_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.fake_natural_selected"
                name="fake_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.fake_natural_selected"
                name="fake_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.fake_natural_selected"
                name="fake_natural"
                required
              />
            </td>
            <th scope="row">
              Natural
            </th>
          </tr>
          <tr>
            <th scope="row">
              Machine-like
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.machinelike_humanlike_selected"
                name="machinelike_humanlike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.machinelike_humanlike_selected"
                name="machinelike_humanlike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.machinelike_humanlike_selected"
                name="machinelike_humanlike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.machinelike_humanlike_selected"
                name="machinelike_humanlike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.machinelike_humanlike_selected"
                name="machinelike_humanlike"
                required
              />
            </td>
            <th scope="row">
              Human-like
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unconscious
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unconscious_conscious_selected"
                name="unconscious_conscious"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unconscious_conscious_selected"
                name="unconscious_conscious"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unconscious_conscious_selected"
                name="unconscious_conscious"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unconscious_conscious_selected"
                name="unconscious_conscious"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unconscious_conscious_selected"
                name="unconscious_conscious"
                required
              />
            </td>
            <th scope="row">
              Conscious
            </th>
          </tr>
          <tr>
            <th scope="row">
              Artificial
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.artificial_lifelike_selected"
                name="artificial_lifelike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.artificial_lifelike_selected"
                name="artificial_lifelike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.artificial_lifelike_selected"
                name="artificial_lifelike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.artificial_lifelike_selected"
                name="artificial_lifelike"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.artificial_lifelike_selected"
                name="artificial_lifelike"
                required
              />
            </td>
            <th scope="row">
              Lifelike
            </th>
          </tr>        
        </tbody>
      </table>

      <h5>1.2 Please rate your impression of the chatbot's <b>LIKABILITY</b> on the following scale:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Dislike
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.dislike_like_selected"
                name="dislike_like"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.dislike_like_selected"
                name="dislike_like"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.dislike_like_selected"
                name="dislike_like"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.dislike_like_selected"
                name="dislike_like"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.dislike_like_selected"
                name="dislike_like"
                required
              />
            </td>
            <th scope="row">
              Like
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unfriendly
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unfriendly_friendly_selected"
                name="unfriendly_friendly"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unfriendly_friendly_selected"
                name="unfriendly_friendly"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unfriendly_friendly_selected"
                name="unfriendly_friendly"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unfriendly_friendly_selected"
                name="unfriendly_friendly"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unfriendly_friendly_selected"
                name="unfriendly_friendly"
                required
              />
            </td>
            <th scope="row">
              Friendly
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unkind
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unkind_kind_selected"
                name="unkind_kind"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unkind_kind_selected"
                name="unkind_kind"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unkind_kind_selected"
                name="unkind_kind"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unkind_kind_selected"
                name="unkind_kind"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unkind_kind_selected"
                name="unkind_kind"
                required
              />
            </td>
            <th scope="row">
              Kind
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unpleasant
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unpleasant_pleasant_selected"
                name="unpleasant_pleasant"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unpleasant_pleasant_selected"
                name="unpleasant_pleasant"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unpleasant_pleasant_selected"
                name="unpleasant_pleasant"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unpleasant_pleasant_selected"
                name="unpleasant_pleasant"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unpleasant_pleasant_selected"
                name="unpleasant_pleasant"
                required
              />
            </td>
            <th scope="row">
              Pleasant
            </th>
          </tr>
          <tr>
            <th scope="row">
              Awful
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.awful_nice_selected"
                name="awful_nice"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.awful_nice_selected"
                name="awful_nice"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.awful_nice_selected"
                name="awful_nice"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.awful_nice_selected"
                name="awful_nice"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.awful_nice_selected"
                name="awful_nice"
                required
              />
            </td>
            <th scope="row">
              Nice
            </th>
          </tr>        
        </tbody>
      </table>

      <h5>1.3 Please rate your impression of the chatbot's <b>INTELLIGENCE</b> on the following scale:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Incompetent
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.incompetent_competent_selected"
                name="incompetent_competent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.incompetent_competent_selected"
                name="incompetent_competent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.incompetent_competent_selected"
                name="incompetent_competent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.incompetent_competent_selected"
                name="incompetent_competent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.incompetent_competent_selected"
                name="incompetent_competent"
                required
              />
            </td>
            <th scope="row">
              Competent
            </th>
          </tr>
          <tr>
            <th scope="row">
              Ignorant
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.ignorant_knowledegeable_selected"
                name="ignorant_knowledegeable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.ignorant_knowledegeable_selected"
                name="ignorant_knowledegeable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.ignorant_knowledegeable_selected"
                name="ignorant_knowledegeable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.ignorant_knowledegeable_selected"
                name="ignorant_knowledegeable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.ignorant_knowledegeable_selected"
                name="ignorant_knowledegeable"
                required
              />
            </td>
            <th scope="row">
              Knowledgeable
            </th>
          </tr>
          <tr>
            <th scope="row">
              Irresponsible
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.irresponsible_responsible_selected"
                name="irresponsible_responsible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.irresponsible_responsible_selected"
                name="irresponsible_responsible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.irresponsible_responsible_selected"
                name="irresponsible_responsible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.irresponsible_responsible_selected"
                name="irresponsible_responsible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.irresponsible_responsible_selected"
                name="irresponsible_responsible"
                required
              />
            </td>
            <th scope="row">
              Responsible
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unintelligent
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unintelligent_intelligent_selected"
                name="unintelligent_intelligent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unintelligent_intelligent_selected"
                name="unintelligent_intelligent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unintelligent_intelligent_selected"
                name="unintelligent_intelligent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unintelligent_intelligent_selected"
                name="unintelligent_intelligent"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unintelligent_intelligent_selected"
                name="unintelligent_intelligent"
                required
              />
            </td>
            <th scope="row">
              Intelligent
            </th>
          </tr>
          <tr>
            <th scope="row">
              Foolish
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.foolish_sensible_selected"
                name="foolish_sensible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.foolish_sensible_selected"
                name="foolish_sensible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.foolish_sensible_selected"
                name="foolish_sensible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.foolish_sensible_selected"
                name="foolish_sensible"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.foolish_sensible_selected"
                name="foolish_sensible"
                required
              />
            </td>
            <th scope="row">
              Sensible
            </th>
          </tr>        
        </tbody>
      </table>

      <h5>
        1.4 Please describe anything from your interaction that influenced how you perceived the chatbot. You may also provide any additional impressions
        you had which were not already covered in the above questions.
      </h5>
      <b-form-group
        label-for="impressions_free"
      >
        <b-form-textarea
          id="impressions_free"
          v-model="form.impressions_free"
          required
          placeholder="Enter response"
        />
      </b-form-group> 


      <h3>2. Linguistic Style</h3>
      <h5>2.1 Please rate how you perceived the chatbot's <b>LANGUAGE STYLE</b> on the following scale:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Disruptive
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.disruptive_calmaing_selected"
                name="disruptive_calmaing"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.disruptive_calmaing_selected"
                name="disruptive_calmaing"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.disruptive_calmaing_selected"
                name="disruptive_calmaing"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.disruptive_calmaing_selected"
                name="disruptive_calmaing"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.disruptive_calmaing_selected"
                name="disruptive_calmaing"
                required
              />
            </td>
            <th scope="row">
              Calming
            </th>
          </tr>
          <tr>
            <th scope="row">
              Exaggerated
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.exaggerated_appropriate_selected"
                name="exaggerated_appropriate"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.exaggerated_appropriate_selected"
                name="exaggerated_appropriate"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.exaggerated_appropriate_selected"
                name="exaggerated_appropriate"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.exaggerated_appropriate_selected"
                name="exaggerated_appropriate"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.exaggerated_appropriate_selected"
                name="exaggerated_appropriate"
                required
              />
            </td>
            <th scope="row">
              Appropriate
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unrealistic
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.unrealistic_realistic_selected"
                name="unrealistic_realistic"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.unrealistic_realistic_selected"
                name="unrealistic_realistic"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.unrealistic_realistic_selected"
                name="unrealistic_realistic"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.unrealistic_realistic_selected"
                name="unrealistic_realistic"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.unrealistic_realistic_selected"
                name="unrealistic_realistic"
                required
              />
            </td>
            <th scope="row">
              Realistic
            </th>
          </tr>     
        </tbody>
      </table>

      <h3>3. Personal Pronouns</h3>
      <h5>3.1 Please rate how you perceived the chatbot's <b>USE (OR LACK OF USE) OF THE PRONOUN "I"</b> on the following scale:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Eerie
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.i_eerie_natural_selected"
                name="i_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.i_eerie_natural_selected"
                name="i_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.i_eerie_natural_selected"
                name="i_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.i_eerie_natural_selected"
                name="i_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.i_eerie_natural_selected"
                name="i_eerie_natural"
                required
              />
            </td>
            <th scope="row">
              Natural
            </th>
          </tr>
          <tr>
            <th scope="row">
              Dispensable
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.i_dispensable_indespensable_selected"
                name="i_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.i_dispensable_indespensable_selected"
                name="i_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.i_dispensable_indespensable_selected"
                name="i_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.i_dispensable_indespensable_selected"
                name="i_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.i_dispensable_indespensable_selected"
                name="i_dispensable_indespesable"
                required
              />
            </td>
            <th scope="row">
              Indespesable
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unsuitable
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.i_unsuitable_suitable_selected"
                name="i_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.i_unsuitable_suitable_selected"
                name="i_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.i_unsuitable_suitable_selected"
                name="i_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.i_unsuitable_suitable_selected"
                name="i_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.i_unsuitable_suitable_selected"
                name="i_unsuitable_suitable"
                required
              />
            </td>
            <th scope="row">
              Suitable
            </th>
          </tr>
        </tbody>
      </table>

      <h5>3.2 Please provide a short explanation of your choices from the previous question.</h5>
      <b-form-group
        label-for="pronoun_i_free"
      >
        <b-form-textarea
          id="pronoun_i_free"
          v-model="form.pronoun_i_free"
          required
          placeholder="Enter response"
        />
      </b-form-group> 


      <h5>3.3 Please rate how you perceived the chatbot's <b>USE (OR LACK OF USE) OF THE PRONOUN "YOU"</b> on the following scale:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Eerie
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.you_eerie_natural_selected"
                name="you_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.you_eerie_natural_selected"
                name="you_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.you_eerie_natural_selected"
                name="you_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.you_eerie_natural_selected"
                name="you_eerie_natural"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.you_eerie_natural_selected"
                name="you_eerie_natural"
                required
              />
            </td>
            <th scope="row">
              Natural
            </th>
          </tr>
          <tr>
            <th scope="row">
              Dispensable
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.you_dispensable_indespensable_selected"
                name="you_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.you_dispensable_indespensable_selected"
                name="you_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.you_dispensable_indespensable_selected"
                name="you_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.you_dispensable_indespensable_selected"
                name="you_dispensable_indespesable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.you_dispensable_indespensable_selected"
                name="you_dispensable_indespesable"
                required
              />
            </td>
            <th scope="row">
              Indespesable
            </th>
          </tr>
          <tr>
            <th scope="row">
              Unsuitable
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.you_unsuitable_suitable_selected"
                name="you_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.you_unsuitable_suitable_selected"
                name="you_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.you_unsuitable_suitable_selected"
                name="you_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.you_unsuitable_suitable_selected"
                name="you_unsuitable_suitable"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.you_unsuitable_suitable_selected"
                name="you_unsuitable_suitable"
                required
              />
            </td>
            <th scope="row">
              Suitable
            </th>
          </tr>
        </tbody>
      </table>

      <h5>3.4 Please provide a short explanation of your choices from the previous question.</h5>
      <b-form-group
        label-for="pronoun_you_free"
      >
        <b-form-textarea
          id="pronoun_you_free"
          v-model="form.pronoun_you_free"
          required
          placeholder="Enter response"
        />
      </b-form-group>        

      <h3>4. Gender</h3>
      <h5>4.1 If you had to assign a gender to the chatbot, what would it be?</h5>

      <b-form-group style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom:2%">
        <b-form-radio
          v-model="form.gender_selected"
          name="gender"
          value="male"
          required
        >
          Male
        </b-form-radio>
        <b-form-radio
          v-model="form.gender_selected"
          name="gender"
          value="female"
          required
        >
          Female
        </b-form-radio>
        <b-form-radio
          v-model="form.gender_selected"
          name="gender"
          value="genderless"
          required
        >
          Genderless
        </b-form-radio>
      </b-form-group>

      <h5>4.2 Please provide a short explanation of your choice.</h5>
      <b-form-group
        label-for="gender_free"
      >
        <b-form-textarea
          id="gender_free"
          v-model="form.gender_free"
          required
          placeholder="Enter response"
        />
      </b-form-group>          
        
      <h3>5. Feeling during the interaction</h3>  
      <h5>
        5.1 Please reflect on your conversation with the chatbot and rate <b>HOW MUCH YOU EXPERIENCED EACH FEELING</b> on the following scale from 1 <i>(NOT AT ALL)</i>
        to 5 (<i>A LOT)</i>
      </h5>
      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col" class="text-center">
              1
            </th>
            <th scope="col" class="text-center">
              2
            </th>
            <th scope="col" class="text-center">
              3
            </th>
            <th scope="col" class="text-center">
              4
            </th>
            <th scope="col" class="text-center">
              5
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Positive
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_positive_selected"
                name="feeling_positive"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_positive_selected"
                name="feeling_positive"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_positive_selected"
                name="feeling_positive"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_positive_selected"
                name="feeling_positive"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_positive_selected"
                name="feeling_positive"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Good
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_good_selected"
                name="feeling_good"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_good_selected"
                name="feeling_good"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_good_selected"
                name="feeling_good"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_good_selected"
                name="feeling_good"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_good_selected"
                name="feeling_good"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Pleasant
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_pleasant_selected"
                name="feeling_pleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_pleasant_selected"
                name="feeling_pleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_pleasant_selected"
                name="feeling_pleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_pleasant_selected"
                name="feeling_pleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_pleasant_selected"
                name="feeling_pleasant"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Happy
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_happy_selected"
                name="feeling_happy"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_happy_selected"
                name="feeling_happy"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_happy_selected"
                name="feeling_happy"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_happy_selected"
                name="feeling_happy"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_happy_selected"
                name="feeling_happy"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Joyful
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_joyful_selected"
                name="feeling_joyful"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_joyful_selected"
                name="feeling_joyful"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_joyful_selected"
                name="feeling_joyful"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_joyful_selected"
                name="feeling_joyful"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_joyful_selected"
                name="feeling_joyful"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Contended
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_contented_selected"
                name="feeling_contented"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_contented_selected"
                name="feeling_contented"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_contented_selected"
                name="feeling_contented"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_contented_selected"
                name="feeling_contented"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_contented_selected"
                name="feeling_contented"
                required
              />
            </td>
          </tr>

          <tr>
            <th scope="row">
              Negative
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_negative_selected"
                name="feeling_negative"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_negative_selected"
                name="feeling_negative"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_negative_selected"
                name="feeling_negative"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_negative_selected"
                name="feeling_negative"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_negative_selected"
                name="feeling_negative"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Bad
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_bad_selected"
                name="feeling_bad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_bad_selected"
                name="feeling_bad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_bad_selected"
                name="feeling_bad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_bad_selected"
                name="feeling_bad"
                required
              />
            </td class="text-center">
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_bad_selected"
                name="feeling_bad"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Unpleasant
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_unpleasant_selected"
                name="feeling_unpleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_unpleasant_selected"
                name="feeling_unpleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_unpleasant_selected"
                name="feeling_unpleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_unpleasant_selected"
                name="feeling_unpleasant"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_unpleasant_selected"
                name="feeling_unpleasant"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Sad
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_sad_selected"
                name="feeling_sad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_sad_selected"
                name="feeling_sad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_sad_selected"
                name="feeling_sad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_sad_selected"
                name="feeling_sad"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_sad_selected"
                name="feeling_sad"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Afraid
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_afraid_selected"
                name="feeling_afraid"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_afraid_selected"
                name="feeling_afraid"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_afraid_selected"
                name="feeling_afraid"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_afraid_selected"
                name="feeling_afraid"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_afraid_selected"
                name="feeling_afraid"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Angry
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.feeling_angry_selected"
                name="feeling_angry"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.feeling_angry_selected"
                name="feeling_angry"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.feeling_angry_selected"
                name="feeling_angry"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.feeling_angry_selected"
                name="feeling_angry"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.feeling_angry_selected"
                name="feeling_angry"
                required
              />
            </td>
          </tr>              
        </tbody>
      </table> 


      <h3>6. Trust</h3>
      <h5>6.1 Please indicate how much you agree with the following statements:</h5>

      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" class="text-center"/>
            <th scope="col" class="text-center">
              Strongly disagree
            </th>
            <th scope="col" class="text-center">
              Rather disagree
            </th>
            <th scope="col" class="text-center">
              Neither agree nor disagree
            </th>
            <th scope="col" class="text-center">
              Rather agree
            </th>
            <th scope="col" class="text-center">
              Strongly agree
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              I already know similar systems.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_1_selected"
                name="trust_in_auto_1"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_1_selected"
                name="trust_in_auto_1"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_1_selected"
                name="trust_in_auto_1"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_1_selected"
                name="trust_in_auto_1"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_1_selected"
                name="trust_in_auto_1"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              I rather trust an automated system than mistrust it.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_2_selected"
                name="trust_in_auto_2"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_2_selected"
                name="trust_in_auto_2"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_2_selected"
                name="trust_in_auto_2"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_2_selected"
                name="trust_in_auto_2"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_2_selected"
                name="trust_in_auto_2"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              One should be careful with unfamiliar automated systems.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_3_selected"
                name="trust_in_auto_3"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_3_selected"
                name="trust_in_auto_3"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_3_selected"
                name="trust_in_auto_3"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_3_selected"
                name="trust_in_auto_3"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_3_selected"
                name="trust_in_auto_3"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              The developers take my well being seriously.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_4_selected"
                name="trust_in_auto_4"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_4_selected"
                name="trust_in_auto_4"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_4_selected"
                name="trust_in_auto_4"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_4_selected"
                name="trust_in_auto_4"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_4_selected"
                name="trust_in_auto_4"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              I trust the system.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_5_selected"
                name="trust_in_auto_5"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_5_selected"
                name="trust_in_auto_5"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_5_selected"
                name="trust_in_auto_5"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_5_selected"
                name="trust_in_auto_5"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_5_selected"
                name="trust_in_auto_5"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              The developers are trustworthy.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_6_selected"
                name="trust_in_auto_6"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_6_selected"
                name="trust_in_auto_6"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_6_selected"
                name="trust_in_auto_6"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_6_selected"
                name="trust_in_auto_6"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_6_selected"
                name="trust_in_auto_6"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              I can rely on the system.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_7_selected"
                name="trust_in_auto_7"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_7_selected"
                name="trust_in_auto_7"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_7_selected"
                name="trust_in_auto_7"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_7_selected"
                name="trust_in_auto_7"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_7_selected"
                name="trust_in_auto_7"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              I have already used similar systems.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_8_selected"
                name="trust_in_auto_8"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_8_selected"
                name="trust_in_auto_8"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_8_selected"
                name="trust_in_auto_8"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_8_selected"
                name="trust_in_auto_8"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_8_selected"
                name="trust_in_auto_8"
                required
              />
            </td>
          </tr>
          <tr>
            <th scope="row">
              Automated systems generally work well.
            </th>
            <td class="text-center">
              <b-form-radio
                value="1"
                v-model="form.trust_in_auto_9_selected"
                name="trust_in_auto_9"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="2"
                v-model="form.trust_in_auto_9_selected"
                name="trust_in_auto_9"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="3"
                v-model="form.trust_in_auto_9_selected"
                name="trust_in_auto_9"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="4"
                v-model="form.trust_in_auto_9_selected"
                name="trust_in_auto_9"
                required
              />
            </td>
            <td class="text-center">
              <b-form-radio
                value="5"
                v-model="form.trust_in_auto_9_selected"
                name="trust_in_auto_9"
                required
              />
            </td>
          </tr>
        </tbody>
      </table> 

      <h3>7. Satisfaction</h3>
      <h5>7.1 Please indicate how satisfied you were with the chatbot in terms of the <b>OVERALL INTERACTION</b>:</h5>  
      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Very dissatisfied
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.satisfied_interaction_selected"
                name="satisfied_interaction"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.satisfied_interaction_selected"
                name="satisfied_interaction"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.satisfied_interaction_selected"
                name="satisfied_interaction"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.satisfied_interaction_selected"
                name="satisfied_interaction"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.satisfied_interaction_selected"
                name="satisfied_interaction"
                required
              />
            </td>
            <th scope="row">
              Completely satisfied
            </th>
          </tr>
        </tbody>
      </table> 

      <h5>7.2 Please indicate how satisfied you were with the chatbot in terms of the <b>TASK-COMPLETION</b>:</h5>  
      <table
        class="table table-striped"
        style="width: 70%; margin-top: 2%; margin-left: 15%; margin-bottom: 2%"
      >
        <thead>
          <tr>
            <th scope="col" />
            <th scope="col">
              1
            </th>
            <th scope="col">
              2
            </th>
            <th scope="col">
              3
            </th>
            <th scope="col">
              4
            </th>
            <th scope="col">
              5
            </th>
            <th scope="col" />                
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              Very dissatisfied
            </th>
            <td>
              <b-form-radio
                value="1"
                v-model="form.satisfied_task_selected"
                name="satisfied_task"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="2"
                v-model="form.satisfied_task_selected"
                name="satisfied_task"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="3"
                v-model="form.satisfied_task_selected"
                name="satisfied_task"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="4"
                v-model="form.satisfied_task_selected"
                name="satisfied_task"
                required
              />
            </td>
            <td>
              <b-form-radio
                value="5"
                v-model="form.satisfied_task_selected"
                name="satisfied_task"
                required
              />
            </td>
            <th scope="row">
              Completely satisfied
            </th>
          </tr>
        </tbody>
      </table>

      <h5>7.3 What things did you find positive about the interaction.</h5>
      <b-form-group
        label-for="positive_free"
      >
        <b-form-textarea
          id="positive_free"
          v-model="form.positive_free"
          placeholder="Enter response"
        />
      </b-form-group>

      <h5>7.4 What things did you find negative about the interaction.</h5>
      <b-form-group
        label-for="negative_free"
      >
        <b-form-textarea
          id="negative_free"
          v-model="form.negative_free"
          placeholder="Enter response"
        />
      </b-form-group>             
      
      <b-button
        type="submit"
        variant="primary"
        style="margin-bottom:2%; margin-left:45%"
      >
        Submit
      </b-button>
    </b-form>
    <div style="position: abosolute; text-align: center; margin-top: 40%;" v-else>
      <h4>
        Thank you for participating. Your code is <b>{{code}}</b>. Once you have copied it, you can close this window.
      </h4>
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
  </div>
</template>

<style scoped>

.containter{
  width: 70%;
  margin: auto;
  height: 97%; 
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
import Vue from 'vue';
import axios from 'axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import { mapState } from "vuex";

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
    name: 'Survey',
    computed: {
      
      ...mapState(["token"]),
    },    
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/ws?token=" + this.token);
        this.socket.onopen = (event) => {
          // this.startDialog();
        };
        this.socket.onmessage = (msg) => {
          var content = JSON.parse(msg.data)
          if (content['topic'] == 'survey_code') {
            this.code = content['msg']
            // alert("Thank you for participating your completion code is: " + content['msg'])
            
          }
        }        
      }
    },     
    data() {
      return {
        form: {
          fake_natural_selected: '',
          machinelike_humanlike_selected: '',
          unconscious_conscious_selected: '',
          artificial_lifelike_selected: '',
          dislike_like_selected: '',
          unfriendly_friendly_selected: '',
          unkind_kind_selected: '',
          unpleasant_pleasant_selected: '',
          awful_nice_selected: '',
          incompetent_competent_selected: '',
          ignorant_knowledegeable_selected: '',
          irresponsible_responsible_selected: '',
          unintelligent_intelligent_selected: '',
          foolish_sensible_selected: '',
          disruptive_calmaing_selected: '',
          exaggerated_appropriate_selected: '',
          unrealistic_realistic_selected: '',
          i_eerie_natural_selected: '',
          i_dispensable_indespensable_selected: '',
          i_unsuitable_suitable_selected: '',
          you_eerie_natural_selected: '',
          you_dispensable_indespensable_selected: '',
          you_unsuitable_suitable_selected: '',
          gender_selected: '',
          feeling_positive_selected: '',
          feeling_good_selected: '',
          feeling_pleasant_selected: '',
          feeling_happy_selected: '',
          feeling_joyful_selected: '',
          feeling_contented_selected: '',
          feeling_negative_selected: '',
          feeling_bad_selected: '',
          feeling_unpleasant_selected: '',
          feeling_sad_selected: '',
          feeling_afraid_selected: '',
          feeling_angry_selected: '',
          trust_in_auto_1_selected: '',
          trust_in_auto_2_selected: '',
          trust_in_auto_3_selected: '',
          trust_in_auto_4_selected: '',
          trust_in_auto_5_selected: '',
          trust_in_auto_6_selected: '',
          trust_in_auto_7_selected: '',
          trust_in_auto_8_selected: '',
          trust_in_auto_9_selected: '',
          satisfied_interaction_selected: '',
          satisfied_task_selected: '',
          dem_gender_selected: '',
          dem_age_selected: '',
          dem_country: '',
          dem_native_language: '',
          impressions_free: '',
          pronoun_i_free: '',
          pronoun_you_free: '',
          gender_free: '',
          positive_free: '',
          negative_free: '',
        },
        socket: null,
        active: true,
        code: null,
      }
    },  
    methods: {
        has_token: function() {
            return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
        },      
      onSubmit(evt) {
        evt.preventDefault()
        if (this.has_token()){
          this.socket.send(JSON.stringify({
            access_token: this.token,
            topic: "get_survey_code",
          }));
          var m = {};
          Object.assign(m, this.form, {access_token: this.token, topic: "survey_results"});
          this.socket.send(JSON.stringify(m));
          this.active = false;         
        }
        else {
          this.$bvModal.show('connectionalert')
        };
      },
    },   
}
</script>