export const game = {
    
    state: {
        gameNum: 0
    },
    mutations: {
        toMaths(state) {
             state.gameNum = 1   
        },

        toScience(state) {
            state.gameNum = 2
        },

        toCustom(state) {
            state.gameNum = 3
        },

        reset(state) {
            state.gameNum = 0
        }
    },
    actions: {

    },
    getters: {
        getGameNum(state) {
            return state.gameNum
        }
    }
}
