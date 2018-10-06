from peewee import *

db = PostgresqlDatabase('company', user = 'postgres', host = 'localhost', password = 'kibatha@123')

class User(Model):
    id = AutoField()
    name = CharField()
    email = CharField()
    password = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = 'users'


User.create_table(fail_silently=True)

# db.create_tables('projects')