import sys

repo = open('repo_beta.py', 'r+')
exxit = False
old_data = repo.read()

new_data = old_data.replace('}', '    "')

while not exxit:
    program_name = input('Название программы: ')
    if program_name == 'xxsit': break
    command = input('Команда: ')
    new_data += program_name + '": "' + command + '",\n'

new_data += "}"
repo.write(new_data)