def user_command():
    number = int(input("Ввод: \n 1. Если вы хотите создать записку: \n 2. Если вы хотите изменить записку:"
                       "\n 3. Если вы хотите посмотреть записку по id: \n 4. Если вы хотите посмотреть записку по дате: \n"
                       " 5. Если вы хотите удалить записку: \n 6. Посмотреть все записки: \n 7. Выход из меню: \n"
                       "Введите цифру: "))
    if 0 < number < 8:
        return number
    else:
        print(int(input("Некорректный ввод! Введите число от 1 до 7  ")))
from tabulate import tabulate  ## Таблица для вывода всех контактов
def print_all_notes(notes):
    data_to_print = []
    for i in range(len(notes)):
        listik = list(notes[i].values())
        listik.pop(0)
        data_to_print.append(listik)

    col_names = ["id", "Заголовок", "Текст", "Дата"]
    print(tabulate(data_to_print, headers=col_names, tablefmt='double_grid', showindex="always"))