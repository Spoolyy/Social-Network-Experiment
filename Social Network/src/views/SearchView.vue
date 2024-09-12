<script>
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import Trends from '@/components/Trends.vue';
export default {
    name: 'SearchView',
    components: {
        PeopleYouMayKnow,
        Trends
    }
}
</script>
<template>
    <div class=" max-w-7xl grid grid-cols-4 gap-4 mx-auto">
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-white flex p-4 border border-gray-200 rounded-lg space-x-4">
                <input type="search" name="search" id="searchbar" placeholder="What or who are you looking for?"
                    class="w-full p-4 rounded-lg bg-gray-100">
                <button class="bg-blue-600 rounded-lg py-4 px-6 text-white">Search</button>
            </div>
            <div class="bg-white p-4 border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
                <div class="p-4 bg-gray-100 text-center rounded-lg space-y-4">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                        alt=" Profile Picture" class="rounded-full">
                    <p class="font-bold">Charles Leclerc</p>
                    <div class="flex items-center justify-between px-4">
                        <p class="text-gray-600"><strong>3.2k</strong><br> Friends</p>
                        <p class="text-gray-600"><strong>44k</strong><br> Posts</p>
                    </div>
                </div>
                <div class="p-4 bg-gray-100 text-center rounded-lg space-y-4">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                        alt=" Profile Picture" class="rounded-full">
                    <p class="font-bold">Lewis Hamilton</p>
                    <div class="flex items-center justify-between px-4">
                        <p class="text-gray-600"><strong>8.9k</strong><br> Friends</p>
                        <p class="text-gray-600"><strong>72k</strong><br> Posts</p>
                    </div>
                </div>
                <div class="p-4 bg-gray-100 text-center rounded-lg space-y-4">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                        alt=" Profile Picture" class="rounded-full">
                    <p class="font-bold">Max Verstappen</p>
                    <div class="flex items-center justify-between px-4">
                        <p class="text-gray-600"><strong>2.1k</strong><br> Friends</p>
                        <p class="text-gray-600"><strong>20k</strong><br> Posts</p>
                    </div>
                </div>
                <div class="p-4 bg-gray-100 text-center rounded-lg space-y-4">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                        alt=" Profile Picture" class="rounded-full">
                    <p class="font-bold">Kimi Raikkonen</p>
                    <div class="flex items-center justify-between px-4">
                        <p class="text-gray-600"><strong>14k</strong><br> Friends</p>
                        <p class="text-gray-600"><strong>12</strong><br> Posts</p>
                    </div>
                </div>
                <div class="p-4 bg-gray-100 text-center rounded-lg space-y-4">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                        alt=" Profile Picture" class="rounded-full">
                    <p class="font-bold">Keanu Reeves</p>
                    <div class="flex items-center justify-between px-4">
                        <p class="text-gray-600"><strong>27k</strong><br> Friends</p>
                        <p class="text-gray-600"><strong>19k</strong><br> Posts</p>
                    </div>
                </div>
            </div>
            <div class="p-4 bg-white border border-gray-200 text-center items-center rounded-lg space-y-4">
                <div class="flex items justify-between py-2">
                    <div class="flex items-center">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
                            alt="Profile Picture" class="h-[40px] rounded-full">
                        <h1 class="font-semibold ml-4">Lewis Hamilton</h1>
                    </div>
                    <div class="flex items-center">
                        <h1>8 seconds ago</h1>
                    </div>
                </div>
                <div class="flex text-lg">
                    <p>2025 here i come</p>
                </div>
                <div class="flex justify-between">
                    <div class="flex items-center space-x-4 pt-2 pb-4">
                        <div class="flex items-center space-x-1 hover:scale-105 duration-300">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-7 hover:fill-red-600 duration-300">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                            </svg>
                            <p class="text-gray-600 hover:text-black duration-300">172k Likes</p>
                        </div>
                        <div class="flex items-center space-x-1 hover:scale-105 duration-300">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-7 hover:fill-blue-500 duration-300">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785A5.969 5.969 0 0 0 6 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337Z" />
                            </svg>
                            <p class="text-gray-600 hover:text-black duration-300">16k Comments</p>
                        </div>
                    </div>
                    <div class="flex items-center hover:scale-125 duration-300">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="size-7">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>
        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow/>
            <Trends/>
        </div>
    </div>
</template>