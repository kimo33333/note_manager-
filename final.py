notes = []
name = input("Введите ваше имя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: ")
creation_date = input("Введите дату создания заметки: ")
modification_date = input("Введите дату изменения заметки: ")
titles = []
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
titles.append(title1)
titles.append(title2)
note = {
    "username": name,
    "content": content,
    "status": status,
    "created_date": creation_date,
    "issue_date": modification_date,
    "titles": titles
}
notes.append(note)
for note in notes:
    print("Имя пользователя:", note["username"])
    print("Содержание:", note["content"])
    print("Статус:", note["status"])
    print("Дата создания:", note["created_date"])
    print("Дата изменения:", note["issue_date"])
    print("Заголовки:", note["titles"])
