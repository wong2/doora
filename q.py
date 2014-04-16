#-*-coding:utf-8-*-

from config import ACCESS_KEY, SECRET_KEY

import qiniu.conf

qiniu.conf.ACCESS_KEY = ACCESS_KEY
qiniu.conf.SECRET_KEY = SECRET_KEY

import qiniu.rs
