<template>
    <div class='h-12 w-12 rounded text-white flex justify-center font-bold items-center' :style="{background: color}">
        <p><slot></slot></p>
    </div>
</template>

<script>

export default {
    name: 'Tile',
    props: {
	color: String
	},
    data() {
         return {
    isMultiply: true,
    }

    },

methods: {

    multiply() {
    for (let j=0; j < 15; j++) {
        if (j % 2 == 0) {
            this.isMultiply = true;
        } else {
            this.isMultiply = false;
        }
    }

    let isMultiply = false;
    this.$emit("multiplier", isMultiply)

    },

},
}

</script>