//import {Spinner} from 'spin.js';

console.log("ぐるぐる開始");
var opts = {
    lines: 13, // 描画する行数
    length: 38, // 各行の長さ
    width: 17, // 線の太さ
    radius: 45, // 内円の半径
    scale: 1, // スピナーの全体的なサイズを拡大縮小する
    corners: 1, // コーナーの真円度 (0..1)
    color: '#dbdbff', // CSSの色または色の配列
    fadeColor: 'transparent', // CSS color or array of colors
    speed: 1, // 1秒あたりのラウンド数
    rotate: 0, // 回転オフセット
    animation: 'spinner-line-fade-quick', // 行のCSSアニメーション名
    direction: 1, // 1：時計回り、-1：反時計回り
    zIndex: 2e9, // The z-index (defaults to 2000000000)
    className: 'spinner', // スピナーに割り当てるCSSクラス
    top: '50%', // 親に対する相対位置
    left: '50%', // 親に対して左の位置
    shadow: '0 0 1px transparent', // ラインのボックスシャドウ
    position: 'absolute' // 要素の配置
};

var target = document.getElementById('spin');
var spinner = new Spinner(opts).spin(target);
$(window).on('load', function() {
    $('#spin').hide();
});

//spin.js作動部
jQuery(function($){
    //ajaxSend()はAjax通信を行う直前に実行させたい処理
    $(document).ajaxSend(function() {
        $("#spin").fadeIn(300);　
    });
        
    $('#upload').click(function(){
        $.ajax({
            type: 'POST',
            success: function(data){
                console.log(data);
            }
        }).done(function() {
            setTimeout(function(){ $("#spin").fadeOut(300); },500);
        });
    }); 
});