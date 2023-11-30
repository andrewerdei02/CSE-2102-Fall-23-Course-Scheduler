// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginView.vue';
import HomePage from '@/views/HomeView.vue';
import AdminLogin from '@/views/AdminLogin.vue';
import AdminHome from '@/views/AdminHome.vue';
import CourseAdjust from '@/views/CourseAdjust.vue';

const routes = [
  {
    path: '/',
    name: 'LoginPage',
    component: LoginPage
  },

  {
    path: '/AdminLogin',
    name: 'AdminLogin',
    component: AdminLogin
  },

  {
    path: '/home',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/AdminHome',
    name: 'AdminHome',
    component: AdminHome
  },
  {
    path: '/CourseAdjust',
    name: 'CourseAdjust',
    component: CourseAdjust
  },
  {
    path: '/ClassSearch',
    name: 'Class Search',
    component: () => import( '../views/ClassSearchView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
