import { VueElement, createApp } from 'vue'
import App from './App.vue'
import router from './router'

VueElement.prototype.$loggedin = false;

createApp(App)
    .use(router)
    .mount('#app');
