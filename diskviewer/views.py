from typing import Any
import io
import zipfile
from django.http import FileResponse
from django.http import (HttpResponseRedirect, HttpResponse, HttpRequest)
from django.shortcuts import (render, redirect)
import requests


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'diskviewer/index.html')


def file_list(request: HttpRequest) -> HttpResponse:
    public_key = request.POST.get(
        'public_key') or request.GET.get('public_key')
    file_type = request.GET.get('file_type', 'all')
    api_url = 'https://cloud-api.yandex.net/v1/disk/public/resources'
    params = {'public_key': public_key}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Проверяем, является ли ресурс файлом
        if 'file' in data:
            # Это файл, передаем его как единственный элемент
            file_info = {
                'name': data['name'],
                'path': data['path'],
                'type': 'file'
            }
            return render(request, 'diskviewer/file_list.html', {
                # Отображаем файл как единственный элемент
                'items': [file_info],
                'public_key': public_key,
                'file_type': 'file'  # Устанавливаем тип файла
            })

        elif '_embedded' in data:
            # Это директория, обрабатываем как список файлов
            items = data['_embedded']['items']

            # Фильтруем файлы по типу, если указано
            if file_type != 'all':
                items = [item for item in items if item['type'] == file_type]

            return render(request, 'diskviewer/file_list.html', {
                'items': items,
                'public_key': public_key,
                'file_type': file_type
            })
        else:
            return HttpResponse("Неизвестный тип ресурса")

    return HttpResponse("Ошибка при получении данных с Яндекс.Диска")


def download_file(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает скачивание выбранного файла.
    """
    public_key = request.GET.get('public_key')
    path = request.GET.get('path')
    api_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download'
    params = {'public_key': public_key, 'path': path}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        download_url = response.json()['href']
        return HttpResponseRedirect(download_url)
    else:
        return HttpResponse("Ошибка при скачивании файла")


def download_multiple(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        public_key = request.POST.get('public_key')
        paths = request.POST.getlist('paths')
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for path in paths:
                api_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download'
                params = {'public_key': public_key, 'path': path}
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    download_url = response.json()['href']
                    file_content = requests.get(download_url).content
                    file_name = path.split('/')[-1]
                    zip_file.writestr(file_name, file_content)
        zip_buffer.seek(0)
        response = FileResponse(
            zip_buffer, as_attachment=True, filename='files.zip')
        return response
    else:
        return HttpResponse("Некорректный запрос")
