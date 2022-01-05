import axios from "./plugins/axios"
import { createApp } from 'vue'
import App from './App.vue'
import {$axios} from "./plugins/axios"


import 'bootstrap/dist/css/bootstrap.css'
import router from './router'
import store from './store'
import i18n from './i18n'

$axios.get('account/me/').then(r => {
    if (r.data.user){
    store.commit('profile',r.data.user)
    }
}).finally(() =>{
    // setTimeout(() =>{
    //     const app = createApp(App).use(i18n).use(store).use(router).use(axios)
    //     app.mount('#app')
    // },200);
})

const app = createApp(App).use(i18n).use(store).use(router).use(axios)
app.mount('#app')