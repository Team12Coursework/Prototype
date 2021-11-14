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
            // function to handle dropping the piece onto the board.
            // as soon as a piece is dropped, it will trigger an event
            // which will display the next turn and reset buttons.

            const card_id = e.dataTransfer.getData('card_id');
            const card = document.getElementById(card_id);
            const letter = card.childNodes[0].innerHTML;

            let x = (this.id % 15) - 1;
            let y = Math.floor(this.id / 15) - 1;

            let piece = {
                x: x,
                y: y,
                id: card_id,
                letter: letter,
            };

            this.$store.dispatch("board/movePiece", piece).then(
                () => {
                    console.log("piece moved successfully");
                }
            )

            card.style.display = "block";
            e.target.appendChild(card);
        }
    }
}

</script>
