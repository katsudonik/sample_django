from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django', # DB名を設定
        'USER': 'root', # DBへ接続するユーザIDを設定
        'PASSWORD': 'admin', # DBへ接続するユーザIDのパスワードを設定
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'NAME': 'test_sample'
        }
    }
}


#INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
