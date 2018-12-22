# onletter urls.py
from django.urls import path

from . import views

from django.views import View
from django.shortcuts import render
# ファイルのアップロード
from django.conf import settings
from django.conf.urls.static import static

app_name = 'onletter'
urlpatterns = [
    #topページ
    path('', views.toppage.as_view(), name='toppage'),
]

# 開発環境の場合のみ↓を適用する
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)