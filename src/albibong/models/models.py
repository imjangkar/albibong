from peewee import *

db = SqliteDatabase("Albibong.db")


class BaseModel(Model):
    class Meta:
        database = db
