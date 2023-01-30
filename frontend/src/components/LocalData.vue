<template>
  <!-- <button @click="deselectRows">deselect rows</button> -->
  <div class="buttonsPos">
    <a-popover placement="top">
      <template #content>
        <p>Add new data</p>
      </template>
      <a-button :disabled=!disableDataAdd class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><PlusOutlined style="display: flex"/></a-button>
    </a-popover>
    <!-- <a-popover placement="top">
      <template #content>
        <p>Copy data</p>
      </template>
      <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><CopyOutlined style="display: flex"/></a-button>
    </a-popover> -->
    <a-popover placement="top">
      <template #content>
        <p>Delete data</p>
      </template>
      <!-- <template> -->
        <a-button :disabled=!disableDeleteButton class="editable-add-btn" style="margin-bottom: 4px"  @click="onDelete"><DeleteOutlined style="display: flex"/></a-button>
      <!-- </template> -->
      <!-- <a-button class="editable-add-btn" style="margin-bottom: 4px"  @click="onDelete"><DeleteOutlined style="display: flex"/></a-button> -->
    </a-popover>
    <a-popover placement="top">
      <template #content>
        <p>Commit data to database</p>
      </template>
      <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="onSubmit"><CheckOutlined style="display: flex"/></a-button>
    </a-popover>
  </div>
  <ag-grid-vue
      style="width: 100%; height: 100%;"
      class="ag-theme-alpine"
      :rowHeight = 30
      :columnDefs="columnDefs"
      @grid-ready="onGridReady"
      :defaultColDef="defaultColDef"
      :rowData="getAll"
      :enableFillHandle="true"
      :rowSelection="rowSelection"
      :enableCellChangeFlash="true"
      :undoRedoCellEditing="true"
      :enableRangeSelection="true"
      :undoRedoCellEditingLimit="10"
      :columnTypes="columnTypes"
      @cell-value-changed="onCellValueChanged"
      @selection-changed="onSelectionChanged"
      >
    </ag-grid-vue>
 </template>



