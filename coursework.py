import datetime
import json


def format_card_number(card):
    card = card.split()
    card_numbers = card[-1]
    card_type = card[:-1]
    masked_card_num = f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"
    return f"{' '.join(card_type)} {masked_card_num}"


def format_account_number(account_number):
    return f"Счет **{account_number[-4:]}" if len(account_number) >= 4 else account_number


def mask_account_or_card(transaction):
    from_account = ""
    if transaction.get("from"):
        if transaction['from'].startswith('Счет'):
            from_account = format_account_number(transaction['from'])
        else:
            from_account = format_card_number(transaction['from'])
    return from_account


def print_recent_transactions(file_path, num_transactions=5):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    transactions = data if isinstance(data, list) else data.get('operations', [])
    executed_transactions = [t for t in transactions if t.get('state') == 'EXECUTED']
    executed_transactions.sort(key=lambda x: x['date'], reverse=True)

    for transaction in executed_transactions[:num_transactions]:
        date_str = datetime.fromisoformat(transaction['date']).strftime('%d.%m.%Y')

        to_account = format_account_number(transaction['to'])
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['name']
        from_account = mask_account_or_card(transaction)
        # Форматируем вывод в три строки
        print(f"{date_str} {transaction.get('description', '')}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount:,.2f} {currency}\n")