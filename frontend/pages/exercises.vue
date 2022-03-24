<template>
    <v-container fluid>
        <v-row justify="center" class="mb-3">
            <h1>Exercícios</h1>
        </v-row>
        <v-layout justify-center child-flex>
            <v-data-table
            :headers="headers"
            :items="exercises"
            class="elevation-1">
            </v-data-table>
        </v-layout>
    </v-container>
</template>

<script>
import urls from '../helpers/api/urls'
export default {
    data() {
        return {
            exercises: [],
            headers: [
                {text: "ID", value:"id"},
                {text:"Nome", value: "name"},
                {text: "Grupo Muscular", value:"musclegroup.name"}
            ]
        }
    },
    methods: {
        async getExercices() {
            let res = await urls.getExercicios()
            this.exercises = [...res.data]
        },
    },
    mounted() {
        this.getExercices()
    }
}
</script>