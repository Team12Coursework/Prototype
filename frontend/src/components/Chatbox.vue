<template>
    <!-- Chatbox component used for the Chat functionality in the game screen -->

    <form @submit="sendMessage" class="add-form">
        <div class="border p-2 rounded flex flex-col justify-between h-96 w-90/100">
            <div class="flex flex-col">
                <div>
                    <p v-for="message in messages" :key="message"><span class="font-bold text-blue-500">{{ message.sender }}:</span> {{ message.message }}</p>
                </div>
            </div>
            <input class="border rounded p-2" type="text" v-model="text" placeholder="Your message here..." />
        </div>
    </form>
</template>

<script>
export default {
    name: 'Chatbox',
    data() {
        return {
            messages: [],
            text: '',
        }
    },

    methods: {
        addMessage(message) {
            // dummy function provides functionality until the API is finished
            // this will be removed, and an API call will be added to ensure chat messages
            // are broadcast to the other users.
            this.messages = [... this.messages, message]
        },

        sendMessage(e) {
            e.preventDefault()

            if(!this.text) {
                alert('Please add a comment')
                return
            }

            this.addMessage({
                message: this.text,
                sender: "you"
            })
            this.text = ''
        }
    }
}
</script>
