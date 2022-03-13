module.exports = {
    devServer: {
      proxy: {
        "^/backend": {
          target: "http://backend",
          changeOrigin: true,
          logLevel: "debug",
          secure: false,
          pathRewrite: { "^/backend": "" },
        //   onProxyReq: function(request) {
        //       request.setHeader("origin", "http://localhost:8000");
        //   },
        },
      },
    },
  };
  