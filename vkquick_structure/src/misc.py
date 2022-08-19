from src.config.prefixes import prefixes
import vkquick as vq

dp = vq.App(
    prefixes=prefixes,
    filter=vq.filters.OnlyMe(),
    name='StructureBot',
    description='Example structure bot',
    site_title='Site Tittle example'
)