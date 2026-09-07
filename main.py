from src.network import fetch_html
from src.parser import main_parser, single_parser
from src.storage import save
from src.config import BASE_URL, REQUEST_DELAY_MAX, REQUEST_DELAY_MIN
from src.logger import logger

import random
import time

def main():
    try:
        logger.debug("ETL process is starting.")
        home_html = fetch_html(BASE_URL)
        if not home_html:
            logger.critical("Base url is not accessible. Process has been STOPPED!")
            return

        article_links = main_parser(home_html)
        if not article_links:
            logger.warning("main_parser could not find any article urls!")
            return

        article_infos = []

        for i in article_links:
            article_html = fetch_html(i)
            if article_html:
                article_dict = single_parser(article_html)
                if article_dict:
                    article_infos.append(article_dict)
            delay = random.uniform(REQUEST_DELAY_MIN, REQUEST_DELAY_MAX)
            logger.debug(f"Waiting {delay:.2f}s for server health.")
            time.sleep(delay)

        if article_infos:
            save(article_infos)
            logger.info(f"{len(article_infos)} articles saved.")
        else:
            logger.warning("No article info was retrieved.")
    except Exception as e:
        logger.critical(f"Unexpected error occurred in main loop: {e}")

if __name__ == "__main__":
    main()