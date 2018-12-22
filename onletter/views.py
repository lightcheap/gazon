from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# 画像アップロードフォーム
from .form import imageUploadForm
#　画像アップロードもでる
from .models import uploadFile
from PIL import Image

# pyocr
import sys
import pyocr
import pyocr.builders

class toppage(View):
    """トップページ"""
    def get(self, request, *args, **kwargs):

        dict={
            'imageUploadForm':imageUploadForm(),#フォームの用意
            'resultRecognition':uploadFile.verbose_name
        }
        return render(request, 'onletter/top.html', dict)

    def post(self, request, *args, **kwargs):
        # 画像アップロードあたりの処理
        if request.method =='POST':
            form = imageUploadForm(request.POST, request.FILES)
            if not form.is_valid():
                raise ValueError('今アップロードされた画像は無効な形式の為エラーです。')
            
            # モデルのインスタンス作成
            uploadfile = uploadFile()

            uploadfile.uploadImage = form.cleaned_data['imageUpload']
			# アップロードしたファイル名
            uploadFileName = uploadfile.uploadImage.name
            uploadfile.save()
			

			# 画像認識をここに入れとく（とりあえず）
            tools = pyocr.get_available_tools()
            if len(tools) == 0:
                print("OCRツールは見当たりませんけど？")
                sys.exit(1)
			# このツールは推奨された使用順序で返されます
            tool = tools[0]
            print("使用ツールは '%s'" % (tool.get_name()))
			# 例: 使用ツールは 'libtesseract'
            langs = tool.get_available_languages()
            print("Available languages: %s" % ", ".join(langs))
            lang = langs[2]
            print("使用言語は '%s'" % (lang))
			# 例: 使用言語は 'jp'
			# 言語は決してソートされません。 
			# 使用するデフォルト言語については、システムのロケール設定を参照してください

			#画像から文字
            txt = tool.image_to_string(
    		Image.open('media/images/%s' % (uploadFileName)),
    		lang=lang,
    		builder=pyocr.builders.TextBuilder()
			)
			# txt はpython文字列

            word_boxes = tool.image_to_string(
				Image.open('media/images/%s' % (uploadFileName)),
				lang = lang,
				builder = pyocr.builders.WordBoxBuilder()
			)
			# ボックスオブジェクトのリスト。各ボックスは：
			#　　box.content はボックス内の文
			#　　box.position はページ上の位置（ピクセル単位）
			#いくつかのOCRツール（例えばTesseract）は空のボックスを返すかもしれないことに注意
			
            line_and_word_boxes = tool.image_to_string(
				Image.open('media/images/%s' % (uploadFileName)),
				lang = lang,
				builder = pyocr.builders.LineBoxBuilder()
			)
			# 行オブジェクトのリスト。 各行は:
			#  line.word_boxesは、単語ボックスのリスト（行内の個々の単語）
			#  line.contentは行全体のテキストです
			#  line.positionはページ上の行全体の位置（ピクセル単位）
			# 各単語ボックスオブジェクトは、OCRツールによって返される信頼度スコア「confidence」を有する。
			# 信頼スコアは、OCRツールに完全に依存。
			# TesseractとLibtesseractでのみサポートされています（常に楔形文字で0）。
			# いくつかのOCRツール（例えばTesseract）は空の内容のボックスを返すかもしれないことに注意

			# Digtis -Tesseractのみ
            digits = tool.image_to_string(
				Image.open('media/images/%s' % (uploadFileName)),
				lang = lang,
				builder = pyocr.tesseract.DigitBuilder()

			)
			# digits はpython文字列
            print(uploadfile.verbose_name)

            dict={
				'imageUploadForm':imageUploadForm(),#フォームの用意
				'uImage': uploadFile.objects.all().last(), # アップロードした画像
				'resultRecognition':txt,
				'uploadFileName':uploadFileName,
			}
            return render(request,'onletter/top.html', dict)
