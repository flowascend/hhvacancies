import logging
from commons import predict_rub_salary
from time import time as tick
from itertools import count

logger = logging.getLogger(__name__)


def get_stats(different_languages_vacancies) -> dict:
    print(different_languages_vacancies)
    languages_salaries = {}
    for language, response in different_languages_vacancies.items():
        logger.info(f"Parsing vacancies for {language}.")
        total = response[0]
        vacancies = response[1]
        salaries = []
        for vacancy in vacancies:
            if vacancy["salary"]:
                salary_data = vacancy["salary"]
            else:
                continue
            if salary_data["currency"] and (salary_data["from"] or salary_data["to"]):
                salary = predict_rub_salary(
                    currency=salary_data["currency"],
                    salary_from=salary_data["from"],
                    salary_to=salary_data["to"],
                )
                salaries.append(salary)
        if salaries:
            avg_salary = int(sum(salaries) / len(salaries))
        else:
            avg_salary = None
        languages_salaries[language] = {
            "found_vacancies": total,
            "processed_vacancies": len(salaries),
            "average_salary": avg_salary,
        }
    return languages_salaries
