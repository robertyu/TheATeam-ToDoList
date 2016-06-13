from flask import render_template, session, url_for, request, g, jsonify
from app import app
from datetime import datetime
from app import app, db
#from .forms import LoginForm, EditForm
from .models import Todo


@app.route('/')
@app.route('/index')
def index():
    activities  = Todo.query.all()
    count         = Todo.query.count()
    return render_template('index.html', activities=activities, count=count)

@app.route('/add')
def add():
    act = request.args.get('activity', 0, type=str)
    dat = request.args.get('date', 0, type=str)
#    if act != '' and dat != '':
    todo = Todo(activity=act, date=dat)
    db.session.add(todo)
    db.session.commit()
    
    activities  = Todo.query.all()
    return render_template('index.html', activities=activities)
#        return jsonify(result='Activity added successfully!')
#    else:
#        return jsonify(result='All fields are required!')

@app.route('/view/<id>')
def view(id):
    count = todo.query.count()
    return True

@app.route('/editpage/<id>')
def editpage(id):
    task = Todo.query.get(id)
    count = Todo.query.count()
    return render_template('edit.html', task=task, id=id, count=count)

@app.route('/edittask')
def edittask():
    act = request.args.get('activity', 0, type=str)
    dat = request.args.get('date', 0, type=str)
    key = request.args.get('id', 0, type=str)
#   if act != '' and dat != '':
    details = Todo.query.get(key)
    details.activity = act
    details.date = dat
    db.session.add(details)
    db.session.commit()

#        return jsonify(result='Activity edited successfully!')
#    else:
#        return jsonify(result='All fields are required!')

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()

    activities  = Todo.query.all()
    count         = Todo.query.count()
    return render_template('index.html', activities=activities, count=count)
