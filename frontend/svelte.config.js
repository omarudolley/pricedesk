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

                    '@use "src/styles/variables.scss" as *;' +
                    '@use "src/styles/mixins.scss" as *;'
            }
        }),
        optimizeImports()
    ],

    kit: {
        adapter: adapter(),
        alias: {
            $components: 'src/components',
            $lib: 'src/lib'
        }
    }
}

export default config