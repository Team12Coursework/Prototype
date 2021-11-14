<template>
    <div :id="id" :draggable="draggable"
        class="font-bold w-full h-full flex items-center justify-center bg-blue-500 text-gray-50 cursor-pointer rounded"
        @dragstart="dragStart" @dragover.stop
    >
        <p class="w-full h-full flex items-center justify-center">
            {{ letter }}
        </p>
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
    },
    
    methods: {
        dragStart(e) {
            const target = e.target;

            e.dataTransfer.setData('card_id', target.id);

            setTimeout(() =>{
                target.style.display = "none";
            }, 0);
        },
    }
}
</script>
