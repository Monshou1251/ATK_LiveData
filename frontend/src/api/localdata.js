import axios from '@/api/axios'

const getData = apiUrl => {
    return axios.get(apiUrl)
}

export default {
    getData
}

