"""Peewee migrations -- 001_init.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""

from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator

with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""

    print("001_init")

    @migrator.create_model
    class BaseModel(pw.Model):
        id = pw.AutoField()

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class Dungeon(pw.Model):
        id = pw.UUIDField(unique=True)
        type = pw.CharField(max_length=255)
        name = pw.CharField(max_length=255)
        tier = pw.IntegerField(default=0)
        fame = pw.FloatField(default=0.0)
        silver = pw.FloatField(default=0.0)
        re_spec = pw.FloatField(default=0.0)
        start_time = pw.DateTimeField()
        end_time = pw.DateTimeField(null=True)
        meter = pw.TextField()

        class Meta:
            table_name = "dungeon"

    @migrator.create_model
    class Island(pw.Model):
        uuid = pw.UUIDField(unique=True)
        id = pw.CharField(max_length=255)
        name = pw.CharField(max_length=255)
        type = pw.CharField(max_length=255)
        start_time = pw.DateTimeField()
        crops = pw.TextField()
        animals = pw.TextField()

        class Meta:
            table_name = "island"

    @migrator.create_model
    class Location(pw.Model):
        uuid = pw.UUIDField(unique=True)
        id = pw.CharField(max_length=255)
        name = pw.CharField(max_length=255)
        type = pw.CharField(max_length=255)

        class Meta:
            table_name = "location"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""

    migrator.remove_model("location")

    migrator.remove_model("island")

    migrator.remove_model("dungeon")

    migrator.remove_model("basemodel")
