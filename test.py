from flask import Flask, render_template, request, url_for, redirect
from newapp import Project
import pygal
app = Flask(__name__)
projects = Project.select()

@app.route('/')
def home():
    return render_template('index.html', pie_data=pieChart(), graph_data=barChart(), projectsHtml=projects)


@app.route('/save', methods=['POST'])
def save():
    ProjectSave = Project(
                          title=request.form['titleform'],
                          type=request.form['typeform'],
                          start_date=request.form['startdateform'],
                          end_date=request.form['enddateform'],
                          description=request.form['descriptionform'],
                          amount=request.form['amountform'],
                          status=request.form['statusform']
                         )

    ProjectSave.save()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    return str(id)

@app.route('/chart')
def barChart():
 bar_chart = pygal.Bar()
 #Then create a bar graph object
 rows = Project.select()
 data = []
 for row in rows:
  data.append(row.amount)
  bar_chart=pygal.Bar()
 label = 'Project Amount'
 bar_chart.add(label, data)
 bar_chart.render_to_file('bar_chart.svg')
 bar_data = bar_chart.render_data_uri()
 return bar_data

def pieChart():
 pie_chart = pygal.Pie()
 pie_chart.title = 'Project Type'
 internal = 0
 external = 0
 rows = Project.select()
 for row in rows:
  if row.type == 'Internal':
      internal = internal+1
  else:
      external = external+1

 pie_chart.add('Internal', internal)
 pie_chart.add('External', external)  # Add some values
 pie_chart.render_to_file('bar_chart.svg')
 pie_data = pie_chart.render_data_uri()
 return pie_data




if __name__ == '__main__':
     app.run(debug=True, port=5051)
