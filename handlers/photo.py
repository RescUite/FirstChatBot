from aiogram import Router, types, F

router = Router()


@router.message(F.photo)
async def answer_photo(message: types.Message):
    await message.answer(f"Хорошее фото! Сохраню на память!")
