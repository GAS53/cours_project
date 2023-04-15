Курсовой проект командная разработка.
=====================================

Запуск проекта:
1. ```> cd app```
2. Удалить db.sqlite3 (если есть)
3. ```> python manage.py migrate```
4. ```> python manage.py fill_db```<br>
или, если нужно заполнить всеми тестовыми данными:<br>
```> python manage.py fill_db --all```
при полном заполнении БД заполнится тестовыми данными и создадутся пользователи с логинами 
```test1@test.com```<br>
```test2@test.com```<br>
```test3@test.com```<br>
и паролем<br>
```1234```
5. ```>  python manage.py runserver```