<script>
/* eslint-disable */
import {  defineComponent, onServerPrefetch, onMounted, reactive, watchEffect, ref, unref, toRefs,onUpdated, watch, computed} from 'vue';
import { CheckOutlined, EditOutlined, PlusOutlined, CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { cloneDeep } from 'lodash-es';
import { getAPI } from '@/api/axios'
import { useStore } from 'vuex'
import _ from "lodash";
import { AgGridVue } from "ag-grid-vue3";  // the AG Grid Vue Component
import "ag-grid-community/styles/ag-grid.css"; // Core grid CSS, always needed
import "ag-grid-community/styles/ag-theme-alpine.css"; // Optional theme CSS
import { autoCompleteProps } from 'ant-design-vue/lib/auto-complete';
// import * as agGrid from 'ag-grid-community';
// import 'ag-grid-enterprise';
/* eslint-enable */


export default ({
  name: 'LocalData',
  props: {
    apiUrl: {
        type: String,
        required: true
    }
  },
  components: {
    AgGridVue,
    CheckOutlined,
    PlusOutlined,
    // EditOutlined,
    DeleteOutlined,
  },
  methods: {

  },
  
  async setup(props) {
    const store = useStore()
    store.dispatch('getData', props.apiUrl)
    let getAll = ref(null)
    const gridApi = ref(null)
    const onGridReady = params => {
      gridApi.value = params.api
    }
    let indexAdd = []
    const disableDeleteButton = computed(() => store.state.localdata.deleteDataAllowed)
    const disableDataAdd = computed(() => store.state.localdata.addDataAllowed)
    const apiUrlTest = computed(() => store.state.localdata.apiUrl)
    let columnDefs = ref()
    let rowSelection = 'multiple'
   
    
    
    // DefaultColDef sets props common to all Columns
    const defaultColDef = {
      sortable: true,
      filter: true,
      flex: 1,
      resizable: true,
      editable: true,
      
    };

    const columnTypes = {
      idColumn: { editable: false, maxWidth: 70, resizable: false, headerName: '' },
      nonEditable: {editable: false},
    }

    const deselectRows = () => {
        gridApi.value.deselectAll()
    }

    const validateData = async() => {
      await store.dispatch('getData', props.apiUrl)
      getAll = computed(() => store.state.localdata.data)
      indexAdd = getAll.value.map((item, index) => ({index: ++index, ...item}))
      store.commit('getDataSuccess', indexAdd)
      let getKeys = Object.keys(indexAdd[0])
      // console.log('getKeys: ')
      // console.log(getKeys)

      // columns.value.length = 0
      columnDefs.value = []
      // console.log(columnDefs.value)
      for (const i of getKeys) {
        if (i !== 'id') {
          if (i == 'index') {
              let ff = {
                field: i,
                type: 'idColumn',
                cellStyle: {'background-color': 'rgba(128, 128, 128, 0.060)',
                  'box-shadow': '1px 0px 0px rgba(128, 128, 128, 0.216)'
                },
              }
              columnDefs.value.push(ff)
            } else {
              let ff = {
              field: i,
              cellClassRules: {
                  // apply green to 2008
                  'rag-red': params => params.value === '[null]',
              }
            }
            columnDefs.value.push(ff)
          }
        }
      }
    }


    const handleAdd = (append) => {
      const newStore = getAll.value.slice()
      let newData = []
      for (let i in columnDefs.value) {
        newData.push(columnDefs.value[i]['field'])
      }
      let newDataNull = {}
      for (let z in newData) {
        if (newData[z] == 'index') {
          newData[z] = null
        } else {
          newDataNull[newData[z]] = '[null]'
        }
      }
      console.log(newDataNull)
      if (append) {
          newStore.unshift(newDataNull);
          store.commit('editDataSuccess', newStore)
          store.commit('addData', newDataNull)
          console.log(store.state.localdata.addedData)
        } 
        else {
          newStore.splice(0, 0, newDataNull);
        }
      // validateData()
      console.log(store.state.localdata.addedData)
      // getAll = computed(() => store.state.localdata.data)
    }
    
    let dataWithIndex = []
    let cleanData = []
    const onCellValueChanged = (event) => {
      console.log('data after changes is: ', event.data);
      
      if (event.data['index']) {
        console.log('Data contains Index')
        /* eslint-disable */
        dataWithIndex.push(event.data)
        cleanData = dataWithIndex.map(({ index, ...item }) => item);
        /* eslint-enable */
        console.log(cleanData)
        store.commit('updateData', dataWithIndex)
        console.log(store.state.localdata.updatedData)
        // dataWithIndex = []
      } else {
        console.log('Data has no Index')
        console.log(event.data)
      }
    }

    let dataToDeleteId = []
    let dataToDeleteInDB = []
    const onSelectionChanged = () => {
      const selectedRows = gridApi.value.getSelectedRows();
      dataToDeleteId = selectedRows.map(function (rowNode) {
        return rowNode.id;
      });
      console.log(dataToDeleteId)
      // getAll = getAll.value.filter(function (dataItem) {
      //   return selectedIds.indexOf(dataItem.symbol) < 0;
      // });
    }

    const onDelete = () => {
      dataToDeleteId.forEach(function(id) {
        dataToDeleteInDB.push(id)
      })
      console.log('data stored for submit ', dataToDeleteInDB)
      store.commit('deleteData', dataToDeleteId)
    }

    const onSubmit = () => {
      if (dataToDeleteInDB.length > 0) {
        console.log('Yeehooo, not zero')
        for (let i of dataToDeleteInDB) {
          getAPI.delete(props.apiUrl + i + '/')
          .then(() => {
            console.log('data deleted, id: ' + i)
            dataToDeleteInDB = []
        })}
        validateData()
      } else {
        console.log('Dam, something went wrong bud')
      }

      if (store.state.localdata.updatedData !== null) {
        if (store.state.localdata.updatedData.length > 0) {
          const updatedData = store.state.localdata.updatedData
          for (let i in updatedData) {
            
            getAPI.put(props.apiUrl + updatedData[i]['id'] + '/', updatedData[i])
            .then(() => {
              store.commit('cleanUpdatedData')
            })
          }
          validateData()
          
        }
      }
      
      if (store.state.localdata.addedData !== null) {
        if (store.state.localdata.addedData.length > 0) {
          const dataToAdd = store.state.localdata.addedData
          console.log(dataToAdd)
          for (const i in dataToAdd) {
            getAPI.post(props.apiUrl, dataToAdd[i])
            .then(() => {
              console.log('data added ', dataToAdd)
              store.commit('cleanUpdatedData')
            })
            store.commit('addData', dataToAdd[i])
            // console.log(store.state.localdata.addedData)
          }
          validateData()
          store.commit('cleanUpdatedData')
        }
      }

      

      validateData()
      store.commit('cleanUpdatedData')
    }

    watchEffect(() => validateData())
    await validateData()

    return {
      columnTypes,
      onSelectionChanged,
      onCellValueChanged,
      onDelete,
      handleAdd,
      getAll,
      apiUrlTest,
      gridApi,
      onSubmit,
      disableDeleteButton,
      disableDataAdd,
      onGridReady,
      // updateData,
      columnDefs,
      defaultColDef,
      rowSelection,
      cellWasClicked: (event) => { // Example of consuming Grid Event
        console.log("cell was clicked", event);
      },
      deselectRows,
      // deselectRows: () =>{
      //   gridApi.value.deselectAll()
      // }
    };
  },
});
</script>
<style lang="less">
  .ag-theme-alpine {
    /* disable all borders */
    --ag-borders: solid 1px;
    /* then add back a border between rows */
    --ag-borders-row: dashed 1px;
    --ag-row-border-color: rgba(128, 128, 131, 0.308);
    --ag-cell-horizontal-border: solid 1px rgba(128, 128, 131, 0.288);
    --ag-widget-container-horizontal-padding: 1px;
    --ag-widget-container-vertical-padding: 1px;
  }
  .rag-red {
    color: rgba(128, 128, 128, 0.438);
  }
  .index-background {
    background-color: rgba(128, 128, 128, 0.116);
  }


</style>