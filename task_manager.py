import  json
from os import remove


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, description: str):
        if not description.strip():
            print("Описание задачи не может быть пустым.")
            return

        for task in self.tasks:
            if task['description'] == description:
                print("Такая задача уже существует.")
                return

        self.tasks.append({
            'description': description,
            'completed': False
        })
        print(f"Задача '{description}' добавлена.")


    def complete_task(self, index: int):
        if self.is_index_valid(index):
            task = self.tasks[index]
            if task['completed']:
                print(f"Задача '{task['description']}'уже выполнена.")
            else:
                task['completed'] =  True
                print(f"Задача '{task['description']}' отмечена, как выполненная.")


    def remove_task(self, index: int):
        if self.is_index_valid(index):
            remove_task = self.tasks.pop(index)
            print(f"Задача '{remove_task['description']}' удалена.")


    def save_to_json(self, filename: str):
        try:
            with open(filename, 'w') as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
            print(f"Задачи успешно сохранены в '{filename}'.")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")


    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                loaded_tasks = json.load(file)
                self.tasks = loaded_tasks
            print(f"Задачи успешно загружены из файла '{filename}'.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла '{filename}'. Некорректный формат JSON.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке данных: {e}")


    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\nСписок задач:")
        for i, task in enumerate(self.tasks):
            status = "V" if task['completed'] else "X"
            print(f"{i}[{status}]{task['description']}")


    def is_index_valid(self, index: int):
        if 0 <= index < len(self.tasks):
            return True
        else:
            print("Задача с таким индексом не найдена.")
            return  False