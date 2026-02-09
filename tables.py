import terminaltables
import logging

logger = logging.getLogger(__name__)


def format_stats(stats: dict[dict]):
    formatted_stats = [
        ("Language", "Found Vacancies", "Processed Vacancies", "Average Salary")
    ]
    for key, value in stats.items():
        formatted_stats.append((
            key,
            value["found_vacancies"],
            value["processed_vacancies"],
            value["average_salary"],
        ))
    return tuple(formatted_stats)


def get_table(title, table_data):
    logger.info("Creating table...")
    table_instance = terminaltables.AsciiTable(table_data=table_data, title=title)
    logger.info("Created table successfuly.")
    return table_instance
