import requests
from bs4 import BeautifulSoup
# import json
import time


# URL страницы, которую нужно спарсить
def pars_rostovinstrument():
    url = "https://rostovinstrument.ru/catalog/elektroinstrument/"  # Замените URL на конкретную страницу товаров

    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    # Выполняем запрос на получение HTML-кода страницы
    response = requests.get(url, headers=headers)
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

        # Добавляем данные о товаре в каталог
        catalog.append({"name": name, "price": price, "image": image})

        # Задержка между запросами (по желанию)
        time.sleep(1)
    return (catalog)

def pars_