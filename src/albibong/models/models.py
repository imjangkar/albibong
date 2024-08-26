import os

from peewee import *

home_dir = os.path.expanduser("~")
SQLITE_DB = f"{home_dir}/Albibong/Albibong.db"
db = SqliteDatabase(SQLITE_DB)


class BaseModel(Model):
    class Meta:
        database = db
