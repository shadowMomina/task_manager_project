import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src")
from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    tid = manager.add_task("Test", "Desc")
    assert tid == 1