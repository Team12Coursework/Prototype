<template>
    <div 
        :id="id"
        :draggable="draggable"
        class="font-bold w-full flex items-center justify-center bg-blue-500 text-white border cursor-pointer"
        @dragstart="dragStart"
        @dragover.stop
    >
        <p class="w-full text-center">
            <slot></slot>
        </p>
    </div>
</template>

<script>

export default{
    props: ['id', 'draggable'],
    methods:{
        dragStart: e => {
            const target = e.target;

            e.dataTransfer.setData('card_id', target.id);

            setTimeout(() =>{
                target.style.display = "none";
            }, 0);
        }
    }
}
    
</script>
