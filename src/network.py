import requests
from src.config import HEADERS, REQUEST_TIMEOUT
from src.logger import logger

def fetch_html(url: str):
    try:
        logger.debug(f"Request will be sent: {url}")
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        logger.info(f"Success at fetching html: {url}")
        return response.text
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error! Html couldn't be accessed: {url}, Exception: {e}")
        return None