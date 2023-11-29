// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginView.vue';
import HomePage from '@/views/HomeView.vue';
import ClassSearch from '@/views/ClassSearchView.vue';

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
  },
  {
    path: '/class-search',
    name: 'ClassSearchView',
    component: ClassSearch
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
