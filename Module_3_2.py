def send_email(message, recipient, *, sender="university.help@gmail.com"):
    check_recipient = ''
    check_sender = ''
    valid_addresses = ['.ru', '.com', '.net']
    valid_send_1 = False
    valid_send_2 = False
    if '@' in recipient and '@' in sender:
        for i in range(-4, 0, 1):
            check_recipient += recipient[i]
            check_sender += sender[i]
        for i in range(len(valid_addresses)):
            if valid_addresses[i] in check_recipient:
                valid_send_1 = True
            if valid_addresses[i] in check_sender:
                valid_send_2 = True
        if valid_send_1 and valid_send_2:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            elif sender != recipient:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'Нельзя отправить письмо самому себе!')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

#Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
#НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
#Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
#Нельзя отправить письмо самому себе!
