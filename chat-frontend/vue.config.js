module.exports = {
    // options...
    devServer: {
        disableHostCheck: true,
        proxy: {
            "^/chat": {
            target: "http://localhost:8000",
            ws: true,
            changeOrigin: true
          }
        }
    }
}