import logging
from commons import predict_rub_salary
from sjapi import get_different_languages_vacancies
from pprint import pprint

logger = logging.getLogger(__name__)


def get_stats(different_languages_vacancies: dict) -> dict:
    languages_salaries = {}
    for language, vacancies in different_languages_vacancies.items():
        logger.info(f"Parsing vacancies for {language}.")
        salaries = []
        for vacancy in vacancies[1]:
            if vacancy["currency"] and (vacancy["from"] or vacancy["to"]):
                salary = predict_rub_salary(
                    currency=vacancy["currency"],
                    salary_from=vacancy["payment_from"],
                    salary_to=vacancy["payment_to"],
                )
                salaries.append(salary)
        if salaries:
            avg_salary = int(sum(salaries) / len(salaries))
        else:
            avg_salary = None
        languages_salaries[language] = {
            "found_vacancies": vacancies[1],
            "processed_vacancies": len(salaries),
            "average_salary": avg_salary,
        }
    return languages_salaries
