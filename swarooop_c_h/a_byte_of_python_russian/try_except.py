try:
    text = input('Введите что-нибудь --> ')
except EOFError: # Нажмите ctrl + d
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt: # Нажмите ctrl + c
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))
