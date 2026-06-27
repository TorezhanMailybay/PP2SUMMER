from itertools import zip_longest

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("=== enumerate() ===")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

print("\nFruits with len > 5:")
for i, fruit in enumerate(fruits):
    if len(fruit) > 5:
        print(f"  index {i} -> '{fruit}'")

position = {fruit: i for i, fruit in enumerate(fruits)}
print(f"\nPosition dict: {position}")

lines = ["Line A\n", "Line B\n", "Line C\n"]
for line_no, line in enumerate(lines, start=1):
    print(f"  {line_no:3d}: {line.rstrip()}")

names  = ["Alice", "Bob", "Carol", "Dave"]
scores = [92, 78, 85, 61]
grades = ["A", "C", "B", "D"]

print("\n=== zip() ===")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

print()
for name, score, grade in zip(names, scores, grades):
    print(f"  {name:6s} {score:3d}  Grade: {grade}")

print(f"\nzip -> dict: {dict(zip(names, scores))}")

print("\nIndexed pairs:")
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"  {i}. {name} — {score}")

nums, letters = zip(*[(1, "a"), (2, "b"), (3, "c")])
print(f"\nUnzipped: nums={list(nums)}, letters={list(letters)}")

print("\nzip_longest:")
for pair in zip_longest([1, 2], ["a", "b", "c", "d"]):
    print(f"  {pair}")

print("\n=== sorted() ===")
nums2 = [5, 2, 9, 1, 7, 3]
print(f"Ascending:  {sorted(nums2)}")
print(f"Descending: {sorted(nums2, reverse=True)}")

words = ["banana", "apple", "kiwi", "cherry", "fig"]
print(f"By length:  {sorted(words, key=len)}")
print(f"By alpha:   {sorted(words)}")

students = [
    {"name": "Alice",  "grade": 92},
    {"name": "Bob",    "grade": 78},
    {"name": "Carol",  "grade": 85},
    {"name": "Dave",   "grade": 61},
]
for i, s in enumerate(sorted(students, key=lambda s: s["grade"], reverse=True), 1):
    print(f"  {i}. {s['name']:6s} {s['grade']}")

lst = [10, 3, 7, 1]
lst.sort()
print(f"In-place .sort(): {lst}")

print("\n=== Type conversions ===")
print(int("42"), int(3.99), int("1010", 2), int("FF", 16))
print(float("3.14"), float(7))
print(str(123), str(3.14), str(True))

for val in [0, 1, "", "hi", [], [1], None, 3.14]:
    print(f"  bool({str(val):<8}) = {bool(val)}")

print(list((1, 2, 3)))
print(tuple([4, 5, 6]))
print(set([1, 2, 2, 3, 3, 3]))
print(dict([("a", 1), ("b", 2), ("c", 3)]))

print("\n=== type() and isinstance() ===")
values = [42, 3.14, "hello", True, [1, 2], {"k": "v"}, (1,), {1, 2}]
for v in values:
    print(f"  {str(v):<15} type={type(v).__name__:<8} isinstance(int)={isinstance(v, int)}")

print(f"\ntype(True) is int     : {type(True) is int}")
print(f"isinstance(True, int) : {isinstance(True, int)}")
