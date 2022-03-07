<template>
    <v-navigation-drawer
    temporary
    absolute
    v-model="show_drawer">
        <v-list nav>
            <v-list-item-group>
                <!-- <router-link to="musclegroups">
                    <v-list-item>
                        <v-list-item-title>
                            Grupos Musculares
                        </v-list-item-title>
                    </v-list-item>
                </router-link> -->
                <router-link to="exercises">
                    <v-list-item>
                        <v-list-item-title>
                                Exercícios
                        </v-list-item-title>
                    </v-list-item>
                </router-link>
                <router-link to="treinos">
                    <v-list-item>
                        <v-list-item-title>
                            Treinos
                        </v-list-item-title>
                    </v-list-item>
                </router-link>
                <!-- <router-link to="results">
                    <v-list-item>
                        <v-list-item-title>
                            Resultados
                        </v-list-item-title>
                    </v-list-item>
                </router-link> -->
            </v-list-item-group>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
    data() {
        return {
            show_drawer: false
        }
    },
    methods: {
        show() {
            this.show_drawer = !this.show_drawer
        }
    }
}
</script>

<style scoped>
.nav-link {
    text-decoration: none;
    color: green
}
</style>