<template>
    <!--
    Card component used to style the Scrabble pieces.
    -->
    <div :id="id" :draggable="draggable"
        class="font-bold w-full h-full flex flex-col items-center justify-center text-white bg-gradient-to-br from-blue-600 to-purple-600 cursor-pointer rounded"
        @dragstart="dragStart" @dragover.stop>
        <p class="w-full h-full flex items-center justify-center">{{ letter }}</p>
        <p class="w-full h-full flex items-end justify-end text-sm">{{ points }}</p>
    </div>
</template>

<script>
export default{
    props: {
        id: {
            type: Number,
            required: true,
        },
        draggable: {
            type: Boolean,
            required: true,
        },
        letter: {
            type: String,
            required: true,
        },
        points: {
            type: Number,
            required: true,
        }
    },

    methods: {
        dragStart(e) {
            const target = e.target;
            e.dataTransfer.setData('letter', this.letter);

            setTimeout(() =>{
                target.style.display = "none";
            }, 0);
        },
    }
}
</script>
