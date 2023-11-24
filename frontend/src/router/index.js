// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginView.vue';
import HomePage from '@/views/HomeView.vue';

const routes = [
  {
    path: '/',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/home',
    name: 'HomePage',
    component: HomePage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
