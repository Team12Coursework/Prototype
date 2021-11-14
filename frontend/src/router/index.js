import { createRouter, createWebHistory } from 'vue-router'
import MainMenu from '../views/MainMenu.vue'

const routes = [
    {
        path: '/',
        name: 'MainMenu',
        component: MainMenu
    },
    {
        path: "/play",
        name: "Play",
        component: () => import("@/views/Game.vue"),
    },
    {
        path: "/leaderboard",
        name: "Leaderboard",
        component: () => import("@/components/Leaderboard.vue"),
    },
    {
        path: "/settings",
        name: "Settings",
        component: () => import("@/views/Settings.vue"),
    },
    {
        path: "/login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: () => import("@/views/Register.vue"),
    },
    {
        path: "/gamemodes",
        name: "GameModes",
        component: () => import("@/views/GameModes.vue"),

    },
    {
        path: "/gameover",
        name: "GameOver",
        component: () => import("@/views/GameOver.vue"),
    },
    {
        path: '/:catchAll(.*)', // catch-all route used to display a 404 page to any invalid pages
        component: () => import("@/views/404NotFound.vue"),
    },
]

const router = createRouter({
    // router history mode allows using the back button on the browser to visit the previous page
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
