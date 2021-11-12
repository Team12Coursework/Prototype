<template>
    <base-table :headings="['Against', 'Result', 'Date']">
        <tr>
            <td class="px-6 py-4 whitespace-nowrap">Harry Lees</td>
            <td class="px-6 py-4 whitespace-nowrap text-blue-500">Victory</td>
            <td class="px-6 py-4 whitespace-nowrap">2021-10-17</td>
        </tr>

        <tr>
            <td class="px-6 py-4 whitespace-nowrap">Harry Lees</td>
            <td class="px-6 py-4 whitespace-nowrap text-red-500">Defeat</td>
            <td class="px-6 py-4 whitespace-nowrap">2021-10-17</td>
        </tr>

        <tr>
            <td class="px-6 py-4 whitespace-nowrap">Harry Lees</td>
            <td class="px-6 py-4 whitespace-nowrap text-red-500">Defeat</td>
            <td class="px-6 py-4 whitespace-nowrap">2021-10-17</td>
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
            recentMatches: []
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