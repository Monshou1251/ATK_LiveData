// import localdataApi from "@/api/localdata"

const state = {
    data: null,
    isLoading: false,
    error: null,
}

const mutations = {

    getDataStart (state) {
        state.isLoading = !true
    }
    // [mutationTypes.getDataStart](state) {
    //     state.isLoading = true
    //     state.data = null
    // },
    // [mutationTypes.getDataSuccess](state, payload) {
    //     state.isLoading = false
    //     state.data = payload
    // },
    // [mutationTypes.getDataFailure](state) {
    //     state.isLoading = false
    // }
}

const actions = {
    // [actionTypes.getData](context, {apiUrl}) {
    //     return new Promise(resolve => {
    //         context.commit(mutationTypes.getDataStart, apiUrl)
    //         localdataApi
    //             .getData(apiUrl)
    //             .then(response => {
    //                 context.commit(mutationTypes.getDataSuccess, response.data)
    //                 resolve(response.data)
    //             })
    //             .catch(() => {
    //                 context.commit(mutationTypes.getDataFailure)
    //             })
    //     })
    // }
}

export default {
    state,
    actions,
    mutations
}