<template>
    <div class="max-w-7xl grid grid-cols-4 gap-4 mx-auto">
        <div class="main-left col-span-1 space-y-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="flex justify-between">
                    <div class="flex items-center space-x-4">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                            alt="Profile Picture" class="h-[45px] rounded-full">
                        <div class="flex flex-col ml-2 -space-y-1">
                            <h1 class="font-semibold text-lg">Charles Leclerc</h1>
                            <p class="font-medium">Join Ferrari pls</p>
                        </div>
                    </div>
                    <div class="flex justify-center items-center mr-2">
                        <div class="h-[25px] w-[25px] bg-red-600 rounded-full flex items-center justify-center">
                            <p class="text-white">1</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="flex justify-between">
                    <div class="flex items-center space-x-4">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                            alt="Profile Picture" class="h-[45px] rounded-full">
                        <div class="flex flex-col ml-2 -space-y-1">
                            <h1 class="font-medium text-lg">Frederic Vasseur</h1>
                            <p class="text-sm text-gray-500">let me COOK</p>
                        </div>
                    </div>
                    <div class="flex items-center w-[50px]">
                        <p class="text-gray-400 font-thin">18 min. ago</p>
                    </div>
                </div>
            </div>
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="flex justify-between">
                    <div class="flex items-center space-x-4">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                            alt="Profile Picture" class="h-[45px] rounded-full">
                        <div class="flex flex-col ml-2 -space-y-1">
                            <h1 class="font-medium text-lg">Lewis Hamilton</h1>
                            <p class="text-sm text-gray-500">lando SUX</p>
                        </div>
                    </div>
                    <div class="flex items-center w-[50px]">
                        <p class="text-gray-400 font-thin">18 min. ago</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="main-right col-span-3 space-y-4">
            <div id="messages" class="p-4 bg-white border border-gray-200 rounded-lg space-y-4">
                <div class="flex flex-col">
                    <div class="flex justify-end">
                        <div class="flex space-x-2 m-4">
                            <div>
                                <div
                                    class=" rounded-b-lg rounded-l-lg bg-blue-600 flex items-center justify-center px-6 py-4">
                                    <p class="text-white">Lorem ipsum</p>
                                </div>
                                <p>8 minutes ago</p>
                            </div>
                            <div>
                                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                                    alt="Profile Picture" class="h-[45px] rounded-full">
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-end">
                        <div class="flex space-x-2 m-4">
                            <div>
                                <div
                                    class=" rounded-b-lg rounded-l-lg bg-blue-600 flex items-center justify-center px-6 py-4">
                                    <p class="text-white">Lorem ipsum</p>
                                </div>
                                <p>8 minutes ago</p>
                            </div>
                            <div>
                                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                                    alt="Profile Picture" class="h-[45px] rounded-full">
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-start">
                        <div class="flex space-x-2 m-4">
                            <div>
                                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                                    alt="Profile Picture" class="h-[45px] w-[45px] rounded-full">
                            </div>
                            <div class="max-w-[60%]">
                                <div
                                    class=" rounded-b-lg rounded-r-lg bg-green-500 flex items-center justify-center px-6 py-4 max-w-[60%]">
                                    <p class="text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                                        do eiusmod tempor
                                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                        nostrud exercitation
                                        ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                </div>
                                <p>8 minutes ago</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div id="textarea" class="p-4 bg-white border border-gray-200 text-center rounded-lg space-y-4">
                <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking?"></textarea>
                <div class="flex items-center justify-between border-t border-gray-200 pt-4">
                    <button class="bg-blue-600 py-4 px-6 text-white rounded-lg">Send</button>
                </div>
            </div>
        </div>
    </div>
</template>