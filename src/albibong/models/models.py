import os

from peewee import *

home_dir = os.path.expanduser("~")
db_dir = f"{home_dir}/Albibong/Albibong.db"
db = SqliteDatabase(db_dir)


class BaseModel(Model):
    class Meta:
        database = db
