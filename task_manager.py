import  json
from os import remove


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, description: str):
        if not description.strip():
            raise ValueError("Описание задачи не может быть пустым.")

        for task in self.tasks:
            if task['description'] == description:
                raise ValueError("Такая задача уже существует.")

        self.tasks.append({
            'description': description,
            'completed': False
        })


    def complete_task(self, index: int):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Индекс вне диапазона.")
        self.tasks[index]['completed'] = True


    def remove_task(self, index: int):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Индекс вне диапазона.")
        del self.tasks[index]


    def save_to_json(self, filename: str):
        with open(filename, 'w',  encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)


    def load_from_json(self, filename: str):
        with open(filename, 'r',  encoding='utf-8') as file:
            self.tasks = json.load(file)


    def get_tasks(self):
        return self.tasks