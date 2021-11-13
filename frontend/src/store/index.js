import { createStore } from 'vuex'
import { auth } from '@/store/auth.module.js';

export default createStore({
    modules: {
        auth,
    },
})
