import { createStore } from 'vuex'
import { auth } from '@/store/auth.module.js';
import { board } from '@/store/board.module.js';
import { game } from '@/store/game.module.js';

export default createStore({
    strict: false,
    modules: {
        auth,
        board,
        game,
    },
    plugins: [],
})
