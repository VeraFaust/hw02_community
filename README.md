# Социальная сеть «Yatube»

## Описание:
Yatube - это социальная сеть.  
В этом проекте реализовано следующее:
- Создано и зарегистрировано приложение Posts;
- Подключена база данных;
- 10 последних записей выводятся на главную страницу;
- В админ-зоне пользователь может регистрироваться, публиковать новые записи или редактировать/удалять существующие.

## Технологии:
- Python;
- Django;
- Git;
- HTML;
- CSS;
- Bootstrap;
- Django ORM;
- SQL.

## Запуск проекта:
- Клонируйте репозиторий:
```
git clone https://github.com/VeraFaust/hw02_community.git
```
- Откройте папку с проектом в IDE:
```
cd hw02_community
```

- Установите и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```

- Установите зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

- В папке с файлом manage.py запустите миграции:
```
py manage.py makemigrations
```
```
py manage.py migrate
```

- В папке с файлом manage.py создайте админа и запустите проект:
```
py manage.py createsuperuser
```
```
python manage.py runserver
```
Перейти по ссылке:
- На сайт http://127.0.0.1:8000/
- В админ-зону http://127.0.0.1:8000/admin

Созданные посты и группы в админ-зоне, будут отображаться на сайте.

Остановить работу:
```
Ctrl+C
```

## Автор
Вера Фауст
