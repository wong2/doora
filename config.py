#-*-coding:utf-8-*-

ACCESS_KEY = ''
SECRET_KEY = ''

BUCKET_NAME = ''
Q_DOMAIN = '' # your qiniu domain

CALLBACK_URL = '' # explained in http://docs.qiniu.com/api/v6/put.html#put-policy

EXPIRE_TIME = 0 # file expire time in days (0 means no expire)


try:
    from local_config import *
except:
    pass
