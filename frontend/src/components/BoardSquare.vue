<template>
    <div class="rounded" @dragover.prevent @drop.prevent="drop" style="aspect-ratio: 1/1">
        <div v-if="letter" class="font-bold h-full w-full flex items-center justify-center bg-blue-500 text-gray-50 rounded">
            <p class="w-full h-full flex items-center justify-center">
                {{ letter }}
            </p>
        </div>
    </div>
</template>

<script>
export default{
    props: {
        id: {
            type: String,
            required: true,
        },
    },

    computed: {
        letter() {
            return this.$store.state.board.board[this.y][this.x];
        },

        x() {
            return parseInt(this.id.split(',')[0])
        },

        y() {
            return parseInt(this.id.split(',')[1])
        },
    },

    methods: {
        drop(e) {
            // function to handle dropping the piece onto the board.
            // as soon as a piece is dropped, it will trigger an event
            // which will display the next turn and reset buttons.

            const letter = e.dataTransfer.getData('letter');

            console.log('drop', this.x, this.y);

            let piece = {
                x: this.x,
                y: this.y,
                letter: letter,
            };

            this.$store.dispatch("board/movePiece", piece).then(
                () => {
                    console.log("piece moved successfully");
                }
            )
        }
    }
}

</script>
