"""
Найти все полки в библиотеке, на которых стоят книги Ремарка.
"""


d1 = {
    "полка 1": ["три товарища", "1984"],
    "полка 2": ["убить пересмешника", "герой нашего времени"],
    "полка 3": ["10 негритят", "на западном фронте без перемен"]
}

d2 = {
    "1984": "оруэлл",
    "три товарища": "ремарк",
    "убить пересмешника": "ли",
    "герой нашего времени": "лермонтов",
    "10 негритят": "кристи",
    "на западном фронте без перемен": "ремарк"
}


def find_remarque(d1, d2):
    remarque_book = []
    for k in d1.keys():
        for v in d1[k]:
            if d2[v] == 'кристи':
                remarque_book.append(k)
                break

    return remarque_book


print(find_remarque(d1, d2))