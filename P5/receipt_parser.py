import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Все цены
prices = re.findall(r"\d[\d ]*,\d{2}", text)

# Названия товаров
products = re.findall(r"\d+\.\n(.+)", text)

# Итоговая сумма
total = re.search(r"ИТОГО:\n([\d ]*,\d{2})", text)

# Дата и время
datetime = re.search(r"Время:\s*([\d\.]+\s+\d+:\d+:\d+)", text)

# Способ оплаты
payment = re.search(r"(Банковская карта|Наличные)", text)

print("Products:")
for product in products:
    print("-", product)

print("\nPrices:")
for price in prices:
    print(price)

if total:
    print("\nTotal:", total.group(1))

if datetime:
    print("Date & Time:", datetime.group(1))

if payment:
    print("Payment:", payment.group(1))