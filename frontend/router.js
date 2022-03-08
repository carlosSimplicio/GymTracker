import Vue from 'vue'
import Router from 'vue-router'

import index from '~/pages/index'
import exercises from '~/pages/exercises'
import treinos from '~/pages/treinos'

Vue.use(Router)

export function createRouter() {
  return new Router({
    mode: 'history',
    routes: [
      { path: '/', component: index, name: 'home' },
      { path: '/exercises', component: exercises, name: 'exercises' },
      { path: '/treinos', component: treinos, name: 'treinos' },
    ]
  })
}