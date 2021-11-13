<template>
        <main class="w-full flex min-h-screen h-screen border flex-col p-6 space-y-4">
            <div class="w-full h-full border space-x-2 flex">
                <div class="space-y-2 w-full h-full flex flex-col" v-for ="i in 15" :key ="i">
                    <Board class="bg-green-500 w-full min-h-24 h-full p-2 flex items-center justify-center" v-for ="j in 15" :key ="j" id="board-2" />
                </div>
            </div>

            <Board class="w-full border p-2 bg-gray-500 h-32 flex space-x-2" id="board-1">
                <Card v-for="i in 6" :key="i" :id="i" draggable="true">
                    <p>A</p>
                </Card>
            </Board>
        </main>
</template>

<script>
import Board from '@/components/Board.vue'
import Card from '@/components/Card.vue'

export default{
    name: 'game',
    components:{
        Board,
        Card
    }
}
</script>
