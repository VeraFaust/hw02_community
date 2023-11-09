### Описание:
Социальная сеть блогеров. В ней пользователи могут создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи.

### Технологии:
- Python;
- Django;

### Ход работы:
- В корне проекта установить и активировать виртуальное окружение:
```
python(или py) -m venv venv - установка
source venv/Scripts/activate - активация
```
- Через менеджер пакетов pip установить Django:
```
python3(или py) -m pip install --upgrade pip - обновление менеджера пакетов pip
pip install Django==2.2.19 - установка Django версии 2.2.19
```
- Создать основу проекта:
```
django-admin startproject name_project
```
- Запустить dev-сервера и создать первый коммит:
```
cd name_folder с файлом manage.py
python3 manage.py runserver
Перейти по адресу http://127.0.0.1:8000/
Остановить работу Ctrl+C
```
- Создать файл .gitignore и поместить в него всё, что не нужно отправлять в Git:
```
Например: .vscode/, venv/
```
- Сохранить зависимости:
```
pip freeze > requirements.txt
pip install -r requirements.txt - установка всех пакетов из файла requirements.txt
```
- Отправить проект на GitHub:
```
git add . - добавление новых и измененных файлов
git commit -m 'text' - сохранение изменений
git push - отправка коммита на сервер
```
## Автор
Вера Фауст
