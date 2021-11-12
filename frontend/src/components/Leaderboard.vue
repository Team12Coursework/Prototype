<template>
    <base-table :headings="['Rank', 'Username', 'Elo']">
        <tr v-for="user in users" :key="user.id">
            <td :class="coloured(user.rank)" class="px-6 py-4 whitespace-nowrap font-bold">{{ user.rank }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ user.username }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ user.elo }}</td>
        </tr>
    </base-table>
</template>

<script>
import BaseTable from "@/components/BaseTable.vue";

export default {
    components: {
        BaseTable,
    },

    data() {
        return {
            users: [
                {
                    id: 1,
                    username: "Harry Lees",
                    rank: 1,
                    elo: 2882,
                },
                {
                    id: 2,
                    username: "Harry Lees",
                    rank: 2,
                    elo: 2800,
                },
                {
                    id: 3,
                    username: "Harry Lees",
                    rank: 3,
                    elo: 2793,
                },
                {
                    id: 4,
                    username: "Harry Lees",
                    rank: 4,
                    elo: 2700,
                },
            ]
        }
    },

    methods: {
        coloured(rank) {
            switch (rank) {
                case 1:
                    return "text-green-500";
                case 2:
                    return "text-yellow-400";
                case 3:
                    return "text-red-500";
            }
            return "text-gray-500";
        }
    },
}
</script>