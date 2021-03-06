module.exports = {
  devServer: {
    proxy: {
      "^/backend": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/backend": "/" },
      },
    },
  },
};
