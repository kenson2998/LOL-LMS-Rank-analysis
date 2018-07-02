## 說明 ##
這裡是介紹前端網頁的部分。

## heroku+Django創建 ##

## 1.安裝 Heroku 工具
https://toolbelt.heroku.com/download/windows

## 2.終端測試登入，登入時會幫你安裝 heroku-CLI  
```command
heroku login  -> email和password
```
## 3.安裝需要用到的插件  
```command
pip install dj-database-url gunicorn dj-static
```
## 4.創立一個loltwggdjango並先到目錄底下
```command
heroku create loltwggdjango
cd C:\..\loltwggdjango\
```
## 5.指定heroku 指向loltwggdjango的專案上
```command
heroku git:remote -a loltwggdjango
```
檢查目前指向的專案位置指令
```command
git remote -v
```
## 6.將django資料放進來

<p style="color: blue;">[]框起來的檔案是後面會另外建立的</p>

loltwggdjango  
    ├── appkenson  
    │　　　　│   
    │　　　　├── __init__.py  
    │　　　　├── settings.py  
    │　　　　├── urls.py  
    │　　　　├── wsgi.py  
    │　　　　└── [<p style="color: blue;">production_settings.py</p>]  
    ├── templates  
    ├── trips  
    ├── manage.py  
    ├── [<p style="color: blue;">.gitignore</p>]  
    ├── [<p style="color: blue;">procfile</p>]  
    ├── [<p style="color: blue;">requirements.txt</p>]  
    └── [<p style="color: blue;">runtime.txt</p>]  

## 7.設定環境變數
```linux
heroku config:set DJANGO_SETTINGS_MODULE=kensontest2.production_settings
```
## 8.將環境會使用到的pip插件存到[requirements.txt]
```linux
pip freeze > requirements.txt
```
## 9.在開啟的目錄下創檔案
(1)[procfile]不要有副檔名並編輯內容為:  
```python
web: gunicorn kensontest2.wsgi
```
(2)[.gitignore]內容為:  
```python
venv
*.pyc
staticfiles
.env
db.sqlite3
```
(3)[runtime.txt]內容為:
```python
python-3.6.3
```
(4)[production_settings.py]內容為:
```python
# Import all default settings.
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

# Static asset configuration.
STATIC_ROOT = 'staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = False
```
(5)修改 kensontest2/wsgi.py
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kensontest2.settings")
```
(6)修改 kensontest2/settings.py
```python
ALLOWED_HOSTS = ['*']
```


## 10.目錄底下建立 Git Repository,add後面要空白再一個"點"，之後更新文件時，也需要執行這三行。
```python
git init
git add .
git commit -m "testupdate"
```
## 11.設定金鑰
```python
heroku keys:add
```
## 12.上傳資料
```python
git push heroku master
```
## 13.網站初始化
```python
heroku ps:scale web=1
```
## 14.static_ROOT error的問題，就執行:
```python
heroku config:set DISABLE_COLLECTSTATIC=1
```
## 15.都正常以後，執行指令格式化資料庫
```python
heroku run python manage.py migrate
```
## 16.開啟django專案
```python
heroku run python manage.py runserver
```