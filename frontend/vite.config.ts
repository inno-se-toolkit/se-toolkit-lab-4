import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const target = env.VITE_API_TARGET || 'http://127.0.0.1:42002'

  return {
    plugins: [react()],
    server: {
      proxy: {
        '/items': target,
        '/learners': target,
        '/interactions': target,
        '/docs': target,
        '/openapi.json': target,
      },
    },
  }
})
