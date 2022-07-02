import dropbox
import json


with open('secret_keys.json', 'r') as key:
    dict_key = json.load(key)

rdbx = dropbox.Dropbox(
        oauth2_refresh_token=dict_key['dropbox_refresh_token'],
        app_key=dict_key['dropbox_key'],
)

rdbx.refresh_access_token()

dict_key['DROPBOX_OAUTH2_TOKEN'] = rdbx._oauth2_access_token

with open('secret_keys.json', 'w') as key:
    json.dump(dict_key, key)

print(rdbx._oauth2_access_token)

