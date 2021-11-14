<template>
        <navbar />

        <main class="w-full flex flex-col min-h-screen h-screen p-6 space-y-4">
            <scoreboard />
            <div class="w-full flex h-full space-x-4">
                <div class="w-full flex flex-col space-y-4">
                    <div class="w-full h-full space-x-2 flex">
                        <div class="space-y-2 w-full h-full flex flex-col" v-for ="i in 15" :key ="i">
                            <Board class="bg-gray-300 w-full min-h-24 h-full p-1 flex items-center justify-center" v-for ="j in 15" :key ="j" :id="loc(j, i)" />
                        </div>
                    </div>

                    <Board v-if="letters" class="w-full p-2 bg-gray-300 h-32 flex space-x-2" :id="0">
                        <Card v-for="i in 7" :key="i" :id="i" :letter="letters[i-1]" :draggable="true"/>
                    </Board>
                </div>

                <div class="w-full flex flex-col">
                    <chatbox />

                    <div v-if="piecePlaced" class="flex space-x-2">
                        <button @click="resetBoard" class="cursor-pointer p-2 bg-blue-500 rounded text-white">Reset</button>
                        <button @click="nextTurn" class="cursor-pointer p-2 bg-blue-500 rounded text-white">Next Turn</button>
                    </div>
                </div>
            </div>
        </main>
</template>

<script>
import Board from '@/components/Board.vue'
import Card from '@/components/Card.vue'
import Navbar from '@/components/Navbar.vue'
import Chatbox from '@/components/Chatbox.vue'
import Scoreboard from '@/components/Scoreboard.vue'

const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

export default{
    name: 'game',

    data() {
        return {
            alphabet,
            maxId: 0,
            letters: [],
        }
    },

    components:{
        Board,
        Card,
        Navbar,
        Chatbox,
        Scoreboard,
    },

    methods: {
        loc(x, y) {
            // method to return the square ID given the x, y position on the board
            return 15 * x + y
        },

        resetBoard() {
            this.$store.dispatch("resetBoard");
        },

        nextTurn() {
            this.$store.dispatch("nextTurn");
            this.generatePieces();
        },

        generatePieces() {
            let letters = [];
            for (let i=0; i<7; i++) {
                let letter = this.alphabet[Math.floor(Math.random() * 26)];
                letters.push(letter);
                this.maxId += 1;
            }
            this.letters = letters;
        }
    },

    computed: {
        boardArray() {
            return this.$store.state.board;
        },

        piecePlaced() {
            return this.$store.state.board.placed;
        }
    },

    created() {
        this.generatePieces();
    }
}
</script>
