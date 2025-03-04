import commands
import time
import random

# user-m-41x-f25-8y3-k19
# ai-f-62r-v73-0m3-23d

cdf_Mode = False
cdf_Hack = False
cdf_Commands = False
cdf_Online_Surch = False
cdf_Safe_Mode = False
cdf_Online = [0] * 2

cdf_Online[1] = 1

while not cdf_Mode:
    text = input('Enter command: ')
    if text == 'cdf>Mode=On':
        cdf_Mode = commands.cdf_mode_on(cdf_Mode)
    else:
        print('# The command is not corect! #')

while cdf_Mode:
    text = input('Enter <cdf> command: ')
    if text == 'cdf>Mode=Off':
        cdf_Mode = commands.cdf_mode_off(cdf_Mode)
    elif text == 'cdf>Online=On':
        cdf_Online = commands.cdf_online_on(cdf_Online)
    elif text == 'cdf>Online=Off':
        cdf_Online = commands.cdf_online_off(cdf_Online)
    elif text == 'cdf>Online=Surch=On':
        cdf_Online_Surch = commands.cdf_online_surch_on(cdf_Online_Surch, cdf_Online)
    elif text == 'cdf>Hack':
        cdf_Hack = commands.cdf_hack(cdf_Hack, cdf_Safe_Mode)
    elif text == 'cdf>Commands':
        cdf_Commands = commands.cdf_commands(cdf_Commands)
    elif text == 'cdf>Safe=Mode=On':
        cdf_Safe_Mode = commands.cdf_safe_mode_on(cdf_Safe_Mode)
    elif text == 'cdf>Safe=Mode=Off':
        cdf_Safe_Mode = commands.cdf_safe_mode_off(cdf_Safe_Mode)
    else:
        print('# The command is not corect! #')