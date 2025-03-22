import time
import random

def cdf_online_mode(character):
    command = input('Enter the code of character: ')  # ввод кода персонажа

    if command == "code:123": # игрок
        if character[0]:
            character[0] = False
            print('You are not online!')
        else:
            character[0] = True
            print('You are online!')
        return character
    elif command == "code:456": # ии
        if character[1]:
            character[1] = False
            print('AI are not online!')
        else:
            character[1] = True
            print('AI are online!')
        return character
    else:
        print('The code is not correct!')

def cdf_shadow_mode(shadow_mode):
    if shadow_mode:
        safe_mode = False
        print('Shadow mode is off')
        return safe_mode
    else:
        safe_mode = True
        print('Shadow mode is on')
        return safe_mode
