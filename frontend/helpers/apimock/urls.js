import { exercices, treinos } from "./db_mock/db_mock"
import { mockapi, mockapierror } from "./mockadapter"

export default {

    getExercicios() {
        return mockapi(exercices)
    },
    getExerciciosError(erro) {
        return mockapierror(erro)
    },
    getTreinos() {
        return mockapi(treinos)
    }

}