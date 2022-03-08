<template>
    <v-app>
        <toolbar @expand-drawer="handleDrawer"/>
        <drawer ref="drawer"/>
        <v-main>
            <Nuxt/>
        </v-main>
    </v-app>
</template>


<script>
import toolbar from '../components/toolbar.vue'
import drawer from '../components/drawer.vue'

export default ({
    components: {   
        toolbar,
        drawer
    },
    methods: {
        handleDrawer() {
            this.$refs.drawer.show()
        }
    }
})
</script>

<style>
a {
    text-decoration: none;
}
/* a.router-link-active {
    color: grey;
}
a.router-link-exact-active {
    color: grey;
} */
</style>