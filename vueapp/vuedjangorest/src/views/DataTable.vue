<template>
  <div id="datatable">
    <div class="container">
      <div class="row">
        <div class="col-9 mx-auto mt-3">
          <div>
            <input
              type="hidden"
              v-model="id"
              class="form-control mt-2"
              placeholder="id"
            />
            <input
              type="text"
              v-model="name"
              class="form-control mt-2"
              placeholder="Name"
            />
            <input
              type="text"
              v-model="surname"
              class="form-control mt-2"
              placeholder="Surname"
            />
            <input
              type="text"
              v-model="date"
              class="form-control mt-2"
              placeholder="Date"
            />
            <button
              @click="createData"
              type="button"
              class="btn btn-success mt-2 mb-2"
            >
              Submit
            </button>
          </div>

          <table
            class="table table-bordered table-hover"
            style="background-color: #fff"
          >
            <thead class="table" style="border: 1px solid DarkGrey">
              <th>id</th>
              <th>Name</th>
              <th>Surname</th>
              <th>Date</th>
              <th>Edit</th>
              <th>Delete</th>
            </thead>
            <tbody>
              <tr v-for="data in APIData" :key="data.id">
                <td style="width: 5%">{{ data.id }}</td>
                <td style="">{{ data.name }}</td>
                <td style="">{{ data.surname }}</td>
                <td style="">{{ data.date }}</td>
                <td style="width: 20px">
                  <button @click="getOne(data)" class="btn bn-sm btn-succes">
                    <i class="fa-regular fa-pen-to-square"></i>
                  </button>
                </td>
                <td style="width: 20px">
                  <button
                    type="button"
                    @click.prevent="deleteOne(data.id)"
                    class="btn bn-sm btn-succes"
                  >
                    <i class="fa-regular fa-trash-can"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getAPI} from '@/api/axios'
export default {
  name: 'DataTable',
  data() {
    return {
      APIData: null,
      id: '',
      name: '',
      surname: '',
      date: '',
      // APIData: [],
    }
  },
  // components: {
  //   Navbar,
  // },
  mounted() {
    this.getAll()
  },

  methods: {
    async getAll() {
      await getAPI
        .get('datatable/', {
          headers: {Authorization: 'JWT ' + localStorage.access},
        })
        .then((response) => {
          this.APIData = response.data
          this.id = ''
          this.name = ''
          this.surname = ''
          this.date = ''
        })
    },
    createData() {
      if (this.id == '') {
        getAPI
          .post('datatable/', {
            id: this.id,
            name: this.name,
            surname: this.surname,
            date: this.date,
          })
          .then(() => {
            console.log('Im just creating new data')
            this.getAll()
          })
      } else {
        const currentData = {
          id: this.id,
          name: this.name,
          surname: this.surname,
          date: this.date,
        }
        getAPI.put('datatable/' + this.id + '/', currentData).then(() => {
          console.log('Now, Im updating the data')
          this.getAll()
        })
      }
    },
    getOne(data) {
      this.id = data.id
      this.name = data.name
      this.surname = data.surname
      this.date = data.date
    },
    deleteOne(id) {
      if (confirm('Delete data with id ' + id + ' ?')) {
        getAPI.delete('datatable/' + id + '/').then(() => {
          console.log('data deleted'), this.getAll()
        })
      }
    },
  },
}
</script>

<style scoped></style>
