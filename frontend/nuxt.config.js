const _apijs = process.env.API_MOCK === '1' ? 'apimock' : 'api'

export default {
  srcDir: __dirname,
  buildModules: [
    '@nuxtjs/vuetify',
    '@nuxtjs/router'
  ],
}