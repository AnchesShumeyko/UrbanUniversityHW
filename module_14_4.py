import logging
import telegram_api  # файл с сохраненным токеном бота
import crud_functions  # файл с функциями для работы с БД
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = telegram_api.TOKEN
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# получение продуктов из базы данных
products = crud_functions.get_all_products()

# логирование с выводом информации в консоль
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

start_router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Созание осноыныъ кнопок меню
kb_list = [
    [KeyboardButton(text='Рассчитать'),
     KeyboardButton(text='ИНФОРМАЦИЯ')],
    [KeyboardButton(text='Купить')]
]
kb = ReplyKeyboardMarkup(
    keyboard=kb_list,
    resize_keyboard=True,
    one_time_keyboard=True,
)

# создание кнопок инлайн меню для расчета калорий и выаодв формулы
kb2_list = [
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')]
]
kb2 = InlineKeyboardMarkup(inline_keyboard=kb2_list, one_time_keyboard=True)

# создание инлайн меню покупки витаминов
kb3_list = [
    [InlineKeyboardButton(text='Вит А', callback_data='product_buying'),
     InlineKeyboardButton(text='Вит Д', callback_data='product_buying'),
     InlineKeyboardButton(text='Вит Е', callback_data='product_buying'),
     InlineKeyboardButton(text='Вит К', callback_data='product_buying')]
]
kb3 = InlineKeyboardMarkup(inline_keyboard=kb3_list, one_time_keyboard=True, input_field_placeholder="Выберите продукт")


'''Handlers'''

@start_router.message(F.text == 'Купить')
async def get_buying_list(message):
    for product in products:
        price = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}\n"
        await message.answer(price)
        await message.answer_photo(FSInputFile(f'pictures/{product[1]}.png'))
    await message.answer("Выберите продукт для покупки:", reply_markup=kb3)


@start_router.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')


@start_router.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@start_router.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    formula = 'Для женщин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161'
    await call.message.answer(text=formula)


@start_router.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state):
    await call.message.answer('Введите свой возраст')
    await state.set_state(UserState.age)


@start_router.message(F.text, UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@start_router.message(UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@start_router.message(UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_f = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) - 161
    await message.answer(f"суточная норма для женщины - {calories_f}")
    await state.clear()


@start_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@start_router.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


# Основная функция для запуска бота
async def main():
    dp.include_router(start_router)  # стартуем роутер
    await bot.delete_webhook(drop_pending_updates=True)  # аналог skip_updates из aiogram 2x
    await dp.start_polling(bot)  # старт самого бота


if __name__ == "__main__":
    asyncio.run(main())
