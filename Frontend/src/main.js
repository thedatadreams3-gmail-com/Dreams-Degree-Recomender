import Vue from 'vue'
import App from './App.vue'
import VModal from 'vue-js-modal'
import './assets/bar.css'; // here css file for home page 


Vue.config.productionTip = false

Vue.use(VModal)

new Vue({
  render: h => h(App),
}).$mount('#app')
