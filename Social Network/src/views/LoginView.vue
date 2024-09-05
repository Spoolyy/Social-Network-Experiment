<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg space-y-6">
                <h1 id="title" class="text-2xl font-medium">Log</h1>
                <p id="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                <p id="tosignup" class="font-bold">Don't have an account? <router-link to="/signup" class="underline">Sign Up</router-link>
                    here</p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg space-y-6">
                <form class="space-y-6 text-xl">
                    <div class="flex flex-col space-y-2">
                        <label>E-mail</label>
                        <input type="email" placeholder="Insert your E-Mail"
                            class="border border-gray-200 rounded-lg p-2">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label>Password</label>
                        <input type="password" placeholder="Choose a Password"
                            class="border border-gray-200 rounded-lg p-2">
                    </div>
                    
                    <div>
                        <button class="bg-blue-700 text-base py-4 px-6 text-white rounded-lg border border-gray-200"><a
                                href="#">Log In</a></button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>