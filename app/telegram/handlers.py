from aiogram import Router

from aiogram import Bot, F, types
from aiogram.filters.command import Command
from aiogram.types import WebAppInfo

from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.service.db_service import add_users


router = Router()
bot = Bot(token='7217637541:AAFmcDDbJiNDXYieR9jyV1OYVvaYBCWyXFM')


@router.message(Command("start"))
async def command_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    user = await add_users(
        name=message.from_user.username,
        telegram_id=message.from_user.id
    )
    if user is True:
        print('Новая регистрация')

    elif user is False:
        print('Зашел зарегистрированный пользователь!')
    buttons = [
        types.InlineKeyboardButton(
            text='📅 Записаться на консультацию',
            web_app=WebAppInfo(url='https://dae4-46-166-208-81.ngrok-free.app')
        ),
        types.InlineKeyboardButton(text='ℹ️ Информация', callback_data='Information'),

    ]
    builder.add(*buttons)
    builder.adjust(1)
    await message.answer(
        "Приветствую! Я ваш виртуальный помощник в мире кухонь. Чем могу помочь вам сегодня?\n\n"
        "📅 Записаться на консультацию: Хотите получить персональную консультацию?"
        "Просто заполните форму, и мы свяжемся с вами.\n\n"
        "ℹ️ Информация: Узнайте больше о наших услугах, материалах и специальных предложениях.\n\n"
        "Начните свой путь к кухне мечты с нами!",

        reply_markup=builder.as_markup(resize_keyboard=True)
    )


async def send_msg(
        name: str,
        phone: str
):
    await bot.send_message(
        text=f'{name}\n{phone}',
        chat_id='847449845'
    )