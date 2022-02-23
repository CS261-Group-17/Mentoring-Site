import Vue from 'vue'
import store from '@/store'
import router from '@/router'

import axios from 'axios'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
