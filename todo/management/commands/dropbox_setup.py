from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not settings.DEBUG:
            print(default_storage.client.users_get_current_account().name.display_name, '完了')
        else:
            print('デバッグは有効です')
