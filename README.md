# Инструкция по запуску

+ Клонировать репозиторий:

    ```bash
    git clone https://github.com/13WIZORbro/Razum-2.0/tree/develop
    ```

+ Создать файл `.env` на основе `.env.example`:

    ```bash
    cp .env.example .env
    ```

+ Опционально: поменять значение переменных в `.env`

+ Запустить docker контейнер:

    ```bash
    docker compose up
    ```

+ Для создания пользователя с ролью админ:

    ```bash
    docker compose exec web python3 django-admin createsuperuser
    ```

+ Главная страница приложения находится на [http://0.0.0.0:8000](http://0.0.0.0:8000)

+ Админская панель на [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)
