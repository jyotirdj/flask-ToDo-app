from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todoDatabase.db"

db = SQLAlchemy(app)

# ORM Model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default='active') 
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            task = ToDo(content=content)
            db.session.add(task)
            db.session.commit()
            return redirect('/')  
    tasks = ToDo.query.filter_by(status='active').all()
    return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id:int):
    task = ToDo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods = ['POST', 'GET'])
def edit(id:int):
    task = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form.get('content')
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', task = task)
    
@app.route('/update/<int:id>')
def update(id:int):
    task = ToDo.query.get_or_404(id)
    task.status = 'done'
    db.session.commit()
    return redirect('/')


@app.route('/Done')
def done():
    tasks = ToDo.query.filter_by(status='done').all()
    return render_template('Done.html', tasks=tasks)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
