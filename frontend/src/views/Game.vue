<template>
        <navbar />
        <main class="w-1/2 flex min-h-screen h-screen border flex-col p-6 space-y-4">
            <div class="w-full h-full space-x-2 flex">
                <div class="space-y-2 w-full h-full flex flex-col" v-for ="i in 15" :key ="i">
                    <Board class="bg-green-500 w-full min-h-24 h-full p-1 flex items-center justify-center" v-for ="j in 15" :key ="j" :id="loc(i, j)" />
                </div>
            </div>

            <Board class="w-full border p-2 bg-gray-500 h-32 flex space-x-2" :id="0">
                <Card v-for="i in 6" :key="i" :id="i" :letter="alphabet[i]" :draggable="true" />
            </Board>
        </main>
</template>

<script>
import Board from '@/components/Board.vue'
import Card from '@/components/Card.vue'
import Navbar from '@/components/Navbar.vue'

const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

export default{
    name: 'game',

    data() {
        return {
            alphabet,
        }
    },

    components:{
        Board,
        Card,
        Navbar,
    },

    methods: {
        loc(x, y) {
            // method to return the square ID given the x, y position on the board
            return 15 * x + y
        },
    },
}
</script>
