import terminaltables
import logging

logger = logging.getLogger(__name__)


def format_data(salaries):
    return (
        ("Language", "Found Vacancies", "Processed Vacancies", "Average Salary"),
        (
            "C",
            salaries["C"]["found_vacancies"],
            salaries["C"]["processed_vacancies"],
            salaries["C"]["average_salary"],
        ),
        (
            "C#",
            salaries["C#"]["found_vacancies"],
            salaries["C#"]["processed_vacancies"],
            salaries["C#"]["average_salary"],
        ),
        (
            "C++",
            salaries["C++"]["found_vacancies"],
            salaries["C++"]["processed_vacancies"],
            salaries["C++"]["average_salary"],
        ),
        (
            "Java",
            salaries["Java"]["found_vacancies"],
            salaries["Java"]["processed_vacancies"],
            salaries["Java"]["average_salary"],
        ),
        (
            "JavaScript",
            salaries["JavaScript"]["found_vacancies"],
            salaries["JavaScript"]["processed_vacancies"],
            salaries["JavaScript"]["average_salary"],
        ),
        (
            "PHP",
            salaries["PHP"]["found_vacancies"],
            salaries["PHP"]["processed_vacancies"],
            salaries["PHP"]["average_salary"],
        ),
        (
            "Python",
            salaries["Python"]["found_vacancies"],
            salaries["Python"]["processed_vacancies"],
            salaries["Python"]["average_salary"],
        ),
        (
            "Ruby",
            salaries["Ruby"]["found_vacancies"],
            salaries["Ruby"]["processed_vacancies"],
            salaries["Ruby"]["average_salary"],
        ),
    )


def get_table(title, table_data):
    logger.info("Creating table...")
    table_instance = terminaltables.AsciiTable(table_data=table_data, title=title)
    logger.info("Created table successfuly.")
    return table_instance
