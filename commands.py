import time
import random

def cdf_online_mode(character):
    command = input('Enter the file of character: ')

    if command == '12-23-00-19-45': # файл игрока
        command = input('Enter the password of character: ')
        if command == '178-974-358-016': # пароль игрока
            if character[0]:
                character[0] = False
                print('You are not online')
                return character
            else:
                character[0] = True
                print('You are online')
                return character
        else:
            print('The password of character is not correct')
            return character

    elif command == '89-12-54-23-10': # файл ии
        command = input('Enter the password of character: ')
        if command == '432-128-541-874':  # пароль ии
            if character[1]:
                character[1] = False
                print('AI are not online')
                return character
            else:
                character[1] = True
                print('AI are online')
                return character
    else:
        print('The file of character is not correct')
        return character



def cdf_shadow_mode(shadow_mode):
    if shadow_mode:
        safe_mode = False
        print('Shadow mode is off')
        return safe_mode
    else:
        safe_mode = True
        print('Shadow mode is on')
        return safe_mode

def cdf_online_search_mode():
    command = input('Enter the path to the file: ')

    for i in range(11):
        number = random.randint(1, 8)
        time.sleep(number)
        print('Search in progress: ', i * 10, '%')

    if command == '861-324-694': # путь к данным ии
        print('Location of files: pflo:89-12-54-23-10')
    elif command == '758-050-841': # путь к данным
        print('Location of files: pflo:12-23-00-19-45')
    else:
        print('File location not found')


