from src.CompareVacancies import CompareVacancies
from src.ApiHH import ApiHH


def test_compare_vacancies_is_subclass_get_vacancies():
    assert issubclass(CompareVacancies, ApiHH)


def test_sorted_salary(fixture_class_valid, fixture_data):
    data_test = fixture_data
    vacancy = fixture_class_valid

    vacancy.sorted_salary(data_test, 50000, "Москва")
    assert vacancy.sort_salary == {50000: [{'area': {'name': 'Москва'}, 'salary': {'from': 50000, 'to': 80000}}]}


def test_get_top_vacancies_valid(fixture_class_valid, fixture_data):
    vacancy = fixture_class_valid

    vacancy.get_top_vacancies({50000: [{'area': {'name': 'Москва'}, 'salary': {'from': 50000, 'to': 80000}}]}, )

    assert vacancy.top_salary == {80000: [{'area': {'name': 'Москва'}, 'salary': {'from': 50000, 'to': 80000}}]}