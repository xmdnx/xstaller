import sys

repo = open('repo_beta.py', 'r+')
exxit = False
old_data = repo.read()

new_data = old_data.replace('}', '    "')

while not exxit:
    program_name = input('Название программы: ')
    if program_name == 'xxsit': sys.exit()
    number_of_comms = int(input('Кол-во комманд: '))
    comms = []
    for i in range(number_of_comms):
        comms[i] = input('Команда ' + str(i))

repo.write(new_data)