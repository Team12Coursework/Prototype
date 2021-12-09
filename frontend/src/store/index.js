import { createStore } from 'vuex'
import { auth } from '@/store/auth.module.js';
import { board } from '@/store/board.module.js';

export default createStore({
    strict: false,
    modules: {
        auth,
        board,
    },
    plugins: [],
})
