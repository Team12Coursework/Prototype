export const game = {
    
    state: {
        gameNum: 0
    },
    mutations: {
        toGeneral(state) {
             state.gameNum = 1   
        },

        toMaths(state) {
            state.gameNum = 2
        },

        toScience(state) {
            state.gameNum = 3
        },

        toCustom(state) {
            state.gameNum = 4
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
