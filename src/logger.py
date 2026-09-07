import os
import logging
from src.config import DATA_DIR, LOG_FILE_PATH

os.makedirs(DATA_DIR, exist_ok=True)

logger = logging.getLogger("Scraping_Project")
logger.setLevel(logging.DEBUG)
template = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | [%(filename)-10s] | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

terminal_handler = logging.StreamHandler()
terminal_handler.setLevel(logging.INFO)
terminal_handler.setFormatter(template)

file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(template)

logger.handlers.clear() 
logger.addHandler(terminal_handler)
logger.addHandler(file_handler)