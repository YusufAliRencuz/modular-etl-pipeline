from pathlib import Path

BASE_DIR= Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

LOG_FILE_PATH = DATA_DIR / "scraper.log"
OUTPUT_FILE_PATH = DATA_DIR / "articles.json"

BASE_URL = "https://www.mahfiegilmez.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36 OPR/134.0.0.0"
    )
}

REQUEST_TIMEOUT = 10
REQUEST_DELAY_MIN = 0.8
REQUEST_DELAY_MAX = 1.5

SELECTORS = {
    "title": "h3.post-title",
    "date": "time.published",
    "url": "h3.post-title a",
    "content": "div.post-body"
}