import logging
from typing import Literal


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
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


def set_log_file(file_path: str, level_name: str = 'INFO'):
    '''
    Adds a file handler to the logger, saving logs to the specified file.

    Parameters:
    - file_path (str): Path to the log file.
    - level_name (str): Logging level for the file handler (default is 'INFO').
    '''
    level = getattr(logging, level_name.upper(), None)
    if not isinstance(level, int):
        raise ValueError(f'Invalid log level: {level_name}')

    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Avoid duplicate handlers if already added
    logger = logging.getLogger(__name__)
    if not any(isinstance(h, logging.FileHandler) and h.baseFilename == file_handler.baseFilename
               for h in logger.handlers):
        logger.addHandler(file_handler)