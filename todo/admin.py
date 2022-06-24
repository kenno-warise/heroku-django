from django.contrib import admin
from django.core.files.storage import default_storage
from django.conf import settings

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_dir', 'created_at')

    def save_model(self, request, obj, form, change):
        if not settings.DEBUG:
            if obj.file_dir:
                print('file=True')
                default_storage.client._oauth2_access_token = ''
                default_storage.client._oauth2_refresh_token = settings.DROPBOX_OAUTH2_TOKEN
                default_storage.client._app_key = settings.DROPBOX_KEY
                print(default_storage.client.__dict__)
            else:
                print('file=False')

        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
