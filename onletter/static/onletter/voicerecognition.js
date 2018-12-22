
//GAZONの音声認識
var flagSpeech = 0; //フラグを作成。基本「０」だと起動


function soundCognitionLongUse() {
    var content = document.getElementById('scroll');
    var status = document.getElementById('status');
    var resultcontents = document.getElementById('resultSentence');
    var stopbtn = document.getElementById('stopbtn');
    resultcontents.innerHTML;
    var speech = new webkitSpeechRecognition(); //音声認識のAPI使用するからインスタンス作成
    var bufferText = resultcontents.innerHTML;
    speech.interimResults = true; //　trueで変換途中でも認識する
    speech.continuous = true; //  trueで 連続音声認識できる！


    //音声認識の状態を表示
    speech.onsoundstart = function(){
        status.innerHTML = "認識中";
    };
    speech.onnomatch = function(){
        status.innerHTML = "再度チャレンジ";
    };
    speech.onerror = function(){
        status.innerHTML = "エラーです";
        //フラグが０（認識途中でない場合）なら再度関数スタート
        if( flagSpeech == 0 ){
            soundCognitionLongUse();
        }
    };
    speech.onsoundend = function(){
        status.innerHTML = "停止中";
        if( flagSpeech == 0 || flagSpeech == 1 ){
            //長時間途切れることなく使うため、再度関数スタート
            soundCognitionLongUse();
        }
        
    };
    

    //音声認識の結果処理
    speech.onresult = function(event){
        var results = event.results;
        //resultIndex =SpeechRecognitionResultList "配列"の中で最も低いインデックス値の結果を返します。
        for (var i = event.resultIndex; i<results.length; i++){
            // .isFinal =変換終了したかを判定
            if(results[i].isFinal){
                //終了時
                //それまでの保存してた分と一緒に出力する。
                resultcontents.innerHTML = bufferText + results[i][0].transcript;
                bufferText += results[i][0].transcript;
            }else{
                //でないなら途中結果として出力
                content.innerHTML = "[途中経過] "+ results[i][0].transcript;
                //フラグをたてる
                flagSpeech = 1;
            }
        }
    }

    flagSpeech = 0;
    speech.start();
    status.innerHTML = "start";

    //STOPボタンを押したらWebSpeechAPIを止める
    stopbtn.addEventListener('click', function(){
        flagSpeech = 2;
        speech.stop();
        status.innerHTML = "stop";
        
    },false);

}

