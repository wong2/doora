#-*-coding:utf-8-*-

from config import BUCKET_NAME, EXPIRE_TIME, REDIS_HOST, REDIS_PORT
from q import qiniu

from redis import Redis
from datetime import timedelta
from rq_scheduler import Scheduler


connection = Redis(REDIS_HOST, port=REDIS_PORT)
scheduler = Scheduler('doora', connection=connection)


class DELETE_ERROR(Exception):
    pass


def add_to_expire_queue(file_key, expire_in=EXPIRE_TIME):
    if not EXPIRE_TIME:
        return

    scheduler.enqueue_in(timedelta(minutes=expire_in), delete_file, file_key)


def delete_file(file_key):
    ret, err = qiniu.rs.Client().delete(BUCKET_NAME, file_key)
    if err is not None:
        raise DELETE_ERROR
