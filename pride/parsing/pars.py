import requests
from bs4 import BeautifulSoup
# import json
import time


# URL страницы, которую нужно спарсить
def pars_rostovinstrument():
    url_base = "https://rostovinstrument.ru/catalog/elektroinstrument/"  # Замените URL на конкретную страницу товаров

    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    # Выполняем запрос на получение HTML-кода страницы
    response = requests.get(url_base, headers=headers)
    response.raise_for_status()  # Проверка успешности запроса

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Список для хранения данных о товарах
    catalog = []
    # Поиск элементов товаров
    products = soup.find_all(
        "div", class_="list_item_wrapp item_wrap item"
    )  # Замените 'product-card' на правильный класс
    for product in products:
        # Извлекаем название товара
        name_tag = product.find("span")
        name = name_tag.text.strip() if name_tag else "Название не найдено"

        # Извлекаем цену товара+
        price_tag = product.find("span", class_="price_value")
        price = price_tag.text.strip() if price_tag else "Цена не указана"
        # Извлекаем ссылку на изображение товара
        image_tag = "https://rostovinstrument.ru" + str(product.find("img").get("data-src"))
        image = image_tag if image_tag else "Изображение отсутствует"
        url = "https://instrumentdon.ru" + str(product.find('a').get("href"))
        # Добавляем данные о товаре в каталог
        catalog.append({"name": name, "price": price, "image": image, "url": url})

        # Задержка между запросами (по желанию)
    return (catalog)


def pars_obi():
    url = "https://obi.ru/instrument"  # Замените URL на конкретную страницу товаров
    max_pages = 100
    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    # Список для хранения данных о товарах
    catalog = []
    for page in range(1, max_pages + 1):
        url = f'{url}?PAGEN_1={page}'
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        soup = BeautifulSoup(response.text, "html.parser")

        # Поиск элементов товаров
        products = soup.find_all(
            "div", class_="FuS7R"
        )
        for product in products:
            # Извлекаем название товара
            name_tag = product.find(class_='_1UlGi').text.strip()
            name = name_tag if name_tag else "Название не найдено"
            # Извлекаем цену товара+
            price_tag = product.find(class_="_3IeOW").text.strip()[:-1]
            price = price_tag if price_tag else "Цена не указана"
            # Извлекаем ссылку на изображение товара
            image_tag = str(product.find(class_="_2yMrf _3bk5Y"))[47:167]  # !!! НЕ ТРОГАТЬ, РАБОТАЕТ !!!
            image = image_tag if image_tag else "Изображение отсутствует"
            # Извлекаем ссылку на товар
            url = 'https://obi.ru/' + str(product.find('a').get('href'))
            # Добавляем данные о товаре в каталог
            catalog.append({"name": name, "price": price, "image": image, "url": url})
            # Задержка между запросами (по желанию)

    return (catalog)


def pars_instrumentdon():
    url_base = "https://instrumentdon.ru/catalog/"  # Замените URL на конкретную страницу товаров
    max_pages = 10
    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    all_data = []

    for page in range(1, max_pages + 1):
        # Формируем URL для текущей страницы
        url_base = f"{url_base}?PAGEN_1={page}"
        response = requests.get(url_base, headers=headers)

        # Проверяем успешность запроса
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Пример извлечения данных (предположим, что данные находятся в элементах с классом 'item')
            items = soup.find_all(class_='item_block col-4 col-md-3 col-sm-6 col-xs-6')  # Замените на реальный класс
            for item in items:
                name = item.find(class_='item-title').text.strip()  # Замените на реальный класс
                price = item.find(class_='price_value').text.strip()  # Замените на реальный класс
                image = "https://instrumentdon.ru/" + str(item.find("img").get("data-src"))
                url = "https://instrumentdon.ru" + str(item.find('a').get("href"))
                # Проверяем наличие изображения
                image = image if image else "Изображение отсутствует"
                all_data.append({
                    'name': name,
                    'price': price,
                    'image': image,
                    "url": url,
                })

        else:
            print(f"Ошибка при загрузке страницы {page}: {response.status_code}")
        # time.sleep(1)
    return all_data