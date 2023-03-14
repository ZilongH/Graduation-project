import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Ripe from '@/components/Ripe'
import RipeAuth from '@/components/RipeAuth'
import Rov from '@/components/Rov'
import RipeAuthT from '@/components/RipeAuthT'
// import App from '@/App'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Ripe',
      name: 'Ripe',
      component: Ripe
    },
    {
      path: '/RipeAuth',
      name: 'RipeAuth',
      component: RipeAuth
    },
    {
      path: '/Rov',
      name: 'Rov',
      component: Rov
    },
    {
      path: '/RipeAuthT',
      name: 'RipeAuthT',
      component: RipeAuthT
    }
  ]
})
