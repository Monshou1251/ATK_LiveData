<template>
  <div>
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please login</h1>
          <!-- <p v-if="incorrectAuth">
            Incorrect username or password entered - please try again
          </p> -->
          <!-- <p>{{ this.data.username }}</p> -->
          <mcv-validation-errors
            v-if="validationErrors"
            :validationErrors="validationErrors"
          />
          <form v-on:submit.prevent="submitForm">
            <div class="form-group mb-2">
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control"
                placeholder="Username"
              />
            </div>
            <div class="form-group mb-2">
              <input
                type="password"
                name="password"
                id="password"
                v-model="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
            <!-- class="btn btn-lg btn-primary btn-block" -->
            <button type="submit" id="loginbutton" :disabled="isSubmitting">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import McvValidationErrors from '@/components/ValidationErrors'
export default {
  name: 'login',
  computed: {
    isSubmitting() {
      return this.$store.state.auth.isSubmitting
    },
  },
  components: {
    McvValidationErrors,
  },

  data() {
    return {
      username: '',
      password: '',
      // incorrectAuth: false,
    }
  },
  methods: {
    submitForm() {
      this.$store.commit('loginStart')
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')

      const formData = {
        username: this.username,
        password: this.password,
      }
      // попробовать получать запрос через api/auth
      axios
        .post('/api/v1/jwt/create/', formData)
        .then((response) => {
          console.log(response)
          // console.log(response.data.refresh)
          const access = response.data.access
          const refresh = response.data.refresh

          this.$store.commit('setAccess', access)
          this.$store.commit('setRefresh', refresh)
          console.log(
            'Submit form, refresh token is stored' +
              this.$store.state.auth.refresh
          )

          axios.defaults.headers.common['Authorization'] = 'JWT ' + access

          localStorage.setItem('access', access)
          localStorage.setItem('refresh', refresh)

          this.$router.push({name: 'home'})
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
  background-color: #f4f4f4;
}
.login {
  background-color: #fff;
  margin-top: 10%;
  box-shadow: 10px 10px 5px #aaaaaa;
  border-radius: 5px;
}
input {
  padding: 25px 10px;
}

#loginbutton {
  height: 40px;
  color: hwb(0 100% 0%);
  width: 70px;
  margin-bottom: 0;
  background-color: rgba(0, 136, 169, 1);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease 0s;
  border-radius: 5px;
  font-weight: 600;
  box-shadow: 1px 1px 3px #aaaaaa;
}

#loginbutton:disabled,
#loginbutton[disabled] {
  border: 1px solid #999999;
  background-color: #cccccc;
  color: #666666;
}

#loginbutton:hover {
  background-color: rgba(0, 136, 169, 0.7);
}
</style>
