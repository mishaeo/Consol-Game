import commands

cdf_shadow_mode = False
cdf_mode = False
online_mode_characters = [False, True] # первое число игрок, а второе ии

print('Hello, it is the Hacker game! You need to enter the command "cdf.command.mode.on" for start')  # приветствие

command = input('Enter the command: ')  # ввод команды

if command == "cdf.command.mode.on":  # обработка старта режима cdf
    cdf_mode = True

while cdf_mode:  # цикл в режиме cdf_mode
    command = input('Enter the cdf command: ')  # ввод команды

    if command == "cdf.command.mode.off":  # обработка выхода из режима cdf
        cdf_mode = False
    elif command == "cdf.command.online": # обработка режима онлайн
        online_mode_characters = commands.cdf_online_mode(online_mode_characters)
    elif command == "cdf.command.shadow.mode": # обработка теневого режима
        cdf_shadow_mode = commands.cdf_shadow_mode(cdf_shadow_mode)
    elif command == "cdf.command.online.search.mode" and online_mode_characters[0]: # обработка режима поиска онлайн
        commands.cdf_online_search_mode()
    elif command == "cdf.command.online.search.mode" and online_mode_characters[0] == False:
        print('Online mod is off, try again!')
    elif command == "cdf.command.hack.mode" and online_mode_characters[0]: # обработка режима взлома
        commands.cdf_hack_mode(cdf_shadow_mode)
    elif command == "cdf.command.hack.mode" and online_mode_characters[0] == False:
        print('Online mod is off, try again!')
    else:
        print('Unknown command, try again!')  # обработка неизвестной команды



