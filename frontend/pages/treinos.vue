<template>
    <v-container fluid>
        <v-row justify="center" class="mb-3">
            <h1>Treinos</h1>
        </v-row>
        <v-row justify="end">
            <v-btn class="mr-5 mb-3" @click="showPopupCreateRoutine">Criar Treino</v-btn>
        </v-row>
        <v-layout justify-center child-flex wrap>
            <v-data-table
            :headers="headers"
            :items="treinos"
            sort-by="id"
            class="elevation-1"
            @click:row="showPopupRoutine">
            </v-data-table>
        </v-layout>
        <popup-treino ref="popupTreino"/>
        <popup-criar-treino ref="popupCriarTreino"/>
    </v-container>
</template>

<script>
import urls from '../helpers/apimock/urls'
import popupTreino from '../components/popup-treino.vue'
import popupCriarTreino from '../components/popup-criar-treino.vue'

export default {
    components: {
        popupTreino,
        popupCriarTreino
    },
    data() {
        return {
            treinos: [],
            headers: [
                {text: "ID", value:"id"},
                {text:"Nome", value: "name"}
            ]
        }
    },
     mounted() {
        this.getTreinos()
    },
    methods: {
        async getTreinos() {
            let res = await urls.getTreinos()
            this.treinos = [...res.data]
        },
        showPopupRoutine(item) {
            this.$refs.popupTreino.toggle(item)
        },
        showPopupCreateRoutine(item) {
            this.$refs.popupCriarTreino.toggle(item)
        }
    },
}
</script>