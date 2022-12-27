<template>
    
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
    <!-- <a-space align="center" style="margin-bottom: 16px">
    CheckStrictly:
    <a-switch v-model:checked="rowSelection.checkStrictly"></a-switch>
    </a-space> -->
        <a-table
          size=small
          bordered
          rowKey = 'index'
          :row-selection="rowSelection"
          :data-source="getAll"
          :columns="columns"
          :pagination="{ pageSize: 15 }">
          
          <template #bodyCell="{ column, text, record }">
            <!-- <template v-if="column.dataIndex === 'index'">
                {{ getAll.findIndex(i => i == (getAll.find(i => i.conn_type === record.conn_type))) + 1 }}
            </template> -->

            <template v-if="column.dataIndex == 'target_field_name'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].target_field_name" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template>
            <template v-if="column.dataIndex == 'conn_type'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].conn_type" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template>
            <template v-if="column.dataIndex == 'last_read_seq'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].last_read_seq" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template>
            <template v-if="column.dataIndex == 'conn_name'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].conn_name" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template>
            <template v-if="column.dataIndex  == 'required'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].required" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template>
            <!-- {{ columns }} -->
            <!-- <template v-if="columns.includes('conn_type')">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.index].required" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.index)" />
                </div>
              </div>
            </template> -->

            <!-- <template v-if="column.dataIndex === 'name'">
              <div class="editable-cell">
                <div v-if="editableData[record.index]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.id].index" @pressEnter="save(record.index)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.index)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.id)" />
                </div>
              </div>
            </template>

            <template v-if="column.dataIndex === 'surname'">
              <div class="editable-cell">
                <div v-if="editableData[record.id]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.id].surname" @pressEnter="save(record.id)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.id)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || '' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.id)" />
                </div>
              </div>
            </template> -->
            <!-- <template v-if="column.dataIndex === 'date'">
              <div class="editable-cell">
                <div v-if="editableData[record.id]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.id].date" @pressEnter="save(record.id)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.id)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.id)" />
                </div>
              </div>
            </template> -->

            <template v-else-if="column.dataIndex === 'operation'">
              <a-popconfirm
                
                title="Sure to delete?"
                @confirm="onDelete(record.id)"
              >
                <a>Delete</a>
              </a-popconfirm>
            </template>
          </template>
        </a-table>    
</template>


