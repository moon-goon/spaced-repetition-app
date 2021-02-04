const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  target: 'web',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, './static'),
    filename: '[name].js',
    chunkFilename: '[id].[chunkhash].js'
  },
  devServer: {
    contentBase: path.join(__dirname, '/dist'),
    compress: true,
    host: '0.0.0.0',
    port: 3000,
    hot: true,
    watchOptions: {
      aggregateTimeout: 500,
      poll: true
  }
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      }
    ],
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  },
  plugins: [
    new HtmlWebpackPlugin({ template: './public/index.html' }),
  ],
};


