import terminaltables
import logging

logger = logging.getLogger(__name__)


def format_stats(stats: dict[dict]):
    formatted_stats = [
        ("Language", "Found Vacancies", "Processed Vacancies", "Average Salary")
    ]
    for k, v in stats.items():
        formatted_stats.append((
            k,
            v["found_vacancies"],
            v["processed_vacancies"],
            v["average_salary"],
        ))
    return tuple(formatted_stats)


def get_table(title, table_data):
    logger.info("Creating table...")
    table_instance = terminaltables.AsciiTable(table_data=table_data, title=title)
    logger.info("Created table successfuly.")
    return table_instance
