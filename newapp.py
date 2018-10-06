from peewee import *

db = PostgresqlDatabase('company', user = 'postgres', host = 'localhost', password = 'kibatha@123')

class Project(Model):
    id = AutoField()
    title = CharField()
    type = CharField()
    start_date = DateField()
    end_date = DateField()
    description = TextField()
    amount = DoubleField()
    status = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = 'projects'


Project.create_table(fail_silently=True)

# db.create_tables('projects')