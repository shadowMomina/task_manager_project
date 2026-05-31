# Task class - Represents a single task in the system
#Task class represents a single task with id, title, description and status
class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        self.status = "Done"
        return True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["description"], data["status"])

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status}"
    