from icrawler.builtin import GoogleImageCrawler
import os
from PIL import Image, ImageDraw
from random import randint
import requests
import datetime


"""Функция для получения картинок города из Google"""
def get_city_picture(city):

    if not os.path.exists('city'):
        os.mkdir('city')
    request_word = city
    google = GoogleImageCrawler(storage={'root_dir' : '/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/city'})
    google.crawl(keyword=request_word, max_num=10)
#

"""Чистим директорию"""
def clear_directory():
    os.chdir('/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/city')
    for f in os.listdir():
        if os.path.isfile(f):
            os.remove(f)

"""Функция рандомно выбирает картинку из скаченных 10"""
def choose_pic():
    filename = f'{str(randint(1,10)).zfill(6)}.jpg'
    return filename
#
# # choose_pic()
#
"""Функция изменяет размер картинки под необходимый размер для постера"""
def change_size(picture):
    os.chdir('/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/city')
    fixed_width = 500
    poster_image = Image.open(picture)
    width_proportion = (fixed_width / float(poster_image.size[0]))
    height_size = int((poster_image.size[0]) * float(width_proportion))
    resized_image = poster_image.resize((fixed_width, height_size))
    resized_image.save('poster_picture.jpg')
    return 'poster_picture.jpg'


"""Получение погоды необходимого города"""
def get_weather(city):
    api_key = 'e402c0d73ff9e18f6abce97a49a735e6'
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={api_key}'
    r = requests.get(api_call)
    if r.status_code == 200:
        json_object = r.json()
        temp = float(json_object['main']['temp']) - 273
        pressure = json_object['main']['pressure']
        humidity = json_object['main']['humidity']
        wind = json_object['wind']['speed']
        return (f'{city.capitalize()}\n\ntemperature {round(temp)} C\nhumidity {humidity}%\npressure {pressure} mmHg'
                f'\nwind speed {wind} m/s')
    else:
        return f'невозможно получить ответ с сайта, просто выгляните в окно'

"""Формируем постер для города"""
def make_poster(city_pic, text, city):
    date = datetime.date.today()
    main_canvas = Image.new('RGB', (500, 900), 'lightblue')
    drawer = ImageDraw.Draw(main_canvas)
    drawer.text((10, 600), text=text, fill='black', font_size=30)
    image1 = Image.open('/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/city/poster_picture.jpg')
    main_canvas.paste(image1,(0,0))
    main_canvas.save(f'/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/{city}-{date}.jpg')
    main_canvas.show()

def main(city):
    get_city_picture(city)
    picture = choose_pic()
    resized_picture = change_size(picture)
    weather = get_weather(city)
    make_poster(resized_picture, weather, city)
    clear_directory()

main('Moscow')


