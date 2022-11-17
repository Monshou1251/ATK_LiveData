import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import SemanticUI from 'semantic-ui-vue';
import 'semantic-ui-css/semantic.min.css';


createApp(App).use(store, SemanticUI).use(router).mount("#app");

// Vue.config.productionTip = false

// new Vue({
//     router,
//     render: h => h(App),
// }).$mount('#app')
