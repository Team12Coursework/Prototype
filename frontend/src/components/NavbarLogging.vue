<template>
    <nav class="orange-background-color shadow-xl">
        <div class="px-2 sm:px-6 lg:px-8">
            <div class="relative flex items-center justify-between h-14">

                <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
                    <div class="flex-shrink-0 flex items-center font-bold text-lg text-white"><router-link to="/"><img class="logo-max-width" src='../assets/Character_Connect_Logo.jpg'></router-link></div>
                </div>

                <div class="flex items-center space-x-2 text-xs">
                    <div class="ml-3 relative">
                        <div>
                            <div @click="toggleDropdown()" ref="dropdownMenu" class="cursor-pointer">
                                <span class="sr-only">Open user menu</span>
                                <p class='h-10 w-10 rounded-full flex items-center justify-center text-white font-bold bg-purple-400'>HL</p>
                            </div>
                        </div>

                        <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                            <div v-if="dropdownOpen"  class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                                <router-link to='/settings' class="bg-white hover:bg-gray-100 block px-4 py-2 text-sm text-gray-700">Settings</router-link>
                                <router-link to='/logout' class="bg-white hover:bg-gray-100 block px-4 py-2 text-sm text-red-700">Logout</router-link>
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            dropdownOpen: false,
        }
    },

    methods: {
        documentClick(event) {
            let elem = this.$refs.dropdownMenu;
            let target = event.target;

            if ((elem !== target) && !elem.contains(target)) {
                this.dropdownOpen = false;
            }
        },

        toggleDropdown() {
            this.dropdownOpen = !this.dropdownOpen;
        }
    },

    created() {
        document.addEventListener("click", this.documentClick);
    },

    unmounted() {
        document.removeEventListener("click", this.documentClick);
    }
}
</script>
