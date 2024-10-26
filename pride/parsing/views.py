import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Tools
from django.core.paginator import Paginator


def index(request):
    tools = Tools.objects.all()
    paginator = Paginator(tools, 10)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {'tools': tools,
               'page_obj': page_objects,
               }
    return render(request, "main/index.html", context=context)


def parse_news_titles(url):
    # Отправляем GET-запрос к URL
    response = requests.get(url)

    if response.status_code == 200:
        # Парсим HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с классом 'news-title'
        titles = soup.find_all('p', class_='typography.heading.v2.-no-margin')
        print(titles, soup)
        # print(f'Ошибка при запросе: {response.status_code}')
        return [title.text.strip() for title in titles]
    else:
        print(f'Ошибка при запросе: {response.status_code}')
        return []


def news_view(request):
    url = 'https://www.vseinstrumenti.ru/product/nabor-alkalinovyh-batareek-gp-24aa21-2crswc24-24-shtuki-19904-15683542/'  # Укажите реальный URL
    titles = parse_news_titles(url)

    context = {
        'titles': titles,
    }

    return render(request, 'main/news.html', context)
