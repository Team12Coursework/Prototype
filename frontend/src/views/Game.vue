<template>
        <navbar />

        <main class="w-full flex flex-col items-center min-h-screen h-screen p-6 space-y-4  bg-yellow-200 bg-opacity-60">
            <div class="max-w-screen-2xl space-y-4 w-full flex flex-col">
                <scoreboard v-if="players.length === 2" :players="players" />

                <div class="w-full flex h-full justify-center space-x-4">
                    <div class="w-full flex flex-col space-y-4">
                        <div class="w-full space-x-2 flex p-4 rounded" style="background: rgb(255,233,190); background: linear-gradient(0deg, rgba(255,233,190,1) 0%, rgba(236,198,126,1) 25%, rgba(237,200,130,1) 75%, rgba(255,233,190,1) 100%);">
                            <div class="space-y-2 w-full flex flex-col" v-for ="i in 15" :key ="i">
                                <board-square class="w-full p-1 flex items-center justify-center" :style="tileColour(squareId(i, j))" v-for ="j in 15" :key ="j" :id="squareId(i, j)" />
                            </div>
                        </div>

                        <div class="w-full p-2 bg-black shadow-inner rounded h-24 flex space-x-2">
                            <card v-for="tile in tiles" :key="tile[2]" :letter="tile[0]" :points="tile[1]" :id="tile[2]" :draggable="true"/>
                        </div>

                        <div v-if="piecePlaced" class="flex space-x-2 w-full justify-between">
                            <button @click="resetBoard" class="cursor-pointer text-xl font-semibold bg-blue-500 w-36 p-4 rounded-lg text-white">Reset</button>
                            <button @click="nextTurn" class="cursor-pointer text-xl font-semibold bg-blue-500 w-36 rounded-lg text-white">Next Turn</button>
                        </div>
                    </div>

                    <div class="w-3/4 flex flex-col space-y-2">
                        <chatbox :messages="chatMessages" @update:messages="newValue => sendChatMessage(newValue)" />

                        <div class="flex space-x-2 w-full">
                            <button @click="activatePerk('oneRandomLetter')" class="cursor-pointer p-2 bg-gray-400 w-full rounded text-white">Add Tile</button>
                            <button @click="activatePerk('twoRandomLetters')" class="cursor-pointer p-2 bg-gray-400 w-full rounded text-white">Add Two Tiles</button>
                            <button @click="activatePerk('changeLetters')" class="cursor-pointer p-2 bg-gray-400 w-full rounded text-white">Shuffle Tiles</button>
                        </div>
                    </div>
                </div>
            </div>
        </main>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { baseWebSocketURL } from "@/constants.js";

import BoardSquare from '@/components/BoardSquare.vue'
import Card from '@/components/Card.vue'
import Navbar from '@/components/Navbar.vue'
import Chatbox from '@/components/Chatbox.vue'
import Scoreboard from '@/components/Scoreboard.vue'

const store = useStore();
const route = useRoute();
const router = useRouter();

const chatMessages = ref([]);
const gameData = ref(null);
const placed = ref(false);

const localBoard = null;
let socket = null;

import power_up from "@/assets/music/power up.wav"
const perkSound = new Audio(power_up)

function activatePerk(perkName){
    socket.send(JSON.stringify({
        type: "activatePerk",
        subtype: perkName,
    }))
};

function squareId(x, y) {
    return `${(x-1).toString()},${(y-1).toString()}`
};

function tileColour(squareId) {
    const RED_TILES = new Set([ "0,0", "0,7", "7,14", "14,7", "14,14", "0,14", "14,0", "7,0", "7,7"]);
    const BLUE_TILES = new Set([
        "11,0", "3,0", "7,3", "8,2", "9,1", "6,2", "5,1", // top side
        "0,11", "0,3", "3,7", "2,8", "1,9", "2,6", "1,5", // left side
        "11,14", "3,14", "7,11", "8,12", "9,13", "6,12", "5,13", // bottom side
        "14,11", "14,3", "11,7", "12,8", "13,9", "12,6", "13,5", // left side
    ]);

    // check if square is one of the predefined red tiles
    if (RED_TILES.has(squareId)) {
        return "background-color: rgba(248, 113, 113, 1)";
    }

    // check if square is one of the squares surrounding the red tiles
    // on the edge of the board.
    if (BLUE_TILES.has(squareId)) {
        return "background-color: rgba(96, 165, 250, 0.3)";
    }

    let idx = squareId.split(",");
    let x = parseInt(idx[0]);
    let y = parseInt(idx[1]);

    // check if square is on the diagonal
    if (x === y || x === 14 - y) {
        // check if diagonals are within 3 tiles of the center
        if (Math.abs(x-7) < 3 && Math.abs(y-7) < 3)
            return "background-color: rgba(96, 165, 250, 0.3)";
        else
            return "background-color: rgba(248, 113, 113, 0.3)";
    }
    return "background: rgba(243, 244, 246, 0.5)";
};


import reset_word from "@/assets/music/reset_word.wav"
const resetWord = new Audio(reset_word)

function resetBoard() {
    console.log(gameData.value.board);
    resetWord.play();
    store.commit("board/updateBoard", JSON.parse(JSON.stringify(gameData.value.board)));
};

function updateError(data) {
    alert(data.message);
    resetBoard();
};

function updateGame(data) {
    if (data.winner !== null) {
        router.push({ name: "GameOver" });
    }
    gameData.value = data;
    resetBoard();
};

import next_turn from "@/assets/music/next_turn.wav"
const nextTurnSound = new Audio(next_turn)

function nextTurn() {
  nextTurnSound.play();
    socket.send(JSON.stringify({
        type: "gameUpdate",
        board: store.state.board.board,
    }))
};

function sendChatMessage(message) {
    console.log("in sendChatMessage");
    socket.send(JSON.stringify({
        type: "message",
        message: message,
        fromUser: user.value,
        sentAt: new Date().toLocaleTimeString('en-GB')
    }));
};

function receiveChatMessage(message) {
    console.log("received message", message);
    chatMessages.value.push(message);
};

function handleMessage(event) {
    let data = JSON.parse(event.data);
    switch(data.type) {
        case "gameUpdate":
            console.log(data);
            updateGame(data);
            break;
        case "message":
            receiveChatMessage(data);
            break;
        case "updateError":
            updateError(data);
            break;
    }
};

const storeData = computed(() => { return store.state.board });

const tiles = computed(() => {
    if (gameData.value === null)
        return [];

    for (let player of gameData.value.players)
        if (player.name == user.value)
            return player.tiles;
    return [];
});

const players = computed(() => {
    if (gameData.value === null)
        return [];
    return gameData.value.players;
});

const piecePlaced = computed(() => {
    return store.state.board.placed;
});

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

onMounted(() => {
    socket = new WebSocket(`${baseWebSocketURL}/api/game/ws/${route.params.game_id}`);
    socket.addEventListener("open", () => {
        socket.send(JSON.stringify({
            type: "playerJoin",
            player: user.value,
        }))
    })

    socket.addEventListener("message", handleMessage);
})
</script>
