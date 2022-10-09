import json
import csv
import tabulate
from datetime import datetime


todo_columns = ["descriprion", "summary", "start_date", "end_date", "finished", 'finished_date']

def start_app():
    try:
        with open("todo_db.csv", 'r', newline='') as f:
            counter = len(f.readlines())
            if not counter:
                writer = csv.writer(f)
                writer.writerow(todo_columns)

    except:  
        with open("todo_db.csv", 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(todo_columns)


def create_date():
    return datetime.today().strftime('%Y-%m-%d')

def add_record():
    recorder = dict()
    counter = 0
    for column in todo_columns:
        counter += 1
        if counter == 6:
            if recorder[todo_columns[4]] == "1":
                recorder[column] = input(f"Enter the column {column} :")
            else:
                recorder[column] = ""
        else:
            recorder[column] = input(f"Enter the column {column} :")

    print(json.dumps(recorder, indent=2, default=str))
    response = input('Enter 1 to create data for app ')
    if response == "1":
        with open("todo_db.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            if recorder['finished'] == "1":
                recorder['finished'] = '1'
            else:
                recorder['finished'] = '0'
            writer.writerow(recorder.values())
            print('Column is created.')
    else:
        print('Exit by user.')


def todo_list(creation=False):
    data_list = list()
    with open("todo_db.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        if creation:
            for number, row in enumerate(reader, 0):
                if number:
                    data_list.append([number] + row)
        for row in reader:
            data_list.append(row)
        results = tabulate.tabulate(data_list)
    print(results)


def delete_column():
    todo_list(True)
    print('It is posible to enter several items via coma (1,2,3)')
    del_item = input("Enter column number for deleting: ")
    list_del_item = del_item.split(',')
    if len(list_del_item):
        data_list = list()
        with open('todo_db.csv', 'r') as in_data:
            for number, row in enumerate(csv.reader(in_data), 0):
                data_list.append(row)

        list_del_item.sort(reverse=True)

        for index in list_del_item:
            data_list.pop(int(index))

        with open('todo_db.csv', 'w', newline='') as out_data:
            writer = csv.writer(out_data)
            for row in data_list:
                writer.writerow(row)
        print('Column is deleted.')
    else:
        print("The deleting is canceled")


def done_todo():
    todo_list(True)
    print('It is posible to enter several items via coma (1,2,3) ')
    task_done = input("Enter column number for mark as finished: ")
    task_done_list = task_done.split(',')
    if len(task_done_list):
        task_data = list()
        with open('todo_db.csv', 'r') as in_data:
            for num, row in enumerate(csv.reader(in_data), 0):
                task_data.append(row)

        for task_done_index in task_done_list:
            task_data[int(task_done_index)][4] = '1'
            task_data[int(task_done_index)][5] = create_date()

        with open('todo_db.csv', 'w', newline='') as out_data:
            writer = csv.writer(out_data)
            for row in task_data:
                writer.writerow(row)
        print('Task is finished')
    else:
        print("The mark process is canceled")


def todo_info():
    result = dict()
    with open("todo_db.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        for num, row in enumerate(reader, 0):
            if num:
                if row[4] == '1': 
                    result[row[5]] = result.get(row[5], 0) + 1

    info_data = ",\n".join([f"{value}: {key} task is finished" for value, key in result.items()])
    print(info_data)

def menu_list():
    print("".join(["1 = add an item,\n",
                   "2 = remove an item,\n",
                   "3 = mark the task as finished,\n",
                   "4 = list item\n",
                   "5 = todo app information\n",
                   "0 = exit\n",
                   "menu = todo menu\n"
                   ]))



actions_dict = {
    "1": add_record,
    "2": delete_column,
    "3": done_todo,
    "4": todo_list,
    "5": todo_info,
    "menu": menu_list,

}


start_app()
print("The menu of commands:")
menu_list()
while True:
    input_data = input('Select the action: ')
    if input_data == "0":
        print('The app is closed')
        break
    todo_action = actions_dict[input_data]
    if todo_action:
        todo_action()
    else:
        print('Data is incorrect, enter the correct data')

