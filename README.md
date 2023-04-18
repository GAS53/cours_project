Курсовой проект командная разработка.
=====================================

Запуск проекта:
1. ```> cd app```
2. ```> pip install -r requirements.txt```
3. Удалить db.sqlite3 (если есть)
4. ```> python manage.py migrate```
5. ```> python manage.py fill_db```<br>
или, если нужно заполнить всеми тестовыми данными:<br>
```> python manage.py fill_db --all```<br>
при полном заполнении БД заполнится тестовыми данными и создадутся пользователи с логинами 
```test1@test.com```<br>
```test2@test.com```<br>
```test3@test.com```<br>
и паролем<br>
```1234```<br>
Пользователь ```test1@test.com``` обладает аминистративными правами
6. ```>  python manage.py runserver```
