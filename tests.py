import unittest
import json
from datetime import datetime
from unittest.mock import patch, mock_open, call
from coursework import format_card_number  # Импортируйте функции из вашего модуля

# Функция для вывода последних транзакций из файла
def print_recent_transactions(file_path):
    with open(file_path, 'r') as file:
        transactions = json.load(file)
    for transaction in transactions:
        date_str = datetime.fromisoformat(transaction['date']).strftime('%d.%m.%Y')
        amount = transaction['amount']
        print(f"Дата: {date_str}, Сумма: {amount}")

# Тесты
class TestFunctions(unittest.TestCase):

    def setUp(self):
        """Создание тестовых данных перед каждым тестом."""
        self.mock_data = [
            {"date": "2023-09-15T10:00:00", "amount": 100.50},
            {"date": "2023-09-16T11:30:00", "amount": 200.75}
        ]

    def test_format_card_number(self):
        """Тестирует форматирование номера карты."""
        result = format_card_number('Maestro 1308795367077170')
        self.assertEqual(result, 'Maestro 1308 79** **** 7170')

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
        # Устанавливаем данные для mock_open
        mock_open.return_value.read.return_value = json.dumps(self.mock_data)
        print_recent_transactions('operations.json')

        expected_calls = [
            call(f"Дата: {datetime.fromisoformat(tx['date']).strftime('%d.%m.%Y')}, Сумма: {tx['amount']}")
            for tx in self.mock_data
        ]
        
        # Проверяем, что print был вызван с ожидаемыми значениями
        mock_print.assert_has_calls(expected_calls, any_order=True)

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты
