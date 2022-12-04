<template>
    <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><PlusOutlined style="display: flex"/></a-button>
        <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><CopyOutlined style="display: flex"/></a-button>
        <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><DeleteOutlined style="display: flex"/></a-button>
        <a-table bordered :data-source="dataSource2" :columns="columns">
          <template #bodyCell="{ column, text, record }">
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
                  {{ text || ' ' }}
                  <edit-outlined class="editable-cell-icon" @click="edit(record.id)" />
                </div>
              </div>
            </template>

            <template v-if="column.dataIndex === 'date'">
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
            </template>

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

import {  defineComponent, onMounted, reactive, ref, watch} from 'vue';
import { CheckOutlined, EditOutlined, PlusOutlined, CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { cloneDeep } from 'lodash-es';
import {getAPI} from '@/api/axios'
import { useStore } from 'vuex'
// import { watch } from 'fs';
export default defineComponent({
  name: 'LocalData',
  props: {
    apiUrl: {
        type: String,
        required: true
    }
  },
  methods: {
    onDelete(key) {
      getAPI.delete('datatable/' + key)
      .then(() => {
        console.log('data deleted'), this.getAll()
      })
    },

    handleAdd () {
      const newData = {
        // id: '',
        name: 'default',
        surname: 'default',
        date: 'default',
      };
      getAPI
          .post('datatable/', 
            newData
          )
          .then(() => {
            console.log('New data created')
            this.getAll()
          })
    },
  },
  components: {
    CheckOutlined,
    PlusOutlined,
    EditOutlined,
    DeleteOutlined,
    CopyOutlined,
  },
  setup() {
    const columns = [{
      title: 'id',
      dataIndex: 'id',
      key: 'id',
      width: '5%',
    }, {
      title: 'name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'surname',
      dataIndex: 'surname',
      key: 'surname',
    }, {
      title: 'date',
      dataIndex: 'date',
      key: 'date',
    }, {
      title: 'operation',
      dataIndex: 'operation',
      key: 'operation',
    }];

    const store = useStore()

    const editableData = reactive({});

    const dataSource2 = ref([])
    const save = async(key) => {
      const dataToReplace = dataSource2.value.find(item => item.id == key)
      // Object.assign(dataToReplace, dataSource2[key])
      
      Object.assign(dataToReplace, editableData[key]);
      getAPI.put('datatable/' + key + '/', dataToReplace)
      console.log(dataToReplace)
      delete editableData[key];
    };

    const getAll = async () => {
      store.commit('getDataStart')
      await getAPI
        .get('datatable/')
        .then((response) => {
          console.log(response.data)
          dataSource2.value = response.data
          console.log(dataSource2)
        })
    }
    const edit = key => {
      store.commit('getDataStart')
      console.log('id: ' + key) 
      console.log(dataSource2.value.find(item => item.id == 1))
      editableData[key] = cloneDeep(dataSource2.value.find(item => item.id == key))
    };
    onMounted(() => {
      getAll()
      console.log('onMounted into setup works')
      })

    watch(dataSource2)
    
    return {
      columns,
      // onDelete,
      // handleAdd,
      dataSource2,
      getAll,
      editableData,
      edit,
      save,
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