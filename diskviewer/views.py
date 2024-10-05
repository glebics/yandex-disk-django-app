from django.http import (HttpResponseRedirect, HttpResponse, HttpRequest)
from django.shortcuts import (render, redirect)
import requests


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'diskviewer/index.html')


def file_list(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает ввод публичной ссылки и отображает список файлов.
    """
    if request.method == 'POST':
        public_key = request.POST.get('public_key')
        api_url = 'https://cloud-api.yandex.net/v1/disk/public/resources'
        params = {'public_key': public_key}
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            items = data['_embedded']['items']
            return render(request, 'diskviewer/file_list.html', {'items': items, 'public_key': public_key})
        else:
            return HttpResponse("Ошибка при получении данных с Яндекс.Диска")
    else:
        return redirect('index')


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
