import os
from opition import first_opition, user_opition
from classes.studente import Student


list_user = []
msg = ''


while True:
    # Msg user
    msg_confg = f"\n{msg}\n" if msg else msg
    print(f"{first_opition} {msg_confg}")
    msg = ''

    # Input option
    value_option = input('Opition = ').lower()
    os.system('cls')

    # Create a instance of studante and Professor
    if value_option == '1':
        while True:
            # Add a unic id for user
            def add_id(list_user: list) -> int:
                lis_id = [i.id for i in list_user]
                var = 1
                if lis_id:
                    for i in lis_id:
                        if i in lis_id:
                            var = i + 1
                return var

            # Msg for user
            os.system('cls')
            msg_confg = f"\n{msg}\n" if msg else msg
            print(user_opition, msg_confg)

            # input data option
            value_option_user = input('Opition = ').lower()
            valida_value = ['1', '2', '3']  # list to valide option

            # Valide if velue of input is in opition
            if value_option_user not in valida_value:
                msg = '❌ Velue not valid'
                continue

            # Exit
            if value_option_user == '3':
                os.system('cls')
                msg = ''
                break

            # input data user
            name = input('Name = ')
            age = input('Age = ')

            # Valide age
            if age.isalpha():
                msg = '❌ Please, Put only NUMBER for Age'
                continue

            # Valide name
            if not name.isalpha():
                msg = '❌ Please, Put only LETTER for Name'
                continue

            # Instance of studante
            if value_option_user == '1':
                user = Student(name, int(age))
                user.id = add_id(list_user)
                msg = f'✔️  Student "{user.name}" Registered'
                list_user.append(user)
                continue

            # Instance of professor
            # if value_option_user == '2'
                # user.id = add_id(list_user)
                # msg = f'✔️  Professor "{user.name}" Registered'
                # list_user.append(user)
                # continue

    # Show user and your books
    if value_option == '2':
        while True:
            if list_user:
                print(f'Total: {len(list_user)}\n')

                for user in list_user:
                    print(f'id:{user.id}  Name: {user.name}  Age = {user.age}')

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

    # Exit
    if value_option == 'e':
        os.system('cls')
        break
    # os.system('cls')
