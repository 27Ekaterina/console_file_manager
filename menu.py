import os
import shutil
import sys

os.getcwd()

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_directory = input('Введите название создаваемой папки: ')
        if not os.path.exists(f'{name_directory}'):
            os.mkdir(f'{name_directory}')

    elif choice == '2':
        while True:
            print('a. удалить файл')
            print('b. удалить папку')
            print('c. вернуться в главное меню')
            choice_in_2 = input('Выберите подпункт меню: ')
            if choice_in_2 == 'a':
                name_file = input('Введите название удаляемого файла: ')
                if os.path.exists(f'{name_file}'):
                    os.remove(f'{name_file}')
                else:
                    (print("Неверное имя файла"))
            elif choice_in_2 == 'b':
                name_delit_directory = input('Введите название удаляемой папки: ')
                if os.path.exists(f'{name_delit_directory}'):
                    shutil.rmtree(f'{name_delit_directory}')
                else:
                    (print("Неверное имя папки"))
            elif choice_in_2 == 'c':
                break
            else:
                print('Неверный пункт меню')

    elif choice == '3':
        while True:
            print('a. копировать файл')
            print('b. копировать папку')
            print('c. вернуться в главное меню')
            choice_in_3 = input('Выберите подпункт меню: ')
            if choice_in_3 == 'a':
                old_file = input("Введите название копируемого файла: ")
                new_file = input("Введите название копии файла: ")
                shutil.copy(old_file, new_file)
            elif choice_in_3 == 'b':
                old_dirctory = input('Введите название копируемой папки: ')
                new_dirctory = input('Введите название копии папки: ')
                shutil.copytree(old_dirctory, new_dirctory)
            elif choice_in_3 == 'c':
                break
            else:
                print('Неверный пункт меню')
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        path = os.getcwd()
        dirlist = []
        for root, dirs, files in os.walk(path):
            for dirname in dirs:
                dirlist.append(os.path.join(root,dirname))
        for name in dirlist:
            print("Папка", name)

    elif choice == '6':
        path = "C:/Users/Alex42/PycharmProjects/console_file_manager"
        filelist = []
        for root, dirs, files in os.walk(path):
            for file in files:
                filelist.append(os.path.join(root,file))
        for name in filelist:
            print("Файл", name)

    elif choice == '7':
        print(sys.platform)

    elif choice == '8':
        print(os.getlogin())

    elif choice == '9':
        import victory
    elif choice == '10':
        import use_functions
    elif choice == '11':
        print("Рабочая директория", os.getcwd())
        os.chdir('C:/Users/Alex42/PycharmProjects/dz4')
        print("Новая рабочая директория", os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')