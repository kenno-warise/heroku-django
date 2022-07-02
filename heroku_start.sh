#!/bin/bash
#
# Dropbox refresh access token
#
# 2022/06/25


if [ -f ./.env ]; then
  read -p 'heroku localを起動しますか？ yes/no ' m
  if [ $m = 'yes' ] || [ $m = 'ye' ] || [ $m = 'y' ]; then
    echo 'heroku localを起動します。 http://localhost:5000/'
    heroku local
  fi
else
  echo '.envが存在しないので作成します。'
  # heroku addons:create heroku-postgresql:hobby-dev
  # echo 'DATABASE_URLの作成 OK!'
  # key=`python3 manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
  key=`python3 refresh.py django`
  echo 'DjangoのSECRET_KEY再生成 OK!'
  heroku config:set SECRET_KEY=$key
  token=`python3 refresh.py dropbox`
  echo 'Dropboxのアクセストークン生成 OK!'
  heroku config:set DROPBOX_OAUTH2_TOKEN=$token
  branch=`git branch | grep '*' | tr ' ' '\n' | grep -v '*'`
  echo ブランチは$branchで送信します。
  git push heroku $branch
  heroku run python3 manage.py migrate
  echo 'DATABASEの初期化 OK!'
  heroku run python3 manage.py createsuperuser
  echo 'スーパーユーザーの設定 OK!'
  heroku config:get APP_DEBUG DATABASE_URL DROPBOX_OAUTH2_TOKEN SECRET_KEY -s > .env
  read -p 'heroku localを起動しますか？ yes/no ' m
  if [ $m = 'yes' ] || [ $m = 'ye' ] || [ $m = 'y' ]; then
    echo 'heroku localを起動します。 http://localhost:5000/'
    heroku local
  else
    echo 'セットアップ完了'
  fi
fi
