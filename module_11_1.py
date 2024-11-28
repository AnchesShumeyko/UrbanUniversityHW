from icrawler.builtin import GoogleImageCrawler
import os
from PIL import Image, ImageDraw, ImageFont
from random import randint
import requests
import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CITY_DIR = os.path.join(ROOT_DIR, 'city')

"""Функция для получения картинок города из Google"""


def get_city_picture(city):
    if not os.path.exists(CITY_DIR):
        os.makedirs(CITY_DIR)
    request_word = city
    google = GoogleImageCrawler(storage={'root_dir': CITY_DIR})
    google.crawl(keyword=request_word, max_num=10)


"""Чистим директорию"""


def clear_directory():
    for f in os.listdir(CITY_DIR):
        file_path = os.path.join(CITY_DIR, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Не удалось удалить файл {file_path}: {e}')


"""Функция рандомно выбирает картинку из скаченных 10"""


def choose_pic():
    filename = f'{randint(1, 10):06d}.jpg'
    return os.path.join(CITY_DIR, filename)


"""Функция изменяет размер картинки под необходимый размер для постера"""


def change_size(picture):
    fixed_width = 500
    poster_image = Image.open(picture)
    width_proportion = fixed_width / float(poster_image.size[0])
    height_size = int(float(poster_image.size[1]) * width_proportion)
    resized_image = poster_image.resize((fixed_width, height_size))
    resized_image.save(os.path.join(CITY_DIR, 'poster_picture.jpg'))
    return 'poster_picture.jpg'


"""Получение погоды необходимого города"""


def get_weather(city):
    api_key = 'here was a key'
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={api_key}'
    try:
        r = requests.get(api_call)
    except Exception as e:
        return f'Ошибка при получении данных с сервера: {e}'
    json_object = r.json()
    temp = float(json_object['main']['temp']) - 273
    pressure = json_object['main']['pressure']
    humidity = json_object['main']['humidity']
    wind = json_object['wind']['speed']
    return (f'{city.capitalize()}\n\nтемпература {round(temp)} C\nвлажность {humidity}%\nдавление {pressure} mmHg'
            f'\nскорость ветра {wind} м/с')


"""Формируем постер для города"""


def make_poster(text, city):
    date = datetime.date.today()
    main_canvas = Image.new('RGB', (500, 900), 'lightblue')
    drawer = ImageDraw.Draw(main_canvas)
    # font = 'Courier New'
    font = ImageFont.truetype("Courier New", size=18)

    drawer.multiline_text((10, 600), text=text, fill='black', font=font, font_size=30)
    image1 = Image.open(os.path.join(CITY_DIR, 'poster_picture.jpg'))
    main_canvas.paste(image1, (0, 0))
    save_path = os.path.join(ROOT_DIR, f'{city}-{date}.jpg')
    main_canvas.save(save_path)
    main_canvas.show()


def main(city):
    get_city_picture(city)
    picture = choose_pic()
    change_size(picture)
    weather = get_weather(city)
    make_poster(weather, city)
    clear_directory()


if __name__ == '__main__':
    main('Москва')
