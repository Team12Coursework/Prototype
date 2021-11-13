<template>
    <div class="flex space-x-2 justify-center w-full">
        <div v-for="i in 15" :key="i" class="flex flex-col space-y-2 w-full">
            <div  v-for="j in 15" :key="j" class="flex bg-grey-100 w-full rounded justify-center items-center font-semibold" style="aspect-ratio: 1;">
                <Tile :class="colorTile(j)">{{ j }}</Tile>
            </div>
        </div>
    </div>
</template>

<script>
import Tile from "@/components/Tile.vue";

export default {
    name: "GameBoard",
    components: {
        Tile,
    },

    methods: {
    colorTile(j) {
        if (j % 2 == 0) {
            return "bg-green-500"
       } else {
            return "bg-red-500"
        }
    }
},

    mounted() {
        console.log("hello");
    },
}
</script>
