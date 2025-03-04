import time
import random

def cdf_commands(cdf_Commands):
    print('# cdf>Mode=On -> включает режим \'CDF\' #')
    print('# cdf>Mode=Off -> выключает режим \'CDF\' #')
    print('# cdf>Online=On -> позволяет войти в онлайн режим #')
    print('# cdf>Online=Off -> позволяет выйти из онлайн режим #')
    print('# cdf>Online=Surch=On -> позволяет войти в режим поиска в онлайне #')
    print('# cdf>Online=Surch=Off -> позволяет выйти из режим поиска в онлайне #')
    print('# cdf>Hack ->  позволяет взломать файл и получить ключ от него #')
    print('# cdf>Safe=Mode=On ->  позволяет включить режим защиты #')
    print('# cdf>Safe=Mode=Off ->  позволяет выключить режим защиты #')


def cdf_mode_on(cdf_Mode):
    cdf_Mode = True
    print('# cdf mode is on #')
    return cdf_Mode

def cdf_mode_off(cdf_Mode):
    cdf_Mode = False
    print('# cdf mode is off #')
    return cdf_Mode

def cdf_safe_mode_on(cdf_Safe_Mode):
    cdf_Safe_Mode = True
    print('# safe mode is on #')
    return cdf_Safe_Mode

def cdf_safe_mode_off(cdf_Safe_Mode):
    cdf_Safe_Mode = False
    print('# safe mode is off #')
    return cdf_Safe_Mode

def cdf_online_on(cdf_Online):
    while True:
        name_key = input('Enter name key: ')
        if name_key == 'user-m-41x-f25-8y3-k19':
            if cdf_Online[0] == 0:
                cdf_Online[0] = 1
                print('# You are online #')
                return cdf_Online
            else:
                print('# You are already online #')
                return cdf_Online
        elif name_key == 'ai-f-62r-v73-0m3-23d':
            if cdf_Online[1] == 0:
                cdf_Online[1] = 1
                print('# AI is online #')
                return cdf_Online
            else:
                print('# AI is already online #')
                return cdf_Online
        else:
            print('# The name isn\'t correct #')

def cdf_online_off(cdf_Online):
    while True:
        name_key = input('Enter name key: ')
        if name_key == 'user-m-41x-f25-8y3-k19':
            if cdf_Online[0] == 1:
                cdf_Online[0] = 0
                print('# You aren\'t online #')
                return cdf_Online
            else:
                print('# You aren\'t already online #')
                return cdf_Online
        elif name_key == 'ai-f-62r-v73-0m3-23d':
            if cdf_Online[1] == 1:
                cdf_Online[1] = 0
                print('# AI isn\'t online #')
                return cdf_Online
            else:
                print('# AI isn\'t already online #')
                return cdf_Online
        else:
            print('# The name isn\'t correct #')

def cdf_online_surch_on(cdf_Online_Surch, cdf_Online):
    if cdf_Online[0] == 1:
        cdf_Online_Surch = True
        while True:
            text = input('Enter road to file: ')
            if text == 'cdf>Online=Surch=Off':
                cdf_Online_Surch = False
                print('# Surch mode is off #')
                return cdf_Online_Surch
            else:
                pass
            if text[0] == 'p' and text[1] == 'l' and text[2] == 'a' and text[3] == ':':
                if text == 'pla:p8-n3-r2-1d-8a':
                    print('# The file surch, please wait... #')
                    time.sleep(10)
                    print('# The file was found # <ai-frili-v.5-26-70-15-78>')
                    cdf_Online_Surch = False
                    print('# Surch mode is off #')
                    return cdf_Online_Surch
                else:
                    print('# The file surch, please wait... #')
                    time.sleep(10)
                    print('# The file wasn\'t found #')
                    cdf_Online_Surch = False
                    print('# Surch mode is off #')
                    return cdf_Online_Surch
            else:
                print('The road isn\'t correct')
    else:
        print('# You aren\'t online #')


def cdf_hack(cdf_Hack, cdf_Safe_Mode):
    if cdf_Safe_Mode == True:
        cdf_Hack = True
        print('# cdf hack mode is on #')
        while cdf_Hack:
            text = input('Enter the file to hack: ')
            if text == 'ai-frili-v.5-26-70-15-78':
                for i in range(11):
                    i = i * 10
                    print('# The file is hack of', i, '% #')
                    time.sleep(6)
                print('# The file is hack, key is <ai-f-62r-v73-0m3-23d> #')

                cdf_Hack = False
                print('# cdf hack mode is off #')
                return cdf_Hack
            else:
                print('# The file not found #')
    else:
        cdf_Hack = True
        print('# cdf hack mode is on #')
        while cdf_Hack:
            text = input('Enter the file to hack: ')
            if text == 'ai-frili-v.5-26-70-15-78':
                for i in range(11):
                    random_number = random.randint(1, 10)
                    if random_number == 1 or random_number == 2:
                        print('# You were discovered by AI #')
                        print('!!!You lost!!!')
                        exit()
                    i = i * 10
                    print('# The file is hack of', i, '% #')
                    time.sleep(6)
                print('# The file is hack, key is <ai-f-62r-v73-0m3-23d> #')

                cdf_Hack = False
                print('# cdf hack mode is off #')
                return cdf_Hack
            else:
                print('# The file not found #')
