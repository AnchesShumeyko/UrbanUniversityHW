import logging
import telegram_api  # файл с сохраненным токеном бота
import crud_functions2  # файл с функциями для работы с БД
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = telegram_api.TOKEN
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# получение продуктов из базы данных
products = crud_functions2.get_all_products()

# логирование с выводом информации в консоль
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

start_router = Router()


# создан класс состояний для регистрации пользователей
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# создан класс состояний для подсчета калорий
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создание основных кнопок меню
kb_list = [
    [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='ИНФОРМАЦИЯ')
    ],
    [
        KeyboardButton(text='Купить')
    ],
    [
        KeyboardButton(text='РЕГИСТРАЦИЯ')
    ]
]
kb = ReplyKeyboardMarkup(
    keyboard=kb_list,
    resize_keyboard=True,
    one_time_keyboard=True,
)

# создание кнопок инлайн меню для расчета калорий и выэова формулы
kb2_list = [
    [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    ],
    [
        InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
    ]
]
kb2 = InlineKeyboardMarkup(inline_keyboard=kb2_list, one_time_keyboard=True)

kb_add_list = [
    [
        InlineKeyboardButton(text='для  женщин', callback_data='female')
    ],
    [
        InlineKeyboardButton(text='для мужчин', callback_data='male')
    ]
]
kb_add = InlineKeyboardMarkup(inline_keyboard=kb_add_list, one_time_keyboard=True)

# создание инлайн меню покупки витаминов
kb3_list = [
    [
        InlineKeyboardButton(text='Вит А', callback_data='product_buying'),
        InlineKeyboardButton(text='Вит Д', callback_data='product_buying'),
        InlineKeyboardButton(text='Вит Е', callback_data='product_buying'),
        InlineKeyboardButton(text='Вит К', callback_data='product_buying')
    ]
]
kb3 = InlineKeyboardMarkup(inline_keyboard=kb3_list, one_time_keyboard=True, input_field_placeholder="Выберите продукт")

'''Handlers'''


# функция для регистрации пользователя(реагирующая на ввод Регистрация)
@start_router.message(F.text == 'РЕГИСТРАЦИЯ')
async def sign_up(message: Message, state: FSMContext):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)


# функция из цепочки состояний, запоминающая пользователя и проверяющая на уникальность
@start_router.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if not crud_functions2.is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await state.set_state(RegistrationState.username)


# функция из цепочки состояний, запоминающая email, введена простенькая валидация email
@start_router.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    if '@' in message.text:
        await state.update_data(email=message.text)
        await message.answer('Введите свой возраст:')
        await state.set_state(RegistrationState.age)
    else:
        await message.answer('Неверно введен email, попробуйте еще раз')
        await state.set_state(RegistrationState.email)



# функция из цепочки состояний, запоминаюшая возраст и вызывающая запись в базу данных
# введена проверка на то, что человек ввел число
@start_router.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        if isinstance(int(message.text), int):
            await state.update_data(age=message.text)
            data = await state.get_data()
            crud_functions2.add_user(data['username'], data['email'], data['age'])
            await message.answer("Поздравляем! Регистрация выполнена!", reply_markup=kb)
            await state.clear()
    except ValueError:
        await message.answer('Введите возраст числом!')
        await state.set_state(RegistrationState.age)


@start_router.message(F.text == 'Купить')
async def get_buying_list(message):
    for product in products:
        price = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}\n"
        await message.answer(price)
        await message.answer_photo(FSInputFile(f'pictures/{product[1]}.png'))
    await message.answer("Выберите продукт для покупки:", reply_markup=kb3)


@start_router.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb)


@start_router.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@start_router.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    await call.message.answer("Выберите для кого считать!", reply_markup=kb_add)


@start_router.callback_query(F.data == 'female')
async def get_formulas(call: CallbackQuery):
    formula = 'Для женщин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161'
    await call.message.answer(text=formula, reply_markup=kb)


@start_router.callback_query(F.data == 'male')
async def get_formulas(call: CallbackQuery):
    formula = 'Для мужчин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5'
    await call.message.answer(text=formula, reply_markup=kb)


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
    calories_m = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + 5
    await message.answer(f"суточная норма:\nдля женщины - {calories_f}\nдля мужчины - {calories_m}", reply_markup=kb)
    await state.clear()

@start_router.message(F.text == 'ИНФОРМАЦИЯ')
async def take_info(message: Message):
    info = "Это учебный бот, просто протестируйте функции"
    await message.answer(info, reply_markup=kb)

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
