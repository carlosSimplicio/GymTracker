<template>
    <v-dialog v-model="visible" width="800px">
        <v-card class=pa-4>
            <v-card-title>Criar Treino</v-card-title>
            <v-card-text>
                <v-form>
                    <v-text-field label="Nome do Treino"/>
                    <v-btn fab>
                        <v-icon>
                            mdi-plus
                        </v-icon>
                    </v-btn>
                </v-form>
                <v-row justify="end">
                    <v-btn class="mr-2">Cancelar</v-btn>
                    <v-btn>Criar</v-btn>
                </v-row>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script>

export default {
data() {
    return {
    visible: false,
    }
},
methods: {
    toggle() {
    this.visible = !this.visible
    }
},
}
</script>
