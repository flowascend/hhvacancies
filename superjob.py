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
        for vacancy in vacancies["items"]:
            salary = predict_rub_salary(currency=vacancy["currency"], salary_from=vacancy["salary_from"], salary_to=vacancy["salary_to"])
            if (vacancy["currency"]) and (vacancy["from"]) and (vacancy["to"]):
                salary = predict_rub_salary(currency=vacancy["currency"], salary_from=vacancy["from"], salary_to=vacancy["to"])
                salaries.append(salary)
        if salaries:
            avg_salary = int(sum(salaries) / len(salaries))
        else:
            avg_salary = None
        languages_salaries[language] = {
            "found_vacancies": vacancies["found"],
            "processed_vacancies": len(salaries),
            "average_salary": avg_salary,
        }
    return languages_salaries
