import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TransactionView from '../views/TransactionView.vue'
import MoreInfoView from '../views/MoreInfoView.vue'
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/transaction',
    name: 'transaction',
    component: TransactionView
  },
  {
    path: '/moreinfo',
    name: 'moreinfo',
    component: MoreInfoView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path : '/register',
    name : "register",
    component : RegisterView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router