from bs4 import BeautifulSoup
from src.config import SELECTORS
from src.logger import logger

def single_parser(html: str):
    try:
        logger.debug("Html string will be parsed")
        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.select_one(SELECTORS["title"]) 
        if not title_tag:
            logger.warning("Title couldn't be found, article will be passed")
            return None
        title = title_tag.get_text(strip=True)

        date_tag = soup.select_one(SELECTORS["date"])
        date = date_tag.get("datetime") if date_tag else "Unknown"

        url_tag = soup.select_one(SELECTORS["url"])
        url = url_tag.get("href") if url_tag else "Unknown"

        content_elements = soup.select(f"{SELECTORS['content']} p")
        content = " ".join([p.get_text(strip=True) for p in content_elements]) if content_elements else ""

        article_dict = {
            "title": title,
            "date": date,
            "url": url,
            "content": content
        }
        logger.info("Html was parsed successfully")
        return article_dict
    except Exception as e:
        logger.error(f"Unexpected error occurred while parse html: {e}")
        return None

def main_parser(html: str):
    try:
        logger.debug("Html string will be parsed")
        soup = BeautifulSoup(html, "html.parser")
        link_list = soup.select(SELECTORS["url"])

        links = []
        for i in link_list:
            if i.get("href"):
                links.append(i.get("href"))
        logger.info(f"{len(links)} urls are taken succesfully")
        return links
    except Exception as e:
        logger.error(f"Unexpected error occurred while parse html: {e}")
        return []