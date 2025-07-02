import os
import tempfile

import pytest

from task_manager import TaskManager


def test_add_and_complete_task():
    manager = TaskManager()
    manager.add_task("Завершить финальное задание по Python")
    assert len(manager.get_tasks()) == 1
    assert manager.get_tasks()[0]['description'] == "Завершить финальное задание по Python"
    assert manager.get_tasks()[0]['completed'] is False

    manager.complete_task(0)
    assert manager.get_tasks()[0]['completed'] is True


def test_remove_task():
    manager = TaskManager()
    manager.add_task("Специальная задача для удаления")
    assert len(manager.get_tasks()) == 1

    manager.remove_task(0)
    assert len(manager.get_tasks()) == 0

    with pytest.raises(IndexError):
        manager.remove_task(0)


def test_save_and_load_from_json():
    manager = TaskManager()
    manager.add_task("Задача 1")
    manager.add_task("Задача 2")
    manager.complete_task(0)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
        temp_file_name = tmpfile.name

    try:
        manager.save_to_json(temp_file_name)
        new_manager = TaskManager()
        new_manager.load_from_json(temp_file_name)

        assert len(new_manager.get_tasks()) == 2
        assert new_manager.get_tasks()[0]['description'] == "Задача 1"
        assert new_manager.get_tasks()[0]['completed'] is True
        assert new_manager.get_tasks()[1]['description'] == "Задача 2"
        assert new_manager.get_tasks()[1]['completed'] is False
    finally:
        os.remove(temp_file_name)