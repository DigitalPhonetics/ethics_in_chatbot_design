import Vue from 'vue';
import Router from 'vue-router';
// import Login from './components/login.vue';
import Login from './components/simple_login.vue'
import Chat from './components/chat.vue';
import DataAgreement from './components/data_agreement.vue';
import Survey from './components/survey.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Login-Default',
      component: Login,
      props: true,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      props: true,
    },
    {
      path: '/chat',
      name: 'Chat',
      component: Chat,
    },
    {
      path: '/agreement',
      name: 'Agreement',
      component: DataAgreement
    },
    {
      path: '/bippidyboop',
      name: 'Survey',
      component: Survey
    },
  ],
});
