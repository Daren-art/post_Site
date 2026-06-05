Простой блог на Django, где пользователи могут просматривать посты, читать их полностью и просматривать категории.

## Возможности

- Просмотр списка постов
- Страница отдельного поста
- Админ-панель Django
- Адаптивный интерфейс

## Технологии

- Python 3
- Django
- SQLite
- HTML
- CSS

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/Daren-art/post_Site


Создайте виртуальное окружение:

python -m venv venv

Активируйте его:

Windows:

venv\Scripts\activate

Linux/MacOS:

source venv/bin/activate

Установите зависимости:

pip install -r req.txt

Выполните миграции:

python manage.py migrate

Запустите сервер:

python manage.py runserver

Откройте в браузере:

http://127.0.0.1:8000/