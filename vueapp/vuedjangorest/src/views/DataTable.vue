<template>
    <div class="datatable">
    <Navbar></Navbar>
    <div>
        <div class="container">
        <div class="row">
            <div class="col-8 mx-auto mt-5">          
                <table class="table">
                    <thead>
                        <th>Name</th>
                        <th>Surname</th>
                        <th>Date</th>
                    </thead>
                    <tbody>
                        <tr v-for="data in APIData" :key="data.id">
                            <td>{{ data.name }}</td>
                            <td>{{ data.surname }}</td>
                            <td>{{ data.date }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        </div>
        <!-- <div v-for="tables in APIData" :key="tables.id" class="col-md-4">
            <p class="">{{tables.title}}</p>
            <p class="">{{tables.content}}</p> -->

        </div>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar.vue'
    export default {
        name: 'DataTable',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/datatable/')
                .then(response => {
                    console.log('API has received data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>

<style scoped>
</style>