<template>
        <main class="w-full flex">

            <Board class="w-full border bg-gray-500" id="board-1">
                <Card id="card-1" draggable="true">
                    <p>A</p>
                </Card>

                <Card id="card-2" draggable="true">
                    <p>B</p>
                </Card>

                <Card id="card-3" draggable="true">
                    <p>C</p>
                </Card>

                <Card id="card-4" draggable="true">
                    <p>D</p>
                </Card>

                <Card id="card-5" draggable="true">
                    <p>E</p>
                </Card>

                <Card id="card-6" draggable="true">
                    <p>F</p>
                </Card>

                <Card id="card-7" draggable="true">
                    <p>G</p>
                </Card>

            </Board>


            <div class="w-full border space-x-2 flex">
                <div class="space-y-2" v-for ="i in 15" :key ="i">

                <Board class="bg-green-500" v-for ="j in 15" :key ="j" id="board-2" />
                
                </div>
            </div>

            
            
        </main>
</template>



<script>
<<<<<<< HEAD
import BasicLayout from "@/layouts/BasicLayout.vue";
import TileHolder from "@/components/TileHolder.vue";
import GameBoard from "@/components/GameBoard.vue";
import Chatbox from "@/components/Chatbox.vue";

export default {
    name: "Home",

    components: {
        BasicLayout,
        TileHolder,
        GameBoard,
        Chatbox,
    },
};
</script>
=======
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
>>>>>>> drag and drop feature
