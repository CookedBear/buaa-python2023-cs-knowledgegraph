import 'element-plus/dist/index.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ViewUIPlus from 'view-ui-plus'
import 'view-ui-plus/dist/styles/viewuiplus.css'

const app = createApp(App).use(ViewUIPlus)

app.use(router)

app.mount('#app')
