<template>
    <div>
        <v-app-bar dense>
             <v-app-bar-nav-icon @click.stop="$emit('expand-drawer')"/>
            <v-toolbar-title>Diário de Treinos</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-title>GymTrack</v-toolbar-title>
        </v-app-bar>
    </div>
</template>

<script>
export default {
    data() {
        return {
            teste: "DIÁRIO DE TREINO"
        }
    }
}
</script>