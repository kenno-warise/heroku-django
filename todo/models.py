from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from django.conf import settings


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)
    file_dir = models.FileField(
            'ファイル',
            upload_to='file',
            # validators=[FileExtensionValidator(['csv',])],
            null=True,
            blank=True
    )
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        ファイルが保存される前の処理
        Dropboxのアクセストークンを更新する
        """
        if not settings.DEBUG:
            if self.file_dir:
                print('file=True')
                default_storage.client._oauth2_access_token = ''
                default_storage.client._oauth2_refresh_token = settings.DROPBOX_OAUTH2_TOKEN
                default_storage.client._app_key = settings.DROPBOX_KEY
            else:
                print('flie=False')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

