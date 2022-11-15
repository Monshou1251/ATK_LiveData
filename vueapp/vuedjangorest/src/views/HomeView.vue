<template>
  <Navbar></Navbar>
  <div class="home">
    <h1>Home page</h1>
    <span :src="user_data">Logged in user: {{ user_data }}</span>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      user_data: '',
    }
  },
  components: {},
  mounted() {
    this.getMe()
  },
  methods: {
    getMe() {
      axios
        .get('/api/v1/users/me', {
          headers: {Authorization: 'JWT ' + localStorage.access},
        })
        .then((response) => {
          console.log(response)
          console.log(
            'getMe, refresh token is  ' + this.$store.state.auth.access
          )
          this.user_data = response.data.username
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
