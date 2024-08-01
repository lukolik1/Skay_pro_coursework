<<<<<<< HEAD
import json
from datetime import datetime

def format_card_number(card_number):
    if len(card_number) >= 16:
        if card_number.startswith('4'):
            card_type = 'Visa'
        elif card_number.startswith('5'):
            card_type = 'MasterCard'
        else:
            card_type = card_number[:card_number.find(' ')]
        
        space_index = card_number.find(' ')
        last_space_index = card_number.rfind(' ')
        
        card_number_masked = card_type + " " + card_number[space_index + 1:space_index + 4] + card_number[space_index + 5:space_index + 8] + " " + card_number[last_space_index + 0:last_space_index + 3] + card_number[last_space_index + 5:last_space_index + 7] + " " + card_number[last_space_index + 5:last_space_index + 7] + "** **** " + card_number[13:17] 
        return card_number_masked
    else:
        return card_number

def format_account_number(account_number):
    """
    Форматирует номер счета в формате "Счет **XXXX".

    Args:
        account_number (str): Номер счета.SS

    Returns:
        str: Отформатированный номер счета.
    """
    if len(account_number) >= 4:
        return f"Счет **{account_number[-4:]}"
    else:
        return account_number

def print_recent_transactions(file_path, num_transactions=5):
    """
    Выводит на экран список последних выполненных клиентом операций.

    Args:
        file_path (str): Путь к файлу с данными операций.
        num_transactions (int): Количество последних операций для вывода (по умолчанию 5).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Определяем, где хранятся данные об операциях
    if 'operations' in data:
        transactions = data['operations']
    else:
        transactions = data

    # Фильтруем только выполненные операции
    executed_transactions = [t for t in transactions if t.get('state', '') == 'EXECUTED']

    # Сортируем операции по дате в обратном порядке
    executed_transactions.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    # Выводим последние num_transactions операции
    for transaction in executed_transactions[:num_transactions]:
        # Форматируем дату
        date_str = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        # Форматируем номер карты
        from_card = transaction.get('from', '')
        if from_card:
            from_card = format_card_number(from_card)

        # Форматируем номер счета отправителя
        from_account = transaction.get('from', '')
        if from_account:
            from_account = format_account_number(from_account)

        # Форматируем номер счета получателя
        to_account = transaction.get('to')
        to_account = format_account_number(to_account)

        # Форматируем валюту
        currency = transaction['operationAmount']['currency']['name']
        amount = float(transaction['operationAmount']['amount'])

        # Определяем формат отображения валюты
        if currency == 'RUB':
            currency_name = 'руб.'
        elif currency == 'USD':
            currency_name = 'USD'
        else:
            currency_name = currency

        # Выводим информацию об операции
        print(f"{date_str} {transaction.get('description', '')}")
        if from_account:
            print(f"{from_account} -> {to_account}")
        else:
            print(f"{to_account}")
        print(f"{from_card}")
        print(f"{amount:,.2f} {currency_name}")
        print()

# Пример использования
=======
import json
from datetime import datetime

def format_card_number(card_number):
    if len(card_number) >= 16:
        if card_number.startswith('4'):
            card_type = 'Visa'
        elif card_number.startswith('5'):
            card_type = 'MasterCard'
        else:
            card_type = card_number[:card_number.find(' ')]
        
        space_index = card_number.find(' ')
        last_space_index = card_number.rfind(' ')
        
        card_number_masked = card_type + " " + card_number[space_index + 1:space_index + 4] + card_number[space_index + 5:space_index + 8] + " " + card_number[last_space_index + 0:last_space_index + 3] + card_number[last_space_index + 5:last_space_index + 7] + " " + card_number[last_space_index + 5:last_space_index + 7] + "** **** " + card_number[13:17] 
        return card_number_masked
    else:
        return card_number

def format_account_number(account_number):
    """
    Форматирует номер счета в формате "Счет **XXXX".

    Args:
        account_number (str): Номер счета.SS

    Returns:
        str: Отформатированный номер счета.
    """
    if len(account_number) >= 4:
        return f"Счет **{account_number[-4:]}"
    else:
        return account_number

def print_recent_transactions(file_path, num_transactions=5):
    """
    Выводит на экран список последних выполненных клиентом операций.

    Args:
        file_path (str): Путь к файлу с данными операций.
        num_transactions (int): Количество последних операций для вывода (по умолчанию 5).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Определяем, где хранятся данные об операциях
    if 'operations' in data:
        transactions = data['operations']
    else:
        transactions = data

    # Фильтруем только выполненные операции
    executed_transactions = [t for t in transactions if t.get('state', '') == 'EXECUTED']

    # Сортируем операции по дате в обратном порядке
    executed_transactions.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    # Выводим последние num_transactions операции
    for transaction in executed_transactions[:num_transactions]:
        # Форматируем дату
        date_str = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        # Форматируем номер карты
        from_card = transaction.get('from', '')
        if from_card:
            from_card = format_card_number(from_card)

        # Форматируем номер счета отправителя
        from_account = transaction.get('from', '')
        if from_account:
            from_account = format_account_number(from_account)

        # Форматируем номер счета получателя
        to_account = transaction.get('to')
        to_account = format_account_number(to_account)

        # Форматируем валюту
        currency = transaction['operationAmount']['currency']['name']
        amount = float(transaction['operationAmount']['amount'])

        # Определяем формат отображения валюты
        if currency == 'RUB':
            currency_name = 'руб.'
        elif currency == 'USD':
            currency_name = 'USD'
        else:
            currency_name = currency

        # Выводим информацию об операции
        print(f"{date_str} {transaction.get('description', '')}")
        if from_account:
            print(f"{from_account} -> {to_account}")
        else:
            print(f"{to_account}")
        print(f"{from_card}")
        print(f"{amount:,.2f} {currency_name}")
        print()

# Пример использования
>>>>>>> 9e68d5e36a30674f6ad19ef26c7441abd11d27d9
print_recent_transactions('operations.json')