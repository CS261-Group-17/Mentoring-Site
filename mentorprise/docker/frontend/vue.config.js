module.exports = {
  devServer: {
    proxy: {
      "^/backend/*": {
        target: "http://localhost:8000",
        secure: false,
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/backend": "" },
      },
    },
  },
};
