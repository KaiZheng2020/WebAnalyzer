import json
import os
import sys
import time

from loguru import logger

__version__ = "0.0.3"

if getattr(sys, 'frozen', False):
    CONFIG_PATH = os.path.dirname(sys.executable)
else:
    CONFIG_PATH = os.path.dirname(__file__)


def init_log():

    log_path = g_config['log']['path']

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    LOG_FILE = os.path.join(log_path, time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log')

    logger.add(LOG_FILE,
               format="{time:YYYY-MM-DD HH:mm:ss} {level} {function} {thread}: {message}",
               level='DEBUG',
               encoding='utf-8',
               rotation="1 day",
               retention='30 days')


def config_load(config_file) -> dict:
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        logger.info(f'cannot load config file: {config_file}')


def init_config() -> dict:
    config_file = os.path.join(CONFIG_PATH, 'config.json')
    return config_load(config_file)


g_config = init_config()

init_log()
