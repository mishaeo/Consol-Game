import commands
import time
import random

cdf_mode = False
cdf_online = False
online_mode_characters = [False, True] # первое число игрок а второе ии

print('Hello, it is the Hacker game! You need to enter the command "cdf.command.mode.on"')  # приветствие

command = input('Enter the command: ')  # ввод команды

if command == "cdf.command.mode.on":  # условие команды
    cdf_mode = True

while cdf_mode:  # цикл в режиме cdf_mode
    command = input('Enter the cdf command: ')  # ввод команды

    if command == "cdf.command.mode.off":  # обработка выхода из режима
        cdf_mode = False
    elif command == "cdf.command.online.on": # обработка режима онлайн
        online_mode_characters = commands.cdf_online_mode(online_mode_characters)
    else:
        print('Unknown command, try again!')  # обработка неизвестной команды



