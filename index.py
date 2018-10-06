from flask import Flask, render_template, request, url_for, redirect, flash, session
from newapp import Project
from user import User
import pygal
import json
import req
app = Flask(__name__)
app.secret_key = '$ee23rwfs'

def authenticator():
    if session:
        return True
    else:
        return False



@app.route('/login', methods=['POST'])
def login():
    try:
        user = User.get(User.email == request.form['email'], User.password == request.form['password'])
        session['mtu'] = True
        session['id'] = user.id
        flash('Logged in Successfully')
        return redirect(url_for('home'))
    except:
        flash('Bad Credentials')
        return render_template('authentication.html')



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/jsondata')
def jsonData():
    person = {'name':'Edwin', 'location':'Nairobi', 'work': 'techcamp'}
    joke = requests.joke
    return json.dumps(person)

@app.route('/register',methods=['POST'])
def register():
        #check if email exists
   try:
        User.get(User.email == request.form['email'])
        flash('User Already Exists')
        return render_template('authentication.html')
   except:
       if request.form['password'] == request.form['confirm-password']:
            user = User(name=request.form['username'], email=request.form['email'],  password=request.form['password'])
            user.save()
            # set session
            session['mtu'] = True
            session['id'] = user.id
            return redirect(url_for('home'))
       flash('')
       return redirect(url_for('authentication.html'))



@app.route('/')
def home():
    if authenticator():
     projects = Project.select().order_by(Project.id)
     return render_template('index.html', pie_data=pieChart(), graph_data=barChart(), projectsHtml=projects)
    else:
        return render_template('authentication.html')


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
    flash('Record Saved Successfully')
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    project = Project.get(Project.id == id)
    project.title = request.form['titleform']
    project.type = request.form['typeform']
    project.start_date = request.form['startdateform']
    project.save()
    flash('Record Updated Successfully')
    return redirect(url_for('home'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    try:
        project = Project.get[Project.id == id]
        project.delete_instance()
        flash('Record Deleted')
        return redirect(url_for('home'))
    except:
        return ('Server Error')


@app.route('/chart')
def barChart():
 bar_chart = pygal.Bar()
 #Then create a bar graph object
 data = []
 projects = Project.select()
 for row in projects:
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
 projects = Project.select()
 for row in projects:
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

