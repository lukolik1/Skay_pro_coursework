import unittest
import json
from datetime import datetime # вот ваш импорт он и был таким  =)
from unittest.mock import patch, mock_open, call
from coursework import format_card_number, format_account_number, mask_account_or_card, print_recent_transactions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        """Создание тестовых данных перед каждым тестом."""
        self.mock_data = [
            {"date": "2023-09-15T10:00:00", "amount": 100.50},
            {"date": "2023-09-16T11:30:00", "amount": 200.75}
        ]
        self.mock_transactions = [
            {
                "date": datetime(2023, 9, 15, 10, 0).isoformat(),
                "description": "Payment",
                "from": "Счет 1234567890123456",
                "to": "Счет 6543210987654321",
                "operationAmount": {"amount": 100.50, "currency": {"name": "RUB"}},
                "state": "EXECUTED"
            },
            {
                "date": datetime(2023, 9, 16, 11, 30).isoformat(),
                "description": "Transfer",
                "from": "Maestro 1308795367077170",
                "to": "Счет 9876543210123456",
                "operationAmount": {"amount": 200.75, "currency": {"name": "USD"}},
                "state": "EXECUTED"
            },
            {
                "date": datetime(2023, 9, 17, 12, 0).isoformat(),
                "description": "Failed Transaction",
                "from": None,
                "to": None,
                "operationAmount": {"amount": 300.00, "currency": {"name": "EUR"}},
                "state": "CANCELED"
            }
        ]

    def test_format_card_number(self):
        """Тестирует форматирование номера карты."""
        result = format_card_number('Maestro 1308795367077170')
        self.assertEqual(result, 'Maestro 1308 79** **** 7170')

    def test_format_account_number(self):
        """Тестирует форматирование номера счета."""
        self.assertEqual(format_account_number('1234567890123456'), 'Счет **3456')
        self.assertEqual(format_account_number('123'), '123')  # Короткий номер

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps([]))
    @patch('builtins.print')
    def test_print_all_transactions_empty_file(self, mock_print, mock_open):
        """Тестирует поведение функции при пустом файле."""
        print_recent_transactions('operations.json')
        mock_print.assert_not_called()  # Не должно быть вызовов print

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_print_all_transactions(self, mock_print, mock_open):
        """Тестирует вывод всех транзакций из файла."""
        mock_open.return_value.read.return_value = json.dumps(self.mock_transactions)
        print_recent_transactions('operations.json')

        expected_calls = [
            call("15.09.2023 Payment"),
            call("Счет **3456 -> Счет **4321"),
            call("100.50 RUB\n"),
            call("16.09.2023 Transfer"),
            call("Maestro 1308 79** **** 7170 -> Счет **3456"),
            call("200.75 USD\n")
        ]
        
        # Проверяем, что print был вызван с ожидаемыми значениями
        mock_print.assert_has_calls(expected_calls, any_order=True)

    def test_mask_account_or_card(self):
        """Тестирует маскировку счета или карты."""
        transaction_card = {"from": "Maestro 1308795367077170"}
        transaction_account = {"from": "Счет 1234567890123456"}
        transaction_none = {}

        self.assertEqual(mask_account_or_card(transaction_card), 'Maestro 1308 79** **** 7170')
        self.assertEqual(mask_account_or_card(transaction_account), 'Счет **3456')
        self.assertEqual(mask_account_or_card(transaction_none), '')

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_print_recent_transactions_no_executed(self, mock_print, mock_open):
        """Тестирует поведение при отсутствии выполненных транзакций."""
        mock_open.return_value.read.return_value = json.dumps([
            {
                "date": datetime(2023, 9, 17).isoformat(),
                "state": "CANCELED"
            }
        ])
        
        print_recent_transactions('operations.json')
        
        mock_print.assert_not_called()  # Нет выполненных транзакций для вывода

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_print_recent_transactions_fewer_than_requested(self, mock_print, mock_open):
        """Тестирует поведение при меньшем количестве выполненных транзакций."""
        mock_open.return_value.read.return_value = json.dumps(self.mock_transactions[:1])  # Только одна выполненная
        
        print_recent_transactions('operations.json', num_transactions=5)
        
        expected_calls = [
            call("15.09.2023 Payment"),
            call("Счет **3456 -> Счет **4321"),
            call("100.50 RUB\n")
        ]
        
        # Проверяем все вызовы print
        mock_print.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты