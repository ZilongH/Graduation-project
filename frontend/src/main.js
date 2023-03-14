// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import HelloWorld from './components/HelloWorld'
// import Ripe from './components/Ripe'
import router from './router'
import 'bootstrap'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
// import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import VueAxios from 'vue-axios'
Vue.config.productionTip = false
axios.defaults.baseURL = '/api'
// Vue.use(ElementUI)
Vue.use(VueResource)
Vue.use(VueAxios)
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
