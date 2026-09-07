import json

from src.config import OUTPUT_FILE_PATH
from src.logger import logger

def save(data: list):
    try:
        logger.debug("Data will be written to file")
        with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logger.info("Data is saved successfully ")
    except Exception as e:
        logger.error(f"Unexpected error occurred while saving data: {e}")