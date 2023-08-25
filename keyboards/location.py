from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Моя геолокация",
                request_location=True,
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Кнопка внизу"
)
