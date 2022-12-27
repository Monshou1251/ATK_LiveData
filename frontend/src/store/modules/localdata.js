import localdataApi from "@/api/localdata"



const state = {
    data: null,
    dataIsLoaded: false,
    dataToDelete: null,
    addedData: [],
    updatedData: [],
    isLoading: false,
    error: null,
    apiUrl: 'CdcConn/',
    deleteDataAllowed: true,
    addDataAllowed: true,
    updateAllowed: true,
    // columns: [],
}

const getters = {
    // columnsWorks (state) {
    //     const columns = ([])
    //     const firstGetAllElement = state.data[0]
    //     const getKeys = Object.keys(firstGetAllElement)
    //     for (const i of getKeys) {
    //         const ff = {
    //           title: i,
    //           dataIndex: i,
    //           key: i,
    //           // width: '31%',
    //         }
    //         columns.push(ff)
    //         };
    //     return columns
    // }
}

const mutations = {
    disableDataDelete (state) {
        state.deleteDataAllowed = false
    },
    enableDataDelete (state) {
        state.deleteDataAllowed = true
    },
    enableDataAdd (state) {
        state.addDataAllowed = true
    },
    disableDataAdd (state) {
        state.addDataAllowed = false
    },
    getDataStart (state) {
        state.isLoading = true
        state.data = null
    },
    getDataSuccess (state, payload) {
        state.isLoading = false
        state.data = payload
    },
    getDataFailure (state) {
        state.isLoading = false
    },
    editDataStart (state) {
        state.isLoading = true
    },
    dataIsLoadedMutation (state) {
        state.dataIsLoaded = true
    },
    editDataSuccess (state, payload) {
        state.isLoading = false
        state.data = payload
    },
    editDataFailure (state) {
        state.isLoading = false
    },
    deleteData (state, payload) {
        const result = state.data.filter(x => !payload.some(y => x.id === y.id))
        state.data = result
        // const selectedId = payload.map(i => i.id)
        state.dataToDelete = payload
    },
    addData (state, payload) {
        // Object.assign(state.data, payload)
        console.log(payload)
        state.addedData.push(payload)
        state.data.push(payload)
        console.log(state.addedData)
    },
    updateData (state, payload) {
        // const dataToUpdate = state.data.filter(x => !payload.some(y => x.id === y.id))
        console.log(payload)
        state.updatedData.push(payload)
        console.log(state.updatedData)
    },
    changeApiUrl (state, Url) {
        state.apiUrl = Url
    }
  
}

const actions = {
    // setData (state, payload) {
    //     state.data = payload
    // }
    getData (context, apiUrl) {
        return new Promise(resolve => {
            context.commit('getDataStart', apiUrl)
            context.commit('changeApiUrl', apiUrl)

            localdataApi
                .getData(apiUrl)
                .then(response => {
                    context.commit('getDataSuccess', response.data)

                    // context.commit('dataIsLoadedMutation')
                    // console.log(response.data)
                    resolve(response.data)
                    // console.log(state.data)
                })
                .catch(() => {
                    context.commit('getDataFailure')
                })
        })
    }
    // getData (context, apiUrl) {
    //     return new Promise(resolve => {
    //         context.commit('getDataStart', apiUrl)
    //         localdataApi
    //             .getData(apiUrl)
    //             .then(response => {
    //                 context.commit('getDataSuccess', response.data)
    //                 resolve(response.data)
    //             })
    //             .catch(() => {
    //                 context.commit('getDataFailure')
    //             })
    //     })
    // }
}

export default {
    state,
    actions,
    mutations,
    getters
}