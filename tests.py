import unittest
import json
from datetime import datetime

# Функция для вывода последних транзакций из файла
def print_recent_transactions(file_path):
    with open(file_path, 'r') as file:
        transactions = json.load(file)  # Читаем транзакции из JSON-файла
    for transaction in transactions:
        date_str = datetime.fromisoformat(transaction['date']).strftime('%d.%m.%Y')  # Форматируем дату
        amount = transaction['amount']  # Получаем сумму транзакции
        print(f"Дата: {date_str}, Сумма: {amount}")  # Выводим данные на экран

class TestPrintAllTransactions(unittest.TestCase):

    def read_mock_data(self):
        """Читает данные транзакций из файла operations.json."""
        with open('operations.json', 'r') as f:
            return json.load(f)  # Возвращаем загруженные данные

    def test_print_all_transactions(self):
        """Тестирует вывод всех транзакций из файла."""
        mock_data = self.read_mock_data()  # Загружаем данные из файла

        print_recent_transactions('operations.json')  # Вызываем функцию для вывода транзакций

        # Дополнительно, можно проверить формат вывода, если это нужно
        expected_output = ""
        for transaction in mock_data:
            date_str = datetime.fromisoformat(transaction['date']).strftime('%d.%m.%Y')
            amount = transaction['amount']
            expected_output += f"Дата: {date_str}, Сумма: {amount}\n"

        # В этом тесте мы просто выводим данные, а не проверяем их
        print(expected_output)

    def test_print_all_transactions_empty_file(self):
        """Тестирует поведение функции при пустом файле transactions.json."""
        with open('operations.json', 'w') as f:
            f.write('[]')  # Создаем пустой файл

        print_recent_transactions('operations.json')  # Вызываем функцию с пустым файлом

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты