#!/usr/bin/python3

import requests
import sys


class Employee:
    __url = "https://jsonplaceholder.typicode.com/"

    def __init__(self, id=0):
        self.id = id

    def employee_data(self):
        response = requests.get(Employee.__url + "users/{}".format(self.id))
        if response.status_code == 200:
            return response.json()

    def todo_list(self):
        response = requests.get(Employee.__url + "todos?userId={}"
                                .format(self.id))
        if response.status_code == 200:
            return response.json()

    def todo_progress(self):
        employee_name = self.employee_data().get("name")
        tasks = self.todo_list()
        tasks_done = [task['title'] for task in tasks if task['completed']]
        result = "Employee {} is done with tasks ({}/{}):"\
            .format(employee_name, len(tasks_done), len(tasks))
        for task in tasks_done:
            result += "\n\t{}".format(task)
        return result


if __name__ == "__main__":

    employee = Employee(sys.argv[1])
    print(employee.employee_data())
    print("\n\n\n==================\n\n\n")
    print(employee.todo_list())
    print("\n\n\n==================\n\n\n")
    print(employee.todo_progress())
