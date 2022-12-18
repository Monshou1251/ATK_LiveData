import {createStore} from 'vuex'
// import Vuex from "vuex";
// import Vue from "vue";
import auth from '@/store/modules/auth'
import localdata from '@/store/modules/localdata'

// Vue.use(Vuex)

export default createStore({
  // namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    localdata
  },
})
