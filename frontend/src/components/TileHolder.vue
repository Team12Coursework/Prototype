<template>
    <div
        class="w-full flex bg-gray-100 p-2 space-x-2 rounded"
        @drop="onDrop($event, 1)" 
        @dragenter.prevent
        @dragover.prevent
    >
        <div
            v-for="item in getList(1)"
            @dragstart="startDrag($event, item)"
            :key="item.id"
            class="bg-blue-400 rounded h-12 w-12 flex justify-center items-center p-2 cursor-pointer font-semibold text-white text-lg" draggable="true"
        >
            {{ item.title }}
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "TileHolder",
    setup() {
        const items = ref([
            { id: 0, title: 'A', list: 1},
            { id: 1, title: 'B', list: 1},
            { id: 2, title: 'C', list: 1},
        ])

        const getList = (list) => {
            return items.value.filter((item) => item.list == list)
        }

        const startDrag = (event, item) => {
            console.log(item);
            event.dataTransfer.dropEffect = "move";
            event.dataTransfer.effectAllowed = "move";

            event.dataTransfer.setData("itemID", item.id);
        }

        const onDrop = (event, list) => {
            const itemID = event.dataTransfer.getData("itemID");
            const item = items.value.find((item) => item.id == itemID);
            item.list = list;
        }

        return {
            getList,
            startDrag,
            onDrop,
        }
    },
}
</script>
