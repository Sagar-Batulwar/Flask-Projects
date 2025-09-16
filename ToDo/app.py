from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

todo = []

@app.route('/')
def index():
    return render_template('index.html', todo=todo)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('todoitem')
    todos = todo.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todo):
        todo.pop(task_id)
    return redirect(url_for('index'))

