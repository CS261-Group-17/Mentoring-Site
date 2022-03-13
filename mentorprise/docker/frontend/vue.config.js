module.exports = {
  devServer: {
    proxy: {
      "^/backend/*": {
        pathRewrite: { "^/backend": "" },
      },
    },
  },
};
