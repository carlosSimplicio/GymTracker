<template>
    <v-dialog v-model="visible" max-width="60vw">
        <v-card>
            <v-card-title>{{ treino.name }}</v-card-title>
            <v-container fluid>
                <v-row>
                    <v-expansion-panels accordion>
                        <v-expansion-panel v-for="routine in treino.routines" :key="routine.exercise.id">
                            <v-expansion-panel-header>
                                <div class="inline-row">
                                    <div class="mr-2">{{ routine.exercise.nome }}</div>
                                    <div>{{ routine.sessions.length }} séries</div>
                                </div>
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                <v-row v-for="serie in routine.sessions" :key="serie.load">
                                    <div>Repetições: {{ serie.repetitions }} Carga: {{ serie.load }}</div>
                                </v-row>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    data() {
        return {
            visible: false,
            treino: {},
        }
    },
    methods: {
        toggle(treino) {
            this.visible = true
            this.treino = treino
        }
    }
}
</script>

<style scoped>
.inline-row{
    display: flex;
    flex-direction: row;
}
</style>