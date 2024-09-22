// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['~/assets/css/main.css'],

  // devtools: { enabled: true },
  // imports: {
  //   dirs: [
  //     // Scan top-level modules
  //     'composables',
  //     // ... or scan modules nested one level deep with a specific name and file extension
  //     'composables/*/index.{ts,js,mjs,mts}',
  //     // ... or scan all modules within given directory
  //     'composables/**'
  //   ]
  // }
  modules: [
    '@nuxtjs/tailwindcss'
  ],

  compatibilityDate: '2024-09-10'
})