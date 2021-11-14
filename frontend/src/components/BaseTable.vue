<template>
    <!-- 
    BaseTable component used for basic table styling 
    Components such as Leaderboard and MatchHistory will inherit from this component
    to ensure consistent styling
    -->
    <div class="border rounded shadow-md mt-4">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
                <tr>
                    <th v-for="heading in headings" :key="heading" scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">{{ heading }}</th>
                </tr>
            </thead>

            <tbody class="bg-white divide-y divide-gray-200">
                <slot>
                </slot>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        headings: {
            required: true,
            type: Array,
        },
    }
}
</script>
