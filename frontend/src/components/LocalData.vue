<template>
    <a-popover placement="top">
      <template #content>
        <p>Add new data</p>
      </template>
      <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><PlusOutlined style="display: flex"/></a-button>
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
      <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="onDelete"><DeleteOutlined style="display: flex"/></a-button>
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
          rowKey="id"
          :row-selection="rowSelection"
          :data-source="getAll"
          :columns="columns"
          :pagination="{ pageSize: 15 }">
          
          <template #bodyCell="{ column, text, record, }">
            <template v-if="column.dataIndex === 'index'">
                {{ getAll.findIndex(i => i == (getAll.find(i => i.id === record.id))) + 1 }}
            </template>

            <template v-if="column.dataIndex === 'id' ">
              <div class="editable-cell">
                <div v-if="editableData[record.id]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.id].id" @pressEnter="save(record.id)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.id)" />
                </div>
                <div v-else class="editable-cell-text-wrapper">
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.id)" />
                </div>
              </div>
            </template>

            <template v-if="column.dataIndex === 'name'">
              <div class="editable-cell">
                <div v-if="editableData[record.id]" class="editable-cell-input-wrapper">
                  <a-input v-model:value="editableData[record.id].name" @pressEnter="save(record.id)" />
                  <check-outlined class="editable-cell-icon-check" @click="save(record.id)" />
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
            </template>

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
import {  defineComponent, onMounted, reactive, ref, toRefs, onBeforeUpdate, computed} from 'vue';
import { CheckOutlined, EditOutlined, PlusOutlined, CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { cloneDeep } from 'lodash-es';
import {getAPI} from '@/api/axios'
import { useStore } from 'vuex'
// import { Table } from 'ant-design-vue';
// import { watch } from 'fs';
/* eslint-enable */
export default defineComponent({
  name: 'LocalData',
  props: {
    apiUrl: {
        type: String,
        required: true
    }
  },
  methods: {
  },
  components: {
    CheckOutlined,
    PlusOutlined,
    EditOutlined,
    DeleteOutlined,
    // CopyOutlined,
  },
  setup(props) {
    const store = useStore()
   

    // const getAll = ref([])
    // store.dispatch('getData', {apiUrl: props.apiUrl})
    // e shallowRef() instead.
    const getAll = reactive(computed(() => store.state.localdata.data))
    
    // const dataConverted = (getAll) => {
    //   return _.cloneDeep(getAll);
    // }
    // const plainObject = { ...getAll };
    // console.log(plainObject)

    const columns = [
    {
      title: '#',
      dataIndex: 'index',
      key: 'index',
      width: '2%',
      align: 'center',
    }, 
    {
      title: 'id',
      dataIndex: 'id',
      key: 'id',
      width: '8%',
      align: 'center',
    }, {
      title: 'name',
      dataIndex: 'name',
      key: 'name',
      width: '31%',
    },
    {
      title: 'surname',
      dataIndex: 'surname',
      key: 'surname',
      width: '31%',
    }, {
      title: 'date',
      dataIndex: 'date',
      key: 'date',
    },
  ];
    
    
    // const kek = ['afaf', 'ffff', 1]
    // console.log(kek.findIndex(i => i == 'afaf'))
   
    // const kek = [{id: 1, name: 'Boba'}, {id: 2, name: 'Boba2'}, {id: 22, name: 'Boba3'}]
    // const findKek = kek.find(i => i.name === 'Boba2')
    // const IndexKek = kek.findIndex(i => i == (findKek))
    // console.log(findKek)
    // console.log(IndexKek)


    

    const editableData = reactive({});

    const dataSource2 = ref([])

    

    // const getData = computed(() => sto)

    // const products = computed(() => store.state.products.all)
    // const addProductToCart = (product) => store.dispatch('cart/addProductToCart', product)
    // store.dispatch('products/getAllProducts')

    // const getAll = async () => {
    //   store.commit('getDataStart')
    //   // store.commit('getDataSuccess')
    //   console.log(props)
    //   // store.dispatch('getData')
    //   await getAPI
    //     .get(props.apiUrl)
    //     .then((response) => {

    //       // console.log(response.data)
    //       dataSource2.value = response.data
    //       this.state.commit('setData', response.data)
    //       console.log(store.data)
    //       console.log(dataSource2)
    //     })
    // }
    
    let selectedObject = []

    const rowSelection = {
      onChange: (selectedRowKeys, selectedRows) => {
        console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
        console.log(selectedRowKeys)
        selectedObject = store.state.localdata.data.filter(d => selectedRowKeys.find(key => key === d.id))
        console.log(selectedObject)
      }
    };

    


    const edit = key => {
      store.commit('editDataStart')
      editableData[key] = cloneDeep(store.state.localdata.data.find(item => item.id == key))
    };

    const save = (key) => {
      const dataToReplace = store.state.localdata.data.find(item => item.id == key)
      console.log(dataToReplace)
      Object.assign(dataToReplace, editableData[key]);
      console.log(editableData[key])
      // getAPI.put('datatable/' + key + '/', dataToReplace)
      //   .then(() => {
      //     store.commit('editDataSuccess')
      //   })
      store.commit('updateData', editableData[key])
      // console.log(dataToReplace)
      // console.log(getAll.value)
      delete editableData[key];
    };

    const handleAdd = () => {
      const newData = {
        id: '',
        name: '',
        surname: '',
        // date: '',
      }

      // getAll.value.push(newData)
      // {{ getAll.findIndex(i => i == (getAll.find(i => i.id === record.id))) + 1 }}
      store.commit('addData', newData)
      // const index = store.state.localdata.data.findIndex(i => i == (store.state.localdata.data.find(i => i.name === newData.name))) + 1
      // console.log(index)
      edit(newData.id)
      console.log(newData)
      console.log(getAll)
      
      // console.log("111 " + getAll.value)
      
      // getAPI
      //     .post('datatable/', 
      //       newData
      //     )
      //     .then(() => {
      //       console.log('New data created')
      //       // getAll()
      //     })
    }


    const onDelete = () => {
      const dataToDelete = store.state.localdata.dataToDelete
      console.log(selectedObject)
      store.commit('deleteData', selectedObject)
      console.log(store.state.localdata.data)
      console.log('_____________')
      console.log(dataToDelete)
      console.log('_____________')
    }

    const onSubmit = () => {
      if (store.state.localdata.dataToDelete != null) {
        console.log('Yeehooo, not zero')
        const dataToDeleteId = store.state.localdata.dataToDelete.map(i => i.id)
        console.log(dataToDeleteId)
        for (const i of dataToDeleteId) {
          getAPI.delete('datatable/' + i + '/')
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
          getAPI.post('datatable/', dataToAdd[y])
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
        getAPI.put('datatable/' + z.id + '/', z)
        .then(() => {
          console.log('data added' + z.id)
        })
        }
      } else {
        console.log('updatedData is empty')
      }
    }

  onMounted(() => {
    store.dispatch('getData', {apiUrl: props.apiUrl})
    store.state.localdata.data

    // console.log(store.state.localdata.data)
    // console.log(getAll.data)
    console.log('Im mounted')
    })

    
    return {
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