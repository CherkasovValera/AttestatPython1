
import write

from datetime import datetime
import controller
import view


def last_id(data):
    id_list = [int(i["id"]) for i in data]
    if len(id_list) != 0:
        return max(id_list) + 1
    else:
        return 1
# def delete_note(all_notes, id):
#     inx = None
#     for i in range(len(all_notes)):
#         if all_notes[i]['id'] == id:
#             inx = i
#             break
#     del all_notes[inx]

def what_note_id(what_find, data):
    idnex = 0
    targ = 0
    for i in data:
        if i['id'] == what_find:
            targ = idnex
        idnex += 1
    return data[targ]


def what_data(what_find, data):
    idnex = 0
    targ = 0
    for i in data:
        if datetime.strptime(i['date'], '%d-%m-%Y').date() == what_find:
            targ = idnex
        idnex += 1
    return data[targ]


def main_logic():
    running = True
    notes = write.load_data()
    while running:
        pos = view.user_command()
        if pos == 1:
            create_n = controller.create_note()
            create_n['id'] = last_id(notes)
            notes.append(create_n)
        elif pos == 2:
            controller.update_note(notes, int(input("Введите id: ")))
        elif pos == 3:
            id_what = controller.find_note()
            target = what_note_id(id_what, notes)
            # print(target)
            view.print_all_contacts(target)
        elif pos == 4:
            what_find = datetime.strptime(input("Введите дату  в формате 00-00-0000: "), "%d-%m-%Y").date()
            target = what_data(what_find, notes)
            print(target)
        elif pos == 5:
            controller.delete_note(notes, int(input("Введите id: ")))
        elif pos == 6:
            view.print_all_contacts(notes)
        elif pos ==7:
            running = False
            write.save_data(notes)
        else:
            print("Не правильный ввод команды")




