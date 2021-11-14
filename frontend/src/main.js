import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router/index.js';
import './assets/tailwind.css'
import store from './store'

// main file registers all components and plugins before mounting the Vue application to the #app
// div found in public/index.html

const app = createApp(App).use(store).use(router);

app.use(router);

app.mount('#app')
