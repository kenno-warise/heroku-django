from django.db import models
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)
    file_dir = models.FileField(
            upload_to='csv',
            # validators=[FileExtensionValidator(['csv',])],
            null=True,
            blank=True
    )
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.title

