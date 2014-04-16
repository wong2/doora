#-*-coding:utf-8-*-

ACCESS_KEY = ''
SECRET_KEY = ''

BUCKET_NAME = ''
Q_DOMAIN = '' # your qiniu domain

CALLBACK_URL = ''

EXPIRE_TIME = 0 # file expire time in minutes (0 means no expire)
NEED_EXPIRE = EXPIRE_TIME > 0

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

try:
    from local_config import *
except:
    pass