<script>
/* eslint-disable */
import {  defineComponent, onMounted, reactive, watchEffect, ref, unref, toRefs,onUpdated, watch, onRenderTriggered, onBeforeUnmount, onBeforeMount, onBeforeUpdate, computed} from 'vue';
import { CheckOutlined, EditOutlined, PlusOutlined, CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { cloneDeep } from 'lodash-es';
import { getAPI } from '@/api/axios'
import { useStore } from 'vuex'
/* eslint-enable */


export default ({
  name: 'CdcConn',
  props: {
    apiUrl: {
        type: String,
        required: true
    }
  },
  // methods:{
  // 	filter(nationality){
  //   // We can't find 'Taiwan' in nationalityArr
  //  return this.nationalityArr.filter(n=>n===nationality).length===0?false:true; // false
  //  }
  // },
  components: {
    CheckOutlined,
    PlusOutlined,
    EditOutlined,
    DeleteOutlined,
    // CopyOutlined,
  },
  async setup(props) {
    // console.log('apiUrl is equal to: ' + props.apiUrl)
    const store = useStore()
    const disableDeleteButton = computed(() => store.state.localdata.deleteDataAllowed)
    const disableDataAdd = computed(() => store.state.localdata.addDataAllowed)
    // const disableButton = true
    // const disableButton = store.commit('disableDelete')
    store.commit('changeApiUrl', props.apiUrl)
    console.log(store.state.localdata.apiUrl)
    let columns = reactive([])
    let getAll = reactive([])
    watch(() => store.state.localdata.apiUrl, (newUrl, oldUrl) => {
      // console.log('newUrl', newUrl)
      console.log('oldUrl', oldUrl)
      store.dispatch('getData', newUrl)
      .then(() => {store.commit('changeApiUrl', newUrl)
      })
      .then(() => {
        getAll = computed(() => store.state.localdata.data)
        console.log(getAll)
        // let getAllString = JSON.parse(JSON.stringify(getAll.value))
        let getAllString = getAll.value
        let arr = getAllString.map((item, index) => ({index: ++index, ...item}))

        getAll = arr
        store.commit('getDataSuccess', getAll)
        const firstGetAllElement = getAll[0]
        let getKeys = Object.keys(firstGetAllElement)
        // columns.splice(0, (columns.length))
        columns.length = 0
        for (const i of getKeys) {
          const ff = {
            title: i,
            dataIndex: i,
            key: i,
          }
          columns.push(ff)
        
        }
        console.log('this comes COLUMNS from watch:')
        console.log(columns)
        const blop = {"width" : "1%"}
        // Object.assign(insertData.find(item => item.id == key), editableData[key]);
        Object.assign(columns.find(i => i.title === "index"), blop);
        console.log(columns)
      })
    })

    await store.dispatch('getData', props.apiUrl)
    .then(() => {store.commit('changeApiUrl', props.apiUrl)})
    .then(() => {
      getAll = computed(() => store.state.localdata.data)
    })
    let kek = reactive(getAll.value.map((item, index) => ({index: ++index, ...item})))
      let firstGetAllElement = kek[0]
      let getKeys = Object.keys(firstGetAllElement)
      for (const i of getKeys) {
        const ff = {
          title: i,
          dataIndex: i,
          key: i,
        }
        columns.push(ff)
        const blop = {"width" : "1%"}
        // Object.assign(insertData.find(item => item.id == key), editableData[key]);
        Object.assign(columns.find(i => i.title === "index"), blop);
      }
    
    const editableData = reactive({});
    const dataSource2 = ref([])
    let selectedObject = []

    const rowSelection = {
      onChange: (selectedRowKeys, selectedRows) => {
        console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
        console.log(selectedRowKeys)
        // const selectedObject2 = getAll.value
        selectedObject = getAll.filter(d => selectedRowKeys.find(key => key === d.index))
        console.log(selectedObject)
      }
    };

    const edit = index => {
      store.commit('editDataStart')
      console.log(index)
      editableData[index] = cloneDeep(getAll.filter(item => index === item.index)[0])
      console.log(editableData)
      // editableData[index] = cloneDeep(getAll.find(item => item.index === index))
    };

    const save = (key) => {
      const dataToReplace = getAll.find(item => item.index == key)
      console.log(dataToReplace)
      Object.assign(dataToReplace, editableData[key]);
      console.log(editableData[key])
      store.commit('updateData', editableData[key])
      delete editableData[key];
    };

    const handleAdd = () => {
      const newData = {
        id: '',
        name: '',
        surname: '',
        // date: '',
      }
      store.commit('addData', newData)
      edit(newData.id)
      console.log(newData)
      console.log(getAll)
    }


    const onDelete = () => {
      console.log(store.state.localdata.data)
      const dataToDelete = store.state.localdata.dataToDelete
      console.log(selectedObject)
      store.commit('deleteData', selectedObject)
      console.log(dataToDelete)
    }

    const onSubmit = () => {
      if (store.state.localdata.dataToDelete != null) {
        console.log('Yeehooo, not zero')
        const dataToDeleteId = store.state.localdata.dataToDelete.map(i => i.id)
        console.log(dataToDeleteId)
        for (const i of dataToDeleteId) {
          getAPI.delete(props.apiUrl + i + '/')
          .then(() => {
            console.log('data deleted, id: ' + i)
        })}
      } else {
        console.log('Dam, something went wrong bud')
      }
      if (store.state.localdata.addedData.length > 0) {
        console.log('Hippito Hoppiti women are property')
        // console.log(store.state.localdata.addedData)
        const dataToAdd = store.state.localdata.addedData
        console.log(dataToAdd)
        for (const y in dataToAdd) {
          console.log(dataToAdd[y])
          getAPI.post('CdcConn/', dataToAdd[y])
          .then(() => {
            console.log('data added' + y)
          })
        }
      } else {
        console.log('addedData is empty')
      }
      if (store.state.localdata.updatedData.length > 0) {
        const updatedData = store.state.localdata.updatedData
        console.log('updatedData is not empty!')
        for (const z of updatedData) {
        console.log(z.id)
        getAPI.put('CdcConn/' + z.id + '/', z)
        .then(() => {
          console.log('data added' + z.id)
        })
        }
      } else {
        console.log('updatedData is empty')
      }
    }

    // onMounted(() => {
      // store.dispatch('getData', props.apiUrl).then(() => {
      //   console.log('data received: ', store.state.localdata.data)
      //   getAll = store.state.localdata.data
      // })
      // store.state.localdata.data
      // getAll
      // console.log('that getAll comes from onMounted' + getAll)
      // console.log('Im mounted')
      // console.log(props.apiUrl + ' this comes from onMounted LocalData')
      // })
    
    return {
      // getData: () => store.dispatch('getData', props.apiUrl),
      rowSelection,
      columns,
      onDelete,
      handleAdd,
      dataSource2,
      getAll,
      editableData,
      edit,
      save,
      onSubmit,
      disableDeleteButton,
      disableDataAdd
    };
  },
});
</script>
<style lang="less">
.editable-cell {
  position: relative;
  .editable-cell-input-wrapper,
  .editable-cell-text-wrapper {
    padding-right: 24px;
  }

  .editable-cell-text-wrapper {
    padding: 5px 24px 5px 5px;
  }

  .editable-cell-icon,
  .editable-cell-icon-check {
    position: absolute;
    right: 0;
    width: 20px;
    cursor: pointer;
  }

  .editable-cell-icon {
    margin-top: 4px;
    display: none;
  }

  .editable-cell-icon-check {
    line-height: 28px;
  }

  .editable-cell-icon:hover,
  .editable-cell-icon-check:hover {
    color: #030c13;
  }

  .editable-add-btn {
    margin-bottom: 8px;
  }
}

.editable-cell:hover .editable-cell-icon {
  color: #030c13;
  display: inline-block;
}

</style>