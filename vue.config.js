module.exports = {
    devServer :{
        proxy: {
            '^/(uz|en|uploads)(/api)/' :{
                target: process.env.BACKEND_SERVER_URL || 'http://127.0.0.1:8000',
                ws: true,
                changeOrigin:true
            }
        }
    },

    pluginOptions: {
      i18n: {
        locale: 'uz',
        fallbackLocale: 'uz',
        localeDir: 'locales',
        enableLegacy: false,
        runtimeOnly: false,
        compositionOnly: false,
        fullInstall: true
      }
    }
}
