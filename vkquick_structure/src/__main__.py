from src.config.token import access_token
from src.misc import dp
from loguru import logger

if len(access_token) != 198:
    logger.opt(colors=True).success(f'<yellow>ОШИБКА В КОНФИГУРАЦИИ ТОКЕНА, ПОЖАЛУЙСТА УБЕДИТЕСЬ ЧТО ВЫ ВВЕЛИ ВЕРНЫЙ ТОКЕН</yellow>')
else:
    try:
        logger.opt(colors=True).success(f'<magenta>{"*"*20}</magenta> <yellow>BOT STARTED</yellow> <magenta>{"*"*20}</magenta>')
        dp.run(access_token)
    except KeyboardInterrupt:
        logger.opt(colors=True).info(f'<red>{"*"*20}</red> <green>KeyboardInterrupt</green> <red>{"*"*20}</red>')
    except:
        logger.opt(colors=True).error(f'<red>{"*"*20}</red> <red>ERROR</red> <red>{"*"*20}</red>')
