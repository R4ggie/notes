import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../components/HomePage.vue'
import NotePage from '../components/NotePage.vue'
import PagePage from '../components/PagePage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/homepage',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/notepage',
    name: 'NotePage',
    component: NotePage
  },
  {
    path: '/pagepage',
    name: 'PagePage',
    component: PagePage
  },
  {
    path: '*',
    redirect: '/notepage'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
