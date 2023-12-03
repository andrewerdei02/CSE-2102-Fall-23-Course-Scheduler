// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginView.vue';
import HomePage from '@/views/HomeView.vue';
import AdminLogin from '@/views/AdminLogin.vue';
import AdminHome from '@/views/AdminHome.vue';
import CourseAdjust from '@/views/CourseAdjust.vue';
import AddCourse from '@/views/AddCourse.vue';
import RemoveCourse from '@/views/RemoveCourse.vue';
import AdminCourses from '@/views/AdminCourses.vue';
import ViewSchedule from '@/views/ViewSchedule.vue';


const routes = [
  {
    path: '/',
    name: 'LoginPage',
    component: LoginPage
  },

  {
    path: '/ViewSchedule',
    name: 'ViewSchedule',
    component: ViewSchedule
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
    path: '/AddCourse',
    name: 'AddCourse',
    component: AddCourse
  },
  {
    path: '/RemoveCourse',
    name: 'RemoveCourse',
    component: RemoveCourse
  },

  {
    path: '/AdminCourses',
    name: 'AdminCourses',
    component: AdminCourses
  },

  {
    path: '/ClassSearch',
    name: 'ClassSearch',
    component: () => import( '../views/ClassSearchView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
