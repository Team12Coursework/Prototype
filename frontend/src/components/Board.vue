<template>
    <div :id="id" class="board rounded" @dragover.prevent @drop.prevent="drop">
        <slot></slot>
    </div>
</template>


<script>
export default{
    props: {
        id: {
            type: Number,
            required: true,
        }
    },

    methods: {
        drop(e) {
            const card_id = e.dataTransfer.getData('card_id');
            const card = document.getElementById(card_id);

            console.log(this.id, card_id);

            card.style.display = "block";
            e.target.appendChild(card);
        }
    }
}

</script>
