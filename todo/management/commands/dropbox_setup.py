from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not settings.DEBUG:
            try:
                print(default_storage.client.users_get_current_account().name.display_name, '完了')
            except:
                oauth_refresh_token = default_storage.client._oauth2_access_token
                default_storage.client._oauth2_access_token = ''
                dropbox_key = settings.DROPBOX_KEY
                default_storage.client._app_key = dropbox_key
                print(default_storage.client.__dict__)
                # print(default_storage.client.users_get_current_account().name.display_name, 'セットアップ完了')
        else:
            print('デバッグは有効です')
