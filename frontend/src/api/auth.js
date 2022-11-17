import axios from '@/api/axios'

const register = (credentials) => {
  return axios.post('/users/', {user: credentials})
}

const login = credentials => {
  return axios.post('/api/v1/jwt/create/', {user: credentials})
}

export default {
  register,
  login,
}
