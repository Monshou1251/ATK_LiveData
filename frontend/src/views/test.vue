// const dataSource2 =  
    //   getAPI.get('datatable/')
    //     .then((response) => {
    //       // debugger
    //       return response.data
    //     })
    /* eslint-disable */
    // let test
    const edit  = (dataSource) => {
      debugger
      editableData[id] = cloneDeep(dataSource.value.filter(item => id === item.id)[0]);
    }
    const editableData = reactive({});
    const Data2 = async () => {
      const a = await getAPI.get('datatable/')
      const dataSource = a.data
      // const edit = id => {
      //   console.log('id: ' + id)
      //   console.log(dataSource)
      //   // dataSource2Data()
      //   console.log(dataSource2)
      //   console.log(Data2)
      //   // dataSource2()
      //   editableData[id] = cloneDeep(dataSource.value.filter(item => id === item.id)[0]);
      // };
      debugger
      edit(dataSource)
      
    }
    /* eslint-enable */

    Data2()