import {createRouter, createWebHashHistory} from 'vue-router'
import DataTable from '@/views/DataTable'
import DataSemantic from '@/views/DataSemantic'
import HomeView from '@/views/HomeView'
// import Register from '@/views/Register'
import Login from '@/views/Login'
import Logout from '@/views/Logout'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
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
    path: '/datasemantic',
    name: 'datasemantic',
    component: DataSemantic,
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
