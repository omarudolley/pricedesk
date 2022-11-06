import { sveltekit } from '@sveltejs/kit/vite'
import svg from '@poppanator/sveltekit-svg'

const config = {
  plugins: [sveltekit(), svg()]
}

export default config
