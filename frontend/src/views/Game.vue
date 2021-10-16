<template>
    <basic-layout>
        <game-board />
    </basic-layout>
</template>

<script>
import BasicLayout from '@/layouts/BasicLayout.vue';
import GameBoard from '@/components/GameBoard.vue';

export default {
    name: "Home",
    components: {
        BasicLayout,
        GameBoard,
    }
};
</script>
