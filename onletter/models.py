from django.db import models

import os

# Create your models here.

class uploadFile(models.Model):
    """アップロードファイルのモデル"""
    # upload_toはメディアのルート以下のどこのファイルに
    #　保存するかを指定する。
    #　この場合は media/imagesに保存。
    #　imagesファイルがないなら勝手に新規作成してくれる
    uploadImage = models.ImageField(upload_to='images/')
    verbose_name = ""

    def getFileName(self):
        return os.path.basename(self.file.name)
