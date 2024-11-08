<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg space-y-6">
                <h1 id="title" class="text-2xl font-medium">Sign Up</h1>
                <p id="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                <p id="tologin" class="font-bold">Already have an account? <router-link to="/login" class="underline">Log In</router-link>
                    here</p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg space-y-6">
                <form class="space-y-6 text-xl" v-on:submit.prevent="submitForm">
                    <div class="flex flex-col space-y-2">
                        <label>Name</label>
                        <input v-model="form.name" type="text" placeholder="Your full name" class="border border-gray-200 rounded-lg p-2">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label>E-mail</label>
                        <input v-model="form.email" type="email" placeholder="Your e-mail address"
                            class="border border-gray-200 rounded-lg p-2">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label>Password</label>
                        <input v-model="form.password1" type="password" placeholder="Choose a Password"
                            class="border border-gray-200 rounded-lg p-2">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label>Repeat password</label>
                        <input v-model="form.password2" type="password" placeholder="Repeat your Password"
                            class="border border-gray-200 rounded-lg p-2">
                    </div>
                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>
                    <div>
                        <button class="bg-blue-700 text-base py-4 px-6 text-white rounded-lg border border-gray-200"><a
                                href="#">Sign Up</a></button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast';
export default {
    setup() {
        const toastStore = useToastStore()
        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: []
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response=> {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user ir registed', 'bg-green-300')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data) {
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    },
}
</script>