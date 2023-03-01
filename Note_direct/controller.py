from datetime import datetime
import view
import processing
import write
def find_note():
    find_me = int(input("Введите id заметки: "))
    return find_me
# # Найти сотрудника
# def find_what_empl(what_find): #только одно слово - фамилия
#     return [i for i in what_find if i['id'] == what_find]
# print(len(find_what_empl('')))
def create_note():
    new_note = {'id':''}
    new_note['title'] = input('Введите заголовок: ')
    new_note['text'] = input('Введите текст: ')
    new_note['date'] = datetime.now().strftime("%d-%m-%Y")
    print(new_note)
    return new_note
def update_note(all_note, input_id):
    for i in all_note:
        if i['id'] == input_id:
            i['title'] = input('Введите новый заголовок: ')
            i['text'] = input('Введите новый текст: ')
            i['date'] = datetime.now().strftime("%d-%m-%Y")

def print_all_note(controller):
    view_note_print = []
    for i in range(len(controller)):
        notes = list(controller[i].values())
        notes.pop(0)
        view_note_print.append(notes)
        print(view_note_print)
def delete_note(all_notes, id):
    inx = None
    for i in range(len(all_notes)):
        if all_notes[i]['id'] == id:
            inx = i
            break
    del all_notes[inx]
    print("Записка удалена")





