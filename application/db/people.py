import json

path = 'staff.json'


def get_employees(file_path):
    with open(file_path, 'r', encoding='utf-8') as content:
        data = json.load(content)
        employees_inf = []
        for i in data:
            print(f'name: {i["name"]: <8}| surname: {i["surname"]}')
            employees_inf.append(f'name: {i["name"]: <8} | |  surname: {i["surname"]}')
        return employees_inf


if __name__ == '__main__':
    get_employees(path)
