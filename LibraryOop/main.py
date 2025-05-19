import os
from opition import first_opition, user_opition
from classes.studente import Student


list_user = []
msg = ''


while True:
    msg_confg = f"\n{msg}\n" if msg else msg
    print(f"{first_opition} {msg_confg}")
    msg = ''

    value_option = input('Opition = ').lower()
    os.system('cls')

    if value_option == '1':
        while True:
            os.system('cls')
            msg_confg = f"\n{msg}\n" if msg else msg
            print(user_opition, msg_confg)

            value_option_user = input('Opition = ').lower()
            valida_value = ['1', '2', '3']

            if value_option_user not in valida_value:
                msg = '❌ Velue not valid'
                continue

            if value_option_user == '3':
                os.system('cls')
                msg = ''
                break

            name = input('Name = ')
            age = input('Age = ')

            if age.isalpha():
                msg = '❌ Please, Put only NUMBER for Age'
                continue

            if not name.isalpha():
                msg = '❌ Please, Put only LETTER for Name'
                continue
            

            if value_option_user == '1':
                user = Student(name, int(age))
                user.id = 0
                msg = f'✔️  Student "{user.name}" Registered'
                list_user.append(user)
                continue

            # if value_option_user == '2'
            #     user = Student(name, int(age))
            #     msg = f'✔️  Professor "{user.name}" Registered'

    if value_option == '2':
        while True:
            if list_user:
                print(f'Total: {len(list_user)}\n')

                for user in list_user:
                    print(f'id: {user.id} Name: {user.name}')

                    if user.books:
                        for book in user.books:
                            # print(f'{book.name},{ book.genre}')
                            print(book)
                    else:
                        print('Books: 0\n')
            else:
                msg = '❌ Nathing to list'
                break

            input()
            os.system('cls')
            break

    if value_option == 's':
        os.system('cls')
        break
    # os.system('cls')
