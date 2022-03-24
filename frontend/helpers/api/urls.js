import axios from 'axios'

export default {
    async getExercicios() {
        let response = await axios.get('http://localhost:8000/exercise/list')
        return response
    },
    async getTreinos() {
        let response = await axios.get('http://localhost:8000/routines/list')
        return response
    }
}