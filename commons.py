import logging

logger = logging.getLogger(__name__)


def predict_rub_salary(
    currency: str = None, salary_from: int = None, salary_to: int = None
) -> int:
    average = None
    if not currency or not (salary_from or salary_to):
        return
    if not currency == "RUR" or not currency == "RUB":
        return

    if salary_from and salary_to:
        average = int((salary_from + salary_to) / 2)
    elif salary_from and not salary_to:
        average = int(salary_from * 1.2)
    elif salary_to and not salary_from:
        average = int(salary_to * 0.8)
    return average
