from newapp import Project

# project1 = Project(title='classroom construction', type='internal', start_date='2018-03-12', end_date='2019-03-17', description='class 7', amount=4000000, status=1)
# project1.save()
#
# project2 = Project(title='toilet construction', type='internal', start_date='2019-05-10', end_date='2019-12-12', description='lower block', amount=700000, status=1)
# project2.save()
#
# project3 = Project(title='dormitory construction', type='internal', start_date='2018-03-17', end_date='2019-09-17', description ='main dormitory', amount=12000000, status=2)
# project3.save()

# project1 = Project.select().where(Project.id == 1).get()
# print(project1.id, project1.title, project1.type, project1.start_date, project1.end_date, project1.description, project1.amount, project1.status)

for project in Project.select():
    #print(project.id, project.title, project.type, project.start_date, project.end_date, project.description, project.amount, project.status)
 print(project.amount)