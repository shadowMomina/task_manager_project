# TaskManager class - Manages collection of tasks
import json
import os
from task import Task
"""TaskManager manages collection of tasks with save/load functionality"""
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task.id

    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_done(self, task_id):
        task = self.get_task(task_id)
        if task:
            return task.mark_done()
        return False

    def list_all(self):
        return self.tasks.copy()

    def count_tasks(self):
        return len(self.tasks)

    def save_to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
                if self.tasks:
                    self.next_id = max(t.id for t in self.tasks) + 1