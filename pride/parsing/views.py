from itertools import product
from .models import Tools
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .models import Tools
from django.core.paginator import Paginator
from .pars import pars_rostovinstrument
from django.http import JsonResponse
from .pars import pars_rostovinstrument, pars_instrumentdon, pars_obi


# def index(request):
#     tools = Tools.objects.all()
#     paginator = Paginator(tools, 10)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     context = {'tools': tools,
#                'page_obj': page_objects,
#                }
#     return render(request, "main/index.html", context=context)


# def parse_news_titles(url):
#     # Отправляем GET-запрос к URL
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         # Парсим HTML-код страницы
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Находим все элементы с классом 'news-title'
#         titles = soup.find_all('p', class_='typography.heading.v2.-no-margin')
#         print(titles, soup)
#         # print(f'Ошибка при запросе: {response.status_code}')
#         return [title.text.strip() for title in titles]
#     else:
#         print(f'Ошибка при запросе: {response.status_code}')
#         return []

def tools(request, tool_id):
    tool = Tools.objects.get(pk=tool_id)
    context = {'tool': tool,}
    return render(request, 'main/tool.html', context=context)
#
# def news_view(request):
#     url = 'https://www.vseinstrumenti.ru/product/nabor-alkalinovyh-batareek-gp-24aa21-2crswc24-24-shtuki-19904-15683542/'  # Укажите реальный URL
#     titles = parse_news_titles(url)
#
#     context = {
#         'titles': titles,
#     }
#
#     return render(request, 'main/news.html', context)


# В файле views.py или другом скрипте


# Функция для сохранения данных в базу
def save_data_to_db(catalog):
    for tool in catalog:
        if not Tools.objects.filter(name=tool['name']).exists():
            Tools.objects.create(
                name=tool.get('name'),
                price=tool.get('price'),
                image=tool.get('image'),
                url=tool.get('url'),
            )


# Основное представление, которое проверяет наличие данных и отображает их
def articles_list(request):
    # Сохранение данных
    # save_data_to_db(pars_instrumentdon())
    # save_data_to_db(pars_rostovinstrument())
    # save_data_to_db(pars_obi())



    # Проверка данных в базе
    data_exists = Tools.objects.exists()
    tools = Tools.objects.all()
    paginator = Paginator(tools, 10)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    # Получение всех записей
    articles = Tools.objects.all()
    context = {
        'articles': articles,
        'data_exists': data_exists, # Передаем проверку в шаблон
        'tools': tools,
        'page_obj': page_objects,
    }

    return render(request, 'main/index.html', context)

def run_parser():
    # Здесь вызываем ваш парсер
    pars_instrumentdon()
    pars_rostovinstrument()
    return JsonResponse({'status': 'Парсер выполнен и данные добавлены!'})

