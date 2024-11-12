from encodings.utf_16 import encode

from icrawler.builtin import GoogleImageCrawler
import os
from PIL import Image, ImageDraw, ImageFont
from random import randint
import requests
import datetime


"""Функция для получения картинок города из Google"""
# def get_city_picture(city):
#
#     if not os.path.exists('city'):
#         os.mkdir('city')
#     request_word = city
#     google = GoogleImageCrawler(storage={'root_dir' : '/Users/anchesshumeyko/PycharmProjects/iMac_Anches/module_11/city'})
#     google.crawl(keyword=request_word, max_num=10)
#
# get_city_picture('Moscow')

"""Функция рандомно выбирает картинку из скаченных 10"""
# def choose_pic():
#     os.chdir('city')
#     filename = f'{str(randint(1,10)).zfill(6)}.jpg'
#     image = Image.open(filename)
#     image.show()
#     return filename
#
# choose_pic()

"""Функция изменяет размер картинки под необходимый размер для постера"""
def change_size(filename):
    os.chdir('city')
    fixed_width = 500
    poster_image = Image.open(filename)
    width_proportion = (fixed_width / float(poster_image.size[0]))
    height_size = int((poster_image.size[0]) * float(width_proportion))
    resized_image = poster_image.resize((fixed_width, height_size))
    return resized_image
#
# change_size('000010.jpg')

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
        return (f'{city}\nтемпература {round(temp)} C\nвлажность {humidity}%\nатмосферное давление {pressure} мм/рт ст'
                f'\nскорость ветра {wind} м/с')
    else:
        return f'невозможно получить ответ с сайта, просто выгляните в окно'

"""Формируем постер для города"""
# def make_poster()
date = datetime.date.today()
main_canvas = Image.new('RGB', (500, 1200), 'lightblue')
# poster = ImageDraw.Draw(main_canvas)
city_pic = change_size('000010.jpg')
#
drawer = ImageDraw.Draw(main_canvas)
text = get_weather('Tver')
drawer.text((10, 600), text=text, encode='utf-8', fill='black', font_size=30)
main_canvas.paste(city_pic, (0,0))
main_canvas.show()











