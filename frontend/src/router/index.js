import {createRouter, createWebHashHistory} from 'vue-router'
import DataTable from '@/views/DataTable'
import DataTableElement from '@/views/DataTableElement'
import ETable from '@/views/ETable'
// import HomeView from '@/views/HomeView'
import GlobalData from '@/views/GlobalData'

// import Register from '@/views/Register'
import Login from '@/views/Login'
import Logout from '@/views/Logout'

const routes = [
  {
    path: '/',
    name: 'globalData',
    component: GlobalData,
  },
  // {
  //   path: '/register',
  //   name: 'register',
  //   component: Register,
  // },
  {
    path: '/datatable',
    name: 'datatable',
    component: DataTable,
  },
  {
    path: '/datatableelement',
    name: 'datatableelement',
    component: DataTableElement,
  },
  {
    path: '/etable',
    name: 'etable',
    component: ETable,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
