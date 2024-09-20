from abc import ABC

import pytest

from config import DATA
from src.ApiHH import ApiHH
from src.AbstractHh import AbstractHh


def test_issubclass():
    assert issubclass(AbstractHh, ABC)
    assert issubclass(ApiHH, AbstractHh)


def test_get_vacancy_from_api():
    vacancy1 = ApiHH('tttttt')
    vacancy2 = ApiHH(1)
    vacancy3 = ApiHH('python')

    vacancy1.get_vacancy_from_api()
    vacancy2.get_vacancy_from_api()
    vacancy3.get_vacancy_from_api()

    assert vacancy1.message == "Vacancies found"
    assert vacancy2.message == "Vacancy not found"
    assert vacancy3.message == "Vacancies found"


def test_save_info_valid():
    vacancy1 = ApiHH('python')

    assert isinstance(vacancy1.all_vacancy, list)
    assert len(vacancy1.all_vacancy) > 0


def test_save_info_zero_len():
    vacancy1 = ApiHH(1)

    assert vacancy1.save_info() == "Vacancy not found"