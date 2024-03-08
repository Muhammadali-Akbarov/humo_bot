"""
inline button creator
"""
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def genmarkup(keyboard_data: dict):
    """
    inline button creator

    use case:
        keyboard_data = [
            ("Button 1", "button1_callback"),
            ("Button 2", "button2_callback"),
            ("Button 3", "button3_callback"),
        ]
        markup = inline.genmarkup(keyboard_data=keyboard_data)
    """
    builder = InlineKeyboardBuilder()
    for i in keyboard_data:
        button = InlineKeyboardButton(
            text=i[0],
            callback_data=i[1]
        )
        builder.add(button)

    return builder.as_markup()
