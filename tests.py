import unittest
import json
from datetime import datetime
from io import StringIO
import sys

from coursework import print_all_transactions

class TestPrintAllTransactions(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.test_data = [
            {
                "id": "b79c5d2d-3c56-4b7e-b5e0-d7d9c5d2d3c5",
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779"
            },
            {
                "id": "a6c5d2d-3c56-4b7e-b5e0-d7d9c5d2d3c5",
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895"
            },
            {
                "id": "c79c5d2d-3c56-4b7e-b5e0-d7d9c5d2d3c5",
                "state": "CANCELED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "4500",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895"
            }
        ]

    def test_print_all_transactions(self):
        # Сохраняем стандартный вывод
        stdout = sys.stdout
        # Создаем StringIO для перехвата вывода
        sys.stdout = StringIO()

        print_all_transactions('operations.json')

        # Получаем вывод из StringIO
        output = sys.stdout.getvalue()

        # Восстанавливаем стандартный вывод
        sys.stdout = stdout

        # Ожидаемый вывод
        expected_output = """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> **5779
31 957,58 руб.

03.07.2019 Перевод организации
MasterCard 7158 30** **** 6758 -> **7895
8 221,37 USD

"""

        self.assertEqual(output, expected_output)

    def test_print_all_transactions_empty_file(self):
        # Сохраняем стандартный вывод
        stdout = sys.stdout
        # Создаем StringIO для перехвата вывода
        sys.stdout = StringIO()

        print_all_transactions('operations.json')

        # Получаем вывод из StringIO
        output = sys.stdout.getvalue()

        # Восстанавливаем стандартный вывод
        sys.stdout = stdout

        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()