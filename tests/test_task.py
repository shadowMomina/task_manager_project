import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src")
from task import Task

def test_task_creation():
    t = Task(1, "Buy milk", "2 litres")
    assert t.id == 1
    assert t.title == "Buy milk"