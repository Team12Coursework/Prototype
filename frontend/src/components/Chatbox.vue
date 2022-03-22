<template>
    <!-- Chatbox component used for the Chat functionality in the game screen -->

    <button class= " rounded-full m-1 font-bold w-36 h-10 border-black border-solid  outline-black"  @click="toggleMuted" :class="buttonColour()">MUTE CHAT</button>
    <form @submit="sendMessage" class="add-form">
        <div class=" bg-white border-solid border-4 shadow-lg rounded flex flex-col justify-between h-96 w-90/100 border-blue-500">
            <div class="flex flex-col">
                <p :style="colourMessage(message)" v-for="message in messages" :key="message">
                    [{{ message.sentAt }}]:
                    <span v-if="message.type === 'playerJoin'" class="italic text-gray-600">{{ message.player.name }} joined the room</span>
                    <span v-if="message.type === 'message'">({{ message.fromUser }}) {{ message.message }}</span>
                </p>
            </div>
            <input class="border rounded border-black p-2 w-3/4 self-center bg-gray-100 mb-1 " type="text" v-model="text" placeholder="Please type in your message here...." />
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
            muted: false
        }
    },

    methods: {
        colourMessage(message) {
            if (message.fromUser == this.user) {
                return "text-red-900"
            } else {
                return "text-red-800"
            }

        },
        
        sendMessage(e) {
            e.preventDefault();

            if(!this.text) {
                alert('Please add a comment');
                return;
            }

            this.$emit("update:messages", this.text);
            this.text = ""; // reset the textbox back to an empty string
        },
         toggleMuted(){
            this.muted = !this.muted;
        },
        buttonColour(){
            return this.muted ? "bg-red-600" : "bg-lime-400";
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
