from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Keyboards:
    builder = None

    @classmethod
    async def view_catalog(
            cls,
            message: types.Message,

    ):
        builder = InlineKeyboardBuilder()
        buttons = [
            types.InlineKeyboardButton(text='👟 Кросcовки', callback_data='Sneaker'),
            types.InlineKeyboardButton(text='👕 Одежда', callback_data='Cloth'),
            types.InlineKeyboardButton(text='⬅  Назад', callback_data='back')

        ]
        builder.add(*buttons)
        builder.adjust(2, 1)
        await message.edit_text('Выберите категорию!', reply_markup=builder.as_markup())
        return builder