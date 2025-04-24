import logging
from typing import Literal

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.FileHandler("app.log"),  # Save logs to a file
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)


def set_log_level(level_name: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']):
    '''
    Set the logging level for the logger.

    Parameters:
    - level_name (str): The log level name.
    '''
    level = getattr(logging, level_name.upper(), None)
    if not isinstance(level, int):
        raise ValueError(f'Invalid log level: {level_name}')
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)