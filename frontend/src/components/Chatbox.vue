<template>
    <!-- Chatbox component used for the Chat functionality in the game screen -->


    <form @submit="sendMessage" class="add-form">
        <div class=" bg-white p-2 shadow-lg rounded flex flex-col h-96 w-90/100">
            <div class="rounded-md m-1 w-24 font-bold h-10 select-none cursor-pointer flex justify-center items-center" @click="muted = !muted" :class="buttonColour()">{{ muted ? "UNMUTE" : "MUTE" }}</div>

            <div class="flex flex-col justify-between flex-grow overflow-auto">
                <div class="flex flex-col space-y-2 p-2">
                    <p class="text-black p-2 pl-4 rounded-full w-3/4 italic" :class="colourMessage(message)" v-for="message in messages" :key="message">
                        [{{ message.sentAt }}]:
                        <span v-if="message.type === 'playerJoin'" class="italic text-gray-600">{{ message.player.name }} joined the room</span>
                        <span v-if="message.type === 'message'">({{ message.fromUser }}) {{ message.message }}</span>
                    </p>
                </div>

                <div class="w-full flex space-x-2">
                    <input class="border rounded border-black p-2 w-full bg-gray-100" type="text" v-model="text" placeholder="your message here..." />
                    <button class="rounded-lg bg-blue-500 hover:bg-blue-400 duration-100 w-1/2 text-white">Send</button>
                </div>
            </div>
        </div>
    </form>
</template>

<script setup>
import { computed, defineProps, ref, defineEmits } from "vue";
import { useStore } from "vuex";

const store = useStore();

const text = ref("");
const muted = ref(false);

const props = defineProps({
    messages: { type: Array, required: true }
});

const emit = defineEmits(["update:messages", "update:muted"]);

function colourMessage(message) {
    if (message.fromUser == user.value) {
        return "bg-blue-200"
    } else {
        return "bg-red-400"
    }
};

function sendMessage(event) {
    event.preventDefault();

    if(!text.value) {
        alert('Please add a comment');
        return;
    }

    console.log("in sendMessage");
    emit("update:messages", text.value);
    text.value = ""; // reset the textbox back to an empty string
};

function buttonColour(){
    return muted.value ? "bg-red-600" : "bg-blue-400";
};

const user = computed(() => {
    // function to decode the JWT token given to the client at login.
    // this function will decode the JWT and extract the username which will be used to play the game.
    var base64Url = store.state.auth.user.accessToken.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload).sub;
});
</script>
