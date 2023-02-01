<template>
  <div class="grid-container">
      <div class="grid-item1">
        <Navbar2></Navbar2>
      </div>
      <div class="grid-item2">
        <Sidebar></Sidebar>
      </div>
      <div class="grid-item3">
        <SearchField></SearchField>
      </div>
      <div class="grid-item4">
        Item-4
        <!-- <step-backward-filled />
        <sliders-filled /> -->
      </div>
      <div class="grid-item5">
        <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><PlusOutlined style="display: flex"/></a-button>
        <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><CopyOutlined style="display: flex"/></a-button>
        <a-button class="editable-add-btn" style="margin-bottom: 4px" @click="handleAdd"><DeleteOutlined style="display: flex"/></a-button>
        <a-table bordered :data-source="APIData" :columns="columns">
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
                v-if="dataSource.length"
                title="Sure to delete?"
                @confirm="onDelete(record.id)"
              >
                <a>Delete</a>
              </a-popconfirm>
            </template>
          </template>
        </a-table>
      </div>
      <div class="grid-item6">
        Item-6
      </div>
      <div class="grid-item7">
        Item-7
      </div>
    <!-- </div> -->
  </div>
  
</template>
<script>

import {  defineComponent, reactive, ref, onMounted } from 'vue';
import { CheckOutlined, EditOutlined, PlusOutlined, CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { cloneDeep } from 'lodash-es';
import Navbar2 from '@/components/Navbar2.vue'
import Sidebar from '@/components/Sidebar.vue'
import SearchField from '@/components/SearchField.vue'
import {getAPI} from '@/api/axios'
export default defineComponent({
  name: 'DataTableElement',
  data() {
    return {
      APIData: null,
      id: '',
      conn_type: '',
      conn_name: '',
    }
  },
  mounted() {
    this.getAll()
  },
  methods: {
    async getAll() {
      await getAPI
        .get('CdcConn/')
        .then((response) => {
          this.APIData = response.data
          this.id = ''
          this.name = ''
          this.surname = ''
          this.date = ''
        })
    },

    onDelete(key) {
      getAPI.delete('CdcConn/' + key)
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
          .post('CdcConn/', 
            newData
          )
          .then(() => {
            console.log('New data created')
            this.getAll()
          })
    },
    // editableData = reactive({}),
    // edit (id) {
    //   console.log(id)
    //   this.editableData[id] = cloneDeep(this.APIData.id);
    // },
  },
  components: {
    CheckOutlined,
    PlusOutlined,
    EditOutlined,
    DeleteOutlined,
    CopyOutlined,
    Sidebar,
    SearchField,
    Navbar2,
  },
  setup() {
    const columns = [
    //   {
    //   title: 'id',
    //   dataIndex: 'id',
    //   key: 'id',
    //   width: '5%',
    // }, 
    {
      title: 'conn_type',
      dataIndex: 'conn_type',
      key: 'conn_type',
    },
    {
      title: 'conn_name',
      dataIndex: 'conn_name',
      key: 'conn_name',
    }, 
    // {
    //   title: 'date',
    //   dataIndex: 'date',
    //   key: 'date',
    // },
    //  {
    //   title: 'operation',
    //   dataIndex: 'operation',
    //   key: 'operation',
    // }
  ];

    const UpdateApi = async () => {
      getAPI.get('CdcConn/')
    }

    onMounted(UpdateApi)

    const dataSource = ref([{
      key: '0',
      name: 'Edward King 0',
      age: 32,
      address: 'London, Park Lane no. 0',
    }, {
      key: '1',
      name: 'Edward King 1',
      age: 32,
      address: 'London, Park Lane no. 1',
    }]);

    const editableData = reactive({});
    const edit = async(key) => {
      console.log('id: ' + key)
      const dataSource2 = await getAPI.get('CdcConn/')
      const insertData = dataSource2.data    
      console.log(insertData.find(item => item.id == 1))
      editableData[key] = cloneDeep(insertData.find(item => item.id == key));
    };
    const save = async(key) => {
      const dataSource2 = await getAPI.get('CdcConn/')
      const insertData = dataSource2.data
      console.log(insertData.find(item => item.id == key))
      console.log(editableData[key])
      console.log(key)
      Object.assign(insertData.find(item => item.id == key), editableData[key]);
      console.log(insertData.find(item => item.id == key))
      await getAPI.put('CdcConn/' + key + '/', editableData[key]).then(() => {
          console.log('Now, Im updating the data')
          
        })
      UpdateApi
      delete editableData[key];
    };

    
    return {
      columns,
      // onDelete,
      // handleAdd,
      dataSource,
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


.grid-container {
  display: grid;
  grid-template-columns: max-content auto minmax(150px, 200px);
  grid-template-rows: 40px 40px auto 40px;
  height: 100vh;
  width: 100%;
  // border: 2px solid rgb(197, 56, 21);
  gap: 2px
}

.grid-item {
  // border: 5px solid rgb(73, 100, 0);
}

// Navbar
.grid-item1 {
  /* position: fixed; */
  grid-column: 1/4;
  grid-row: 1/2;
  // background-color: rgba(165, 42, 42, 0.336);
}

// Sidebar
.grid-item2 {
  grid-column: 1/2;
  grid-row: 2/4;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
}

// SearchField
.grid-item3 {
  grid-column: 2/3;
  grid-row: 2/3;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
  display: block;
  padding: 3px;
}

.grid-item4 {
  grid-column: 3/4;
  grid-row: 2/3;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
}

.grid-item5 {
  padding: 5px;
  grid-column: 2/3;
  grid-row: 3/4;
  background-color: rgba(90, 85, 86, 0.075);
}

.grid-item6 {
  grid-column: 3/4;
  grid-row: 3/4;
  background-color: white;
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.185);
}

.grid-item7 {
  grid-column: 1/4;
  grid-row: 4/5;
  // background-color: rgba(142, 165, 42, 0.336);
}




</style>