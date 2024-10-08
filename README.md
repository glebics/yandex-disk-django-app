
# Yandex Disk Django App

## Описание

Данный проект является веб-приложением на Django для работы с API Яндекс.Диска. Приложение позволяет пользователям просматривать файлы и папки по публичной ссылке и скачивать выбранные файлы на локальный компьютер. Если по публичной ссылке передан конкретный файл, он сразу отображается как единственный элемент. Также реализована фильтрация файлов по типу.

### Выполненные задачи

- **Интеграция с API Яндекс.Диска**: реализовано взаимодействие с публичными ссылками через REST API Яндекс.Диска.
- **Просмотр файлов и папок**: приложение отображает список файлов и папок, если по ссылке передана директория.
- **Скачивание файлов**: пользователи могут выбирать и скачивать отдельные файлы.
- **Обработка файловых ссылок**: если по ссылке передан конкретный файл, он автоматически отображается для скачивания.
- **Фильтрация файлов**: реализована возможность фильтрации файлов по типу (файлы или папки).
- **Обработка ошибок**: приложение корректно обрабатывает ошибки, возникающие при получении данных с Яндекс.Диска.

## Установка и запуск проекта

### Шаги по установке

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/glebics/yandex-disk-django-app.git
   cd yandex-disk-django-app
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных (хотя миграции не используются в этом проекте, команда обязательна для Django):

   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

6. Перейдите в браузер по адресу:

   ```
   http://localhost:8000
   ```

### Использование

1. Введите публичную ссылку на Яндекс.Диск на главной странице.
2. Просмотрите список файлов и папок, если это директория.
3. Выберите и скачайте файлы, если они доступны.
4. Если по ссылке передан конкретный файл, он будет отображен для скачивания.

### Автор

**Рахимжанов Глеб Дмитриевич**  
Специально для компании Mycego.
