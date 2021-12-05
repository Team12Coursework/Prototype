<template>
    <!-- Chatbox component used for the Chat functionality in the game screen -->

    <form @submit="sendMessage" class="add-form">
        <div class="border p-2 rounded flex flex-col justify-between h-96 w-90/100">
            <div class="flex flex-col">
                <p v-for="message in messages" :key="message">
                    [{{ message.sentAt }}]:
                    <span v-if="message.type === 'playerJoin'" class="italic text-gray-600">{{ message.player.name }} joined the room</span>
                    <span v-if="message.type === 'message'">({{ message.fromUser }}) {{ message.message }}</span>
                </p>
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
        },
    },

    computed: {
        user() {
            // function to decode the JWT token given to the client at login.
            // this function will decode the JWT and extract the username which will be used to play the game.

            var base64Url = this.$store.state.auth.user.accessToken.split('.')[1];
            var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));

            return JSON.parse(jsonPayload).sub;
        },
    },
}
</script>
