<template>
    <navbar />

    <main class='flex space-x-5'>
        <sidebar>
            <sidebar-button to='/play'>Play</sidebar-button>
        </sidebar>

        <section class='p-5 w-full'>
            <slot></slot>
        </section>
    </main>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Sidebar from '@/components/Sidebar.vue';
import SidebarButton from '@/components/SidebarButton.vue';

export default {
    name: "BasicLayout",
    components: {
        Navbar,
        Sidebar,
        SidebarButton,
    }
};
</script>
