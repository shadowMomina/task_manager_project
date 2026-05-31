from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Add the src directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from task_manager import TaskManager

app = Flask(__name__)

manager = TaskManager()
manager.load_from_file("data/tasks.json")

@app.route('/')
def index():
    tasks = manager.list_all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        if title:
            manager.add_task(title, description)
            manager.save_to_file("data/tasks.json")
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    manager.mark_done(task_id)
    manager.save_to_file("data/tasks.json")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    manager.remove_task(task_id)
    manager.save_to_file("data/tasks.json")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
# input valiatin is added
