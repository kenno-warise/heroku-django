import dropbox
import json
import argparse

from django.core.management.utils import get_random_secret_key


with open('secret_keys.json', 'r') as key:
    dict_key = json.load(key)

parser = argparse.ArgumentParser()

parser.add_argument('api')
args = parser.parse_args()

if args.api == 'django':
    result = get_random_secret_key()
    dict_key['django_key'] = result
elif args.api == 'dropbox':
    rdbx = dropbox.Dropbox(
            oauth2_refresh_token=dict_key['dropbox_refresh_token'],
            app_key=dict_key['dropbox_key'],
    )  
    rdbx.refresh_access_token()
    result = rdbx._oauth2_access_token
    dict_key['DROPBOX_OAUTH2_TOKEN'] = result

with open('secret_Keys.json', 'w') as key:
    json.dump(dict_key, key)

print(result)
