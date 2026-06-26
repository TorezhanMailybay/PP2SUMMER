import re

text = "My phone number is 87071234567"

# 1. search() - ищет первое совпадение
result = re.search(r"\d+", text)
print("search():", result.group())

# 2. findall() - возвращает все совпадения
text2 = "10 20 30 40"
print("findall():", re.findall(r"\d+", text2))

# 3. split() - разделяет строку
text3 = "apple,banana;orange grape"
print("split():", re.split(r"[,\s;]+", text3))

# 4. sub() - заменяет совпадения
text4 = "Price: 1500 tenge"
print("sub():", re.sub(r"\d+", "***", text4))

# 5. match() - проверяет начало строки
text5 = "Python is awesome"
result = re.match(r"Python", text5)
if result:
    print("match():", result.group())
else:
    print("No match")

text = "abc123 XYZ"

print(re.findall(r".", text))          # любой символ
print(re.findall(r"\d", text))         # цифры
print(re.findall(r"\w", text))         # буквы + цифры + _
print(re.findall(r"\s", text))         # пробелы
print(re.findall(r"[A-Z]", text))      # заглавные буквы
print(re.findall(r"[a-z]", text))      # строчные буквы
print(re.findall(r"\d{3}", text))      # ровно 3 цифры
print(re.findall(r"\w+", text))        # одно или более символов