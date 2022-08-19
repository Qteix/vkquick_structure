from src.misc import dp
import vkquick as vq

@dp.command('Ping')
async def ping_pong(ctx: vq.NewMessage):
    await ctx.answer('Pong!')

"""
Простая пинг понг команда
"""