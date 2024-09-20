from abc import ABC

from src.AbstractJsonSaver import AbstractJsonSaver
from src.JsonSaver import JsonSaver


def test_json_saver_issubclass():
    assert issubclass(JsonSaver, AbstractJsonSaver)
    assert issubclass(AbstractJsonSaver, ABC)


def test_save_file_read_file(fixture_class_json_saver):
    fixture_class_json_saver.save_file([{'name': 'Kris'}])

    assert isinstance(fixture_class_json_saver.read_file(), list)
    assert fixture_class_json_saver.read_file() == [{'name': 'Kris'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Kris'}])

    assert fixture_class_list.read_file() == [{'name': 'Not Kris'}, {'name': 'Kris'}]

    fixture_class_list.delete_vacancy('Kris')
    assert fixture_class_list.read_file() == [{'name': 'Not Kris'}]