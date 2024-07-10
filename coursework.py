import json
from datetime import datetime

def print_all_transactions(file_path):
    """
    Выводит на экран список всех выполненных клиентом операций.

    Args:
        file_path (str): Путь к файлу с данными операций.
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

    # Выводим все операции
    for transaction in executed_transactions:
        # Форматируем дату
        date_str = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        # Форматируем номер карты
        from_card = transaction.get('from', '')
        if from_card:
            from_card = ' '.join([from_card[:4], from_card[4:6] + '** **** ' + from_card[-4:]])

        # Форматируем номер счета
        to_account = transaction.get('to')
        
        if to_account:
    # Проверяем, что номер счета содержит хотя бы 4 цифры
            if len(to_account) >= 4:
                to_account = '**' + to_account[-4:]
            else:
                to_account = to_account

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
        print(f"{from_card} -> {to_account}")
        print(f"{amount:,.2f} {currency_name}")
        print()

# Пример использования
print_all_transactions('operations.json')