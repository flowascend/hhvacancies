import logging
import requests
from os import getenv
from dotenv import load_dotenv
from time import time as tick
from time import sleep as wait
from itertools import count
from pprint import pprint

logger = logging.getLogger(__name__)


def get_vacancies(
    token: str,
    keyword: str,
    area_id: int = 4,
    catalog: int = 48,
    period: int = 30,
    wait_time: float = 3.0,
):
    total_start_tick = tick()
    all_pages = [0, []]
    for page in count(0):
        logger.log(
            15,
            f"[get_vacancies_items] Waiting for {wait_time} seconds to avoid DoS detection...",
        )
        wait(wait_time)
        start_tick = tick()
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {
            "keyword": keyword,
            "catalogues": catalog,
            "town": area_id,
            "period": period,
        }
        headers = {"X-Api-App-Id": token}
        logger.log(15, f"[get_vacancies_items] Sending request to {url}")
        page_response = requests.get(url=url, params=params, headers=headers)
        page_response.raise_for_status()
        page_payload = page_response.json()

        all_pages[0] = page_payload["total"]
        all_pages[1].append(page_payload["objects"])

        if page >= int(page_payload["total"] / 20) - 1:
            logger.log(
                15,
                f"[get_vacancies_items] Last page parsed! Breaking. Time taken: {round((tick() - start_tick), 2)}s.",
            )
            logger.log(
                16,
                f"[get_vacancies_items] Total time: {round((tick() - total_start_tick), 2)}. Total pages: {page}.",
            )
            break
        logger.log(
            15,
            f"[get_vacancies_items] Got page {page} payload. Time taken: {round((tick() - start_tick), 2)}s.",
        )
    return tuple(all_pages)


def get_different_languages_vacancies(
    token: str, period: int = 30, area_id: str = "1", catalog: int = 48
) -> dict:
    top_languages = ["JavaScript", "Java", "Python", "C++", "Ruby", "C#", "PHP", "C"]
    different_languages_vacancies = {}
    for language in top_languages:
        logger.info(f"Parsing vacancies for {language}.")
        language_vacancies = get_vacancies(
            token=token, keyword=language, period=period, area_id=area_id, catalog=48
        )
        different_languages_vacancies[language] = language_vacancies
    return different_languages_vacancies
