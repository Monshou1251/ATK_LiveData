<template>
  <div class="auth-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-6 offset-md-3 col-xs-12">
          <h1 class="text-xs-center">Sign in</h1>
          <p class="text-xs-center">
            <router-link to="{ name: 'register' }">
              Need an account?
            </router-link>
          </p>
          <!-- создаем новый props validation-errors -->
          <!-- этот props создаются в ValidationError.vue -->
          <mcv-validation-errors
            v-if="validationErrors"
            :validationErrors="validationErrors"
          />
          <form @submit.prevent="onSubmit">
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="text"
                placeholder="Email"
                v-model="email"
              />
            </fieldset>
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="password"
                placeholder="Password"
                v-model="password"
              />
            </fieldset>
            <button
              class="btn btn-lg btn-primary pull-xs-right"
              :disabled="isSubmitting"
            >
              Sign In
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import McvValidationErrors from '@/components/ValidationErrors'
import {actionTypes} from '@/backlog/auth'

export default {
  name: 'McvLogin',
  components: {
    McvValidationErrors,
  },
  data() {
    return {
      email: '',
      password: '',
    }
  },
  computed: {
    // три точки это spread, кажде знач. из обьекта засовывает внутрь компутед
    ...mapState({
      isSubmitting: (state) => state.auth.isSubmitting,
      validationErrors: (state) => state.auth.validationErrors,
    }),

    // isSubmitting() {
    //   return this.$store.state.auth.isSubmitting
    // },
    // validationErrors() {
    //   return this.$store.state.auth.validationErrors
    // },
  },
  methods: {
    onSubmit() {
      console.log('submitted form')
      this.$store
        // register это название жкшена
        .dispatch(actionTypes.login, {
          email: this.email,
          password: this.password,
        })
        .then(() => {
          this.$router.push({name: 'home'})
          // router мы подключили во vue в файле main.js
        })
      // мутации мы коммитим, а экшены диспатчим
      // register это наш action
    },
  },
}
</script>
