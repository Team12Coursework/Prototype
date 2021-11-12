<template>
    <basic-layout>
        <div class='flex w-full justify-center space-x-6'>
            <div class="w-full max-w-5xl">
                <game-board class="w-full" />
                <tile-holder class="border shadow-sm mt-4" />
            </div>

            <chatbox />
        </div>
    </basic-layout>
</template>

<script>
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
    }
};
</script>
