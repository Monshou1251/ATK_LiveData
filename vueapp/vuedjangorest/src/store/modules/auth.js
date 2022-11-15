// import authApi from '@/api/auth'
// import {setItem} from '@/helpers/persistanceStorage'


// import { getAPI } from "@/api/axios"

const state = {
  access: '',
  refresh: '',
  isSubmitting: false,
  currentUser: null,
  validationErrors: null,
  isLoggedIn: null,

}

export const mutationTypes = {
  loginStart: '[auth] loginStart',
  loginSuccess: '[auth] loginSuccess',
  loginFailure: '[auth] loginFailure',
}

export const actionTypes = {
  login: '[auth] login'
}

const mutations = {
  initializeStore(state) {
    if (localStorage.getItem("access")) {
      state.access = localStorage.getItem("access")
      state.refresh = localStorage.getItem("refresh")
    } else {
      state.access = ''
      state.refresh = ''
    }
  },
  [mutationTypes.loginStart](state) {
    state.isSubmitting = true
    state.validationErrors = null
  },
  [mutationTypes.loginSuccess](state, payload) {
    state.isSubmitting = false
    state.currentUser = payload
    state.isLoggedIn = true
  },
  [mutationTypes.loginFailure](state, payload) {
    state.isSubmitting = true
    state.validationErrors = payload
  },

  
  setAccess(state, access) {
    state.access = access
  },
  setRefresh(state, refresh) {
    state.refresh = refresh
  }
}

// const actions {

// }
const actions = {
  // [actionTypes.login](context, credentials) {
  //   return new Promise(resolve => {
  //     context.commit(mutationTypes.loginStart)
  //     authApi
  //       .login(credentials)
  //       .then(response => {
  //         context.commit(mutationTypes.loginSuccess, response.data.user)
  //         setItem('accessToken', response.data.user.token)
  //         resolve(response.data.user)
  //       })
  //       .catch(result => {
  //         context.commit(
  //           mutationTypes.loginFailure,
  //           result.response.data.errors
  //         )
  //       })
  //   })
  // }
}


export default {
  state,
  mutations,
  actions,
}
