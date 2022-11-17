import axios from 'axios'

const getAPI = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
})

axios.defaults.baseURL = 'http://127.0.0.1:8000/'


export {getAPI}
export default axios
