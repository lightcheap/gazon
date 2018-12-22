/*require() は各JSファイルをモジュール化しておいて、
使う時に読み込んで参照する*/
var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    
    watch: true,
    context: __dirname,
    
    entry: './onletter/static/onletter/index.js',//Webpackに解析される最初のJSファイル
    output: {
        path: path.resolve('./onletter/static/webpack_bundles/'),//出力jsファイルの場所
        filename: "[name]-[hash].js"//出力ファイルの形式
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ]

}