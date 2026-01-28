import headhunter
import superjob
import tables
import logging
from dotenv import load_dotenv
from os import getenv
from hhapi import get_different_languages_vacancies as get_hh_vacancies
from sjapi import get_different_languages_vacancies as get_sj_vacancies
from time import time as tick

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=20)
    load_dotenv()
    start_tick = tick()
    superjob_key_presence = False
    if getenv("SUPERJOB_SECRET_KEY"):
        superjob_key_presence = True
    else:
        logger.warning(
            "SuperJob secret key not present! Skipping all SuperJob related calls."
        )
    logger.info("Getting salaries... [1/2 - HeadHunter]")
    headhunter_salaries = headhunter.get_stats(get_hh_vacancies())
    if superjob_key_presence:
        logger.info("Getting salaries... [2/2 - SuperJob]")
        superjob_salaries = superjob.get_stats(get_sj_vacancies())
    logger.info("Making tables...")
    headhunter_table_instance = tables.get_table(
        "HeadHunter", tables.format_data(headhunter_salaries)
    )
    if superjob_key_presence:
        superjob_table_instance = tables.get_table(
            "SuperJob", tables.format_data(superjob_salaries)
        )
    logger.info(f"Done! {round((tick() - start_tick), 2)}s.")
    print(headhunter_table_instance.table)
    print(superjob_table_instance.table)


if __name__ == "__main__":
    main()
