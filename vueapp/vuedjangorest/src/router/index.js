import { createRouter, createWebHashHistory } from 'vue-router'
import DataTable from '../views/DataTable.vue'


const routes = [
  {
    path: '/',
    name: 'datatable',
    component: DataTable,
    },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
