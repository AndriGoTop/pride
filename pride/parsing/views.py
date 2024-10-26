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



def parsing_site(request):
    # URL страницы с товарами
    url = "https://www.leroymerlin.ru/catalogue/stroymaterialy/"

    # Заголовки для маскировки под реального пользователя
    headers = {
        "Accept": '*/*',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все блоки с товарами
    products = soup.find_all("div", class_="product-card")

    # Проход по каждому товару и сохранение его данных
    for product in products:
        title = product.find("span", class_="product-card-name").get_text(strip=True)
        price_text = product.find("span", class_="price").get_text(strip=True)
        url = product.find("a", class_="product-card-link")["href"]

        # Очистка и преобразование цены
        try:
            price = float(price_text.replace("₽", "").replace(" ", "").replace(",", "."))
        except ValueError:
            price = None  # Если цена не найдена, устанавливаем None

        # Сохранение данных о товаре в базе данных
        Tools.objects.update_or_create(
            url=url,  # используем URL как уникальный идентификатор
            defaults={
                "title": title,
                "price": price,
                "image_url": product.find("img")["src"] if product.find("img") else None,
            }
        )

    # Отображение сохранённых товаров на странице
    products = Tools.objects.all()
    return render(request, 'main/products.html', {'products': products})


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

def tools(request, tool_id):
    tool = Tools.objects.get(pk=tool_id)
    context = {'tool': tool}
    return render(request, 'main/tool.html', context=context)

def news_view(request):
    url = 'https://www.vseinstrumenti.ru/product/nabor-alkalinovyh-batareek-gp-24aa21-2crswc24-24-shtuki-19904-15683542/'  # Укажите реальный URL
    titles = parse_news_titles(url)

    context = {
        'titles': titles,
    }

    return render(request, 'main/news.html', context)
