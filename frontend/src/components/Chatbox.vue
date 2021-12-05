<template>
    <!-- Chatbox component used for the Chat functionality in the game screen -->

    <form @submit="sendMessage" class="add-form">
        <div class="border p-2 rounded flex flex-col justify-between h-96 w-90/100">
            <div class="flex flex-col">
                    {{ messages }}
                    <!-- <p v-for="message in messages" :key="message"><span class="font-bold text-blue-500">{{ message.sender }}:</span> {{ message.message }}</p> -->
            </div>
            <input class="border rounded p-2" type="text" v-model="text" placeholder="Your message here..." />
        </div>
    </form>
</template>

<script>
export default {
    name: 'Chatbox',
    props: {
        messages: Array,
    },

    data() {
        return {
            text: "",
        }
    },

    methods: {
        sendMessage(e) {
            e.preventDefault();

            if(!this.text) {
                alert('Please add a comment');
                return;
            }

            this.$emit("update:messages", this.text);
            this.text = ""; // reset the textbox back to an empty string
        }
    },
}
</script>
