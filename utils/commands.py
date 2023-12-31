from aiogram import Bot, types


async def set_up_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(
                command="/start",
                description="Начать взаимодействие с ботом",
            ),
            types.BotCommand(
                command="/cat",
                description="Получить котика",
            ),
            types.BotCommand(
                command="/weather",
                description="Узнать погоду",
            )
        ]
    )
