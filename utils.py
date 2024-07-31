import json


def get_data(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def add_task(new_task):
    path = "data.json"
    list_tasks = get_data(path)
    list_tasks.append(new_task)

    with open(path, "w", encoding='utf-8') as file:
        json.dump(list_tasks, file, ensure_ascii=False)


def delete_list_task():
    path = "data.json"
    with open(path, "w", encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False)




# ["Помыть посуду", "Погулять с собакой", "Выучить уроки", "Поесть"]