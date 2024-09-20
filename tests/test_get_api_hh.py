from abc import ABC

from src.AbstractGetApiHh import AbstractGetApiHh
from src.GetApiHh import GetApiHh


def test_issubclass():
    assert issubclass(GetApiHh, ABC)
    assert issubclass(GetApiHh, AbstractGetApiHh)


def test_get_vacancy_from_api(fixture_class_get_hh_valid, fixture_class_get_hh_negative):
    assert len(fixture_class_get_hh_valid) > 0
    assert fixture_class_get_hh_negative == "Vacancy not found"


def test_all_vacancy():
    get_api = GetApiHh()
    get_api.get_vacancy_from_api('python')

    assert len(get_api.all_vacancy) > 0