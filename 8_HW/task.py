from os import path

file_base = "Phone_book.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

        return all_data


def show_all():

    if not all_data:
        print("Пустой файл! Записей не существует.")
    else:
        print(*all_data, sep="\n")


def add_new_contact():

    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись создана!\n")
    else:
        print("Такая запись уже существует!")


def del_contact():

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Не корректный ввод!")


def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Запись уже существует!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена!\n")


def search_contact():
    search_data = exist_contact(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Не корректный ввод!")


def exist_contact(rec_id, data):

    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) < 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" no more than 11 digits\n"
                       f"Enter a {num}: ")
    return answer


def main_menu():

    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Показать все записи\n"
                       "2. Добавить запись\n"
                       "3. Поиск по контактам\n"
                       "4. Изменить запись\n"
                       "5. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                play = False
            case _:
                print("Try again!\n")


def edit_menu():

    add_dict = {"1": "surname", "2": "name",
                "3": "patronymic", "4": "phone number"}

    show_all()
    record_id = input("Введите id записи: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. Фамилия: \n"
                           "2. Имя: \n"
                           "3. Отчество: \n"
                           "4. Номер телефона: \n"
                           "5. Выход: \n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Не правильный ввод. Повторите.")
    else:
        print("Не корректные данные!")


main_menu()

## Доразобраться
##
##
##

# def exp_bd(name):

#     symbol = "\n"

#     change_name = f"{name}.txt"
#     if not path.exists(change_name):
#         with open(change_name, "w", encoding="utf-8") as f:
#             f.write(f'{symbol.join(all_data)}\n')


# def ipm_bd(name):
#     global file_base

#     if path.exists(name):
#         file_base = name
#         read_records()


# def exp_imp_menu():

#     while True:
#         print("\nExp/Imp menu:")
#         move = input("1. Import\n"
#                      "2. Export\n"
#                      "3. exit\n")

#         match move:
#             case "1":
#                 ipm_bd(input("Enter the name of the file: "))
#             case "2":
#                 exp_bd(input("Enter the name of the file: "))
#             case "3":
#                 return 0
#             case _:
#                 print("The data is not recognized, repeat the input.")


