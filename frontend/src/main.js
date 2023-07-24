import 'element-plus/dist/index.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import ViewUIPlus from 'view-ui-plus'
import 'view-ui-plus/dist/styles/viewuiplus.css'
import API from '@/plugins/axios.js'
import ElementPlus from "element-plus";

const app = createApp(App).use(ViewUIPlus).use(ElementPlus).use(router)

app.mount('#app')

app.config.globalProperties.$axios = API;
app.config.globalProperties.$http = API;
