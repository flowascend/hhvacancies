import terminaltables
import logging

logger = logging.getLogger(__name__)


def format_stats(stats: dict[dict]):
    formatted_stats = [
        ("Language", "Found Vacancies", "Processed Vacancies", "Average Salary")
    ]
    for language, stats in stats.items():
        formatted_stats.append((
            language,
            stats["found_vacancies"],
            stats["processed_vacancies"],
            stats["average_salary"],
        ))
    return tuple(formatted_stats)


def get_table(title, table_data):
    logger.info("Creating table...")
    table_instance = terminaltables.AsciiTable(table_data=table_data, title=title)
    logger.info("Created table successfuly.")
    return table_instance
