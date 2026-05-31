import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src")
from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    tid = manager.add_task("Test", "Desc")
    assert tid == 1
def test_extra_third():
    m = TaskManager()
    m.add_task("X", "Y")
    m.add_task("Z", "W")
    m.remove_task(1)
    assert m.count_tasks() == 1

def test_extra_fourth():
    m = TaskManager()
    result = m.get_task(1)
    assert result is None

def test_extra_fifth():
    m = TaskManager()
    m.add_task("Test", "Desc")
    task = m.get_task(1)
    assert task.title == "Test"
def test_add_single_task():
    m = TaskManager()
    task_id = m.add_task("Single Task", "Description")
    assert task_id == 1
    assert m.count_tasks() == 1


def test_remove_nonexistent_task():
    m = TaskManager()
    m.add_task("Task", "Desc")
    m.remove_task(999)
    assert m.count_tasks() == 1


def test_mark_done_on_already_done():
    m = TaskManager()
    task_id = m.add_task("Task", "Desc")
    m.mark_done(task_id)
    result = m.mark_done(task_id)
    assert result == True
    task = m.get_task(task_id)
    assert task.status == "Done"


def test_get_task_wrong_id():
    m = TaskManager()
    m.add_task("Task1", "Desc1")
    m.add_task("Task2", "Desc2")
    result = m.get_task(999)
    assert result is None


def test_list_all_empty():
    m = TaskManager()
    tasks = m.list_all()
    assert len(tasks) == 0
    assert tasks == []


def test_multiple_operations_sequence():
    m = TaskManager()
    id1 = m.add_task("First", "Desc1")
    id2 = m.add_task("Second", "Desc2")
    id3 = m.add_task("Third", "Desc3")
    
    assert m.count_tasks() == 3
    
    m.mark_done(id2)
    task2 = m.get_task(id2)
    assert task2.status == "Done"
    
    m.remove_task(id1)
    assert m.count_tasks() == 2
    
    tasks = m.list_all()
    task_ids = [t.id for t in tasks]
    assert id1 not in task_ids
    assert id2 in task_ids
    assert id3 in task_ids
def test_add_task_with_empty_title():
    m = TaskManager()
    task_id = m.add_task("", "Description")
    assert task_id == 1
    task = m.get_task(1)
    assert task.title == ""

def test_mark_done_multiple_tasks():
    m = TaskManager()
    m.add_task("Task1", "Desc1")
    m.add_task("Task2", "Desc2")
    m.add_task("Task3", "Desc3")
    m.mark_done(1)
    m.mark_done(3)
    assert m.get_task(1).status == "Done"
    assert m.get_task(2).status == "Pending"
    assert m.get_task(3).status == "Done"