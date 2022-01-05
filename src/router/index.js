import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/cat/:id',
    name: 'cat',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login

  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(function (){
  store.commit('clear_breadcrumb')
})

export default router

