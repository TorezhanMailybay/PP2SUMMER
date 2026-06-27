from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students = [
    {"name": "Alice",  "grade": 92, "age": 20},
    {"name": "Bob",    "grade": 55, "age": 22},
    {"name": "Carol",  "grade": 78, "age": 21},
    {"name": "Dave",   "grade": 61, "age": 19},
    {"name": "Eve",    "grade": 88, "age": 23},
    {"name": "Frank",  "grade": 45, "age": 20},
]

print("=== map() ===")
print(list(map(lambda x: x ** 2, numbers)))
print(list(map(lambda x: x * 2, numbers)))
print(list(map(str.upper, ["hello", "world", "python"])))
print(list(map(lambda s: s["grade"], students)))

def celsius_to_fahrenheit(c):
    return round(c * 9/5 + 32, 1)

temps_c = [0, 20, 37, 100]
print(list(zip(temps_c, map(celsius_to_fahrenheit, temps_c))))

a, b = [1, 2, 3], [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))

print("\n=== filter() ===")
print(list(filter(lambda x: x % 2 == 0, numbers)))
print(list(filter(lambda x: x > 5, numbers)))
print([s["name"] for s in filter(lambda s: s["grade"] >= 60, students)])
print([s["name"] for s in filter(lambda s: s["grade"] < 60, students)])

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(is_prime, range(2, 30))))
print(list(filter(None, [0, 1, "", "hello", None, [], [1, 2], False, True])))

print("\n=== reduce() ===")
print(reduce(lambda acc, x: acc + x, numbers))
print(reduce(lambda acc, x: acc * x, numbers))
print(reduce(lambda a, b: a if a > b else b, numbers))
print(reduce(lambda a, b: a + " " + b, ["Python", "is", "awesome"]))
print(reduce(lambda acc, lst: acc + lst, [[1, 2], [3, 4], [5, 6]], []))

print("\n=== Pipeline: map + filter + reduce ===")
result = reduce(
    lambda acc, x: acc + x,
    filter(lambda x: x % 2 == 0,
           map(lambda x: x ** 2, numbers))
)
print(f"Sum of squares of evens (1-10): {result}")

passing_grades = list(map(lambda s: s["grade"], filter(lambda s: s["grade"] >= 60, students)))
avg = reduce(lambda a, b: a + b, passing_grades) / len(passing_grades)
print(f"Avg grade (passing only): {avg:.1f}")

print("\n=== len / sum / min / max ===")
print(f"len={len(numbers)}, sum={sum(numbers)}, min={min(numbers)}, max={max(numbers)}")
print(f"sum with start: {sum(numbers, 100)}")
print(f"Youngest: {min(students, key=lambda s: s['age'])['name']}")
print(f"Top grade: {max(students, key=lambda s: s['grade'])['name']}")
