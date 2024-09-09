import json
from datetime import datetime

def format_card_number(card_number):
    if len(card_number) < 16:
        return card_number
    card_type = 'Visa Classic' if card_number.startswith('4') else 'MasterCard' if card_number.startswith('5') else ''
    return f"{card_type} {card_number[0:5]} {card_number[5:12]}** **** {card_number[12:16]}"

def format_account_number(account_number):
    return f"Счет **{account_number[-4:]}" if len(account_number) >= 4 else account_number

def print_recent_transactions(file_path, num_transactions=5):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    transactions = data if isinstance(data, list) else data.get('operations', [])
    executed_transactions = [t for t in transactions if t.get('state') == 'EXECUTED']
    executed_transactions.sort(key=lambda x: x['date'], reverse=True)

    for transaction in executed_transactions[:num_transactions]:
        date_str = datetime.fromisoformat(transaction['date'][:-1]).strftime('%d.%m.%Y')
        from_card = format_card_number(transaction.get('from', ''))
        from_account = format_account_number(transaction.get('from', ''))
        to_account = format_account_number(transaction['to'])
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['name']

        # Форматируем вывод в три строки
        print(f"{date_str} {transaction.get('description', '')}")
        print(f"{from_card} -> {to_account}")
        print(f"{amount:,.2f} {currency}\n")

# Пример использования
print_recent_transactions('operations.json')