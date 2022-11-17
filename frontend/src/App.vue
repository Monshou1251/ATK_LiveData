<template>
  <Navbar></Navbar>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'
export default {
  name: 'App',
  components: {
    Navbar,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const access = this.$store.state.auth.access
    if (access) {
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    setInterval(() => {
      console.log('mounted: ' + this.$store.state.auth.access)
      this.getAccess()
    }, 600000)
  },
  methods: {
    getAccess() {
      const accessData = {
        refresh: this.$store.state.auth.refresh,
      }

      axios
        .post('/api/v1/jwt/refresh/', accessData)
        .then((response) => {
          const access = response.data.access

          localStorage.setItem('access', access)
          this.$store.commit('setAccess', access)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-image: url('https://www.toptal.com/designers/subtlepatterns/uploads/stripes-light.png');
  background-size: 150px 150px;
}
</style>
