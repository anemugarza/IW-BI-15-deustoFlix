const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: '../appDeustoFlix/static/vue',
  publicPath: '/static/vue/',
})
