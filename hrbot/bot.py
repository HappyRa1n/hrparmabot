import random
from asgiref.sync import sync_to_async
import asyncio
import logging
import hrbot.keyboards as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from hrbot.models import Work
from hrbot.models import City
from os import getenv
from sys import exit
from usersettings import  BOT_TOKEN
bot_token =BOT_TOKEN #Вписать свой токен getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

# Объект бота
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)

# Логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)
    await message.reply("Вы заблокированы")


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True
def CreateButtonsCity(use_map):
    data = City.objects.all()
    city_selection_keyboard = types.InlineKeyboardMarkup(row_width=1)
    types.InlineKeyboardButton(text="Пермь", callback_data="btn_13")
    s = 'btn_'
    if use_map:
        s = s + 'townmap'
    else:
        s = s + 'townwork'
    for v in data:
        city_selection_keyboard.add(types.InlineKeyboardButton(text=v.name, callback_data=s+str(v.id)))
    return city_selection_keyboard
def GetTown(index):
    s = City.objects.get(id=index)
    return s
def GetWork(index):
    s = Work.objects.get(id=index)
    return s
def GetBtnWorksByTown(index):
    works= Work.objects.filter(town=index)
    works_selection_keyboard = types.InlineKeyboardMarkup(row_width=1)
    if len(works) == 0:
        return -1
    for v in works:
        works_selection_keyboard.add(types.InlineKeyboardButton(text=v.name, callback_data="btn_work"+str(v.id)))
    return works_selection_keyboard
def test(essage: types.Message):
    data = Work.objects.all()
    s = random.choice(data)
    k= s.name
    return s.name
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
      await message.answer(
            f"Привет, <b>{message.from_user.first_name}</b>\nЧем могу помочь?",
            reply_markup=kb.start_keyboard
            )


@dp.callback_query_handler(text_startswith="btn_")
async def callbacks_num(call: types.CallbackQuery):
    btn_number = call.data.split("_")[1]
    loop = asyncio.get_event_loop()
    if btn_number == "where":

        city_selection_map = await loop.run_in_executor(None, CreateButtonsCity, True)
        await call.message.answer(
            "В каком городе ты находишься?",
            reply_markup=city_selection_map
        )
    elif btn_number == "about":
        await call.message.answer(
            "Группа компаний <b>PARMA Technologies Group</b> основана в 2016 году. "
            "Главным направлением деятельности является разработка заказного программного обеспечения.\n\n "
            "У нас собрана профессиональная команда, чей опыт работы на рынке информационных технологий составляет"
            "более 12 лет. Решениями, разработанными нашими специалистами, пользуются многие федеральные,"
            "региональные и муниципальные органы государственной власти.\n\n "
            'Подробности по <a href="https://www.parma.ru/">ссылке</a>',
            disable_web_page_preview=True
        )
    elif btn_number == "vacancies":
        city_selection_work = await loop.run_in_executor(None, CreateButtonsCity, False)
        await call.message.answer(
            "Вакансии в каком городе тебя интересуют?",
            reply_markup=city_selection_work
        )
    elif 'townmap' in btn_number:
        index = int(btn_number.replace('townmap',''))
        town = await loop.run_in_executor(None, GetTown, index)
        await call.message.answer_venue(
               town.latitude,
               town.longitude,
               "Адрес и геометка офиса компании:",
               town.address
            )
    elif 'townwork' in btn_number:
        index = int(btn_number.replace('townwork', ''))
        works_in_city = await loop.run_in_executor(None, GetBtnWorksByTown, index)
        if(works_in_city == -1):
            await call.message.answer(
                "На данный момент нет вакансий в этом городе",
            )
        else:
            await call.message.answer(
                "Какая из вакансий тебя интересует?",
                reply_markup=works_in_city
            )
    elif 'work' in btn_number:
        index = int(btn_number.replace('work', ''))
        work = await loop.run_in_executor(None, GetWork, index)
        await call.message.answer(work.name)
        await call.message.answer(work.description)
        if work.interview != "":
            await call.message.answer('Вы можете пройти первичное собеседование по ссылке: \n'+work.interview)
    await call.answer()
    #
    # elif btn_number == "4":
    #     await call.message.answer(
    #         "Отправьте своё резюме в этот чат, мы рассмотрим Вашу заявку и свяжемся с вами"
    #     )
    # elif btn_number == "5":
    #     await call.message.answer("Администратор баз данных")
    # elif btn_number == "6":
    #     await call.message.answer("Бизнес-архитектор")
    # elif btn_number == "7":
    #     await call.message.answer("Руководитель группы разработки")
    # elif btn_number == "8":
    #     await call.message.answer("Специалист по оценке персонала")
    # elif btn_number == "9":
    #     await call.message.answer("Системный архитектор")
    # elif btn_number == "10":
    #     await call.message.answer("DevOps-инженер")
    # elif btn_number == "11":
    #     await call.message.answer("Руководитель проектов")
    # elif btn_number == "12":
    #     await call.message.answer("Pre-Sale менеджер")
    # elif btn_number == "13":
    #     await call.message.answer_venue(
    #         58.00513762428379,
    #         56.200238735786556,
    #         "Адрес и геометка офиса компании:",
    #         "ул. Ленина, 77a"
    #     )
    # elif btn_number == "14":
    #     await call.message.answer_venue(
    #         45.03904199690753,
    #         38.98624678752819,
    #         "Адрес и геометка офиса компании:",
    #         "ул. Северная, 327"
    #     )
    # elif btn_number == "15":
    #     await call.message.answer_venue(
    #         55.713153978710565,
    #         37.62025208405767,
    #         "Адрес и геометка офиса компании:",
    #         "ул. Мытная, 66"
    #     )
    # elif btn_number == "16":
    #     await call.message.answer(
    #         "Извините, но офисы нашей компании находятся только в указанных выше городах"
    #     )



@dp.message_handler()
async def incorrect_message(message: types.Message):
    loop = asyncio.get_event_loop()
    if message.text == "офис":
        city_selection_map = await loop.run_in_executor(None, CreateButtonsCity, True)
        await message.answer(
            "В каком городе ты находишься?",
            reply_markup=city_selection_map
        )
    elif message.text == "вакансии":
        city_selection_work = await loop.run_in_executor(None, CreateButtonsCity, False)
        await message.answer(
            "Вакансии в каком городе тебя интересуют?",
            reply_markup=city_selection_work
        )
    elif message.text == "компания":
        await message.answer(
            "Группа компаний <b>PARMA Technologies Group</b> основана в 2016 году. "
            "Главным направлением деятельности является разработка заказного программного обеспечения.\n\n "
            "У нас собрана профессиональная команда, чей опыт работы на рынке информационных технологий составляет"
            "более 12 лет. Решениями, разработанными нашими специалистами, пользуются многие федеральные,"
            "региональные и муниципальные органы государственной власти.\n\n "
            'Подробности по <a href="https://www.parma.ru/">ссылке</a>',
            disable_web_page_preview=True
        )
    else:
        await message.reply("Лучше воспользуйся ключевыми словами")
        await message.answer("Список ключевых слов:\n"
                             "офис\n"
                             "вакансии\n"
                             "компания")

from aiogram import types

def start_bot():
    executor.start_polling(dp, skip_updates=True)
