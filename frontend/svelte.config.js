import adapter from '@sveltejs/adapter-static'
import preprocess from 'svelte-preprocess'
import { optimizeImports } from 'carbon-preprocess-svelte'

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: [
    preprocess({
      scss: {
        // make variables accessible in components without explicit import
        prependData:
          '@use "src/styles/index.scss" as *;' +
          '@use "src/styles/variables.scss" as *;' +
          '@use "src/styles/mixins.scss" as *;'
      }
    }),
    optimizeImports()
  ],
  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: null,
      precompress: false
    }),
    alias: {
      $components: 'src/components',
      $lib: 'src/lib'
    },
    prerender: {
      default: true
    },
    trailingSlash: 'always',
    paths: {
      base: '/pricedesk'
    }
  }
}

export default config
