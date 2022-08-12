#██   ██ ███    ███ ██████  ███    ██ 
# ██ ██  ████  ████ ██   ██ ████   ██ 
#  ███   ██ ████ ██ ██   ██ ██ ██  ██ 
# ██ ██  ██  ██  ██ ██   ██ ██  ██ ██ 
#██   ██ ██      ██ ██████  ██   ████

#            xmdn 2022
#            XSTALLER
# Full work guaranteed only on Ubuntu

import os, sys, time, xstallerrepo

# VARIABLES
ubuntu = True

# METHODS
def cls():
    os.system('clear')

## SETUP
cls()
print('Hey there! Are you sure you are using this program on Ubuntu?')
if input('Your answer (y/n): ') == 'n':
    print('In this case, technical support will not be provided! You may continue to use the program at your own risk.')
    ubuntu = False

# INSTALL DEPENDECIES
os.system('sudo apt install python3-pip')
os.system('pip3 install rich')

# IMPORT RICH
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install
install()

# SETUP TABLE
table = Table(title='Programs')
table.add_column('ID', style='bold cyan')
table.add_column('App Name', style='bold green')

for i in range(0, len(xstallerrepo.names)):
    table.add_row(str(i), xstallerrepo.names[i])

# SETUP THEME
custom_theme = Theme ({
    'good'     : 'bold green',
    'bad'      : 'bold red',
    'progress' : 'bold blue'
})

console=Console(theme=custom_theme)
cls()
console.print('Rich installed!', style='good')
    
# METHODS
def menu():
    cls()
    if not ubuntu: console.print('NOT UBUNTU MODE!', style='bad')
    console.print(table)
    id_for_install = input('Enter ID of app you want install: ')
    os.system(xstallerrepo.comms[int(id_for_install)])

menu()