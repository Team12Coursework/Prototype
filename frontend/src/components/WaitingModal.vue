<template>
    <teleport to="body">
        <div ref="modal-backdrop" class="fixed z-10 inset-0 overflow-y-auto bg-black bg-opacity-50">
            <div class="flex items-start justify-center min-h-screen pt-24 text-center">
                <div class="bg-white rounded-lg flex flex-col items-center space-y-6 overflow-hidden shadow-xl p-8 w-1/2" ref="modal">
                    <h1 class="text-4xl font-semibold">Waiting for Opponent</h1>
                    <p>
                        Please ensure your opponent has a working link, copy the link from the address bar above
                        for a fresh link.
                    </p>
                    <div style="border-top-color:transparent" class="w-16 h-16 border-4 border-blue-400 rounded-full animate-spin"></div>
                </div>
            </div>
        </div>
    </teleport>
</template>