import logging
from os import getenv

BACKEND = "Telegram" if getenv("ENVIRONMENT") == "production" else "Text"

BOT_DATA_DIR = r'/home/beantorong/PycharmProjects/slurm_python_for_ops/data'
BOT_EXTRA_PLUGIN_DIR = r'/home/beantorong/PycharmProjects/slurm_python_for_ops/plugins'

BOT_LOG_FILE = r'/home/beantorong/PycharmProjects/slurm_python_for_ops/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_PREFIX = "/" if getenv("ENVIRONMENT") == "production" else "!"
BOT_ALT_PREFIXES = ('Пес', 'Bot', 'Err')
BOT_ALT_PREFIXES_SEPARATORS = (':', ',', ':')


BOT_ADMINS = ('@CHANGE_ME', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!
