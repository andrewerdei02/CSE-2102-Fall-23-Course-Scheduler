import { VueElement, createApp } from 'vue'
import App from './App.vue'
import router from './router'

VueElement.prototype.$loggedin = false;

<script>
    const cors = require("cors");
    App.use(cors());
</script>

createApp(App)
    .use(router)
    .mount('#app');
