import pandas as pd


def save_data(data):
    data_note = pd.DataFrame(data)
    data_note.to_csv('notebook1.csv', index=False, sep=';')


def load_data():
    lst = []
    data = pd.read_csv('notebook1.csv', sep=";")
    for index, row in data.iterrows():
        note = {}
        note['id'] = int(row['id'])
        note['title'] = row['title']
        note['text'] = row['text']
        note['date'] = row['date']
        lst.append(note)
    return lst
