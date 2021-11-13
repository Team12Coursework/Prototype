import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router/index.js';
import './assets/tailwind.css'
import store from './store'

const app = createApp(App).use(store).use(router);

app.use(router);

app.mount('#app')
