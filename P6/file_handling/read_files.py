import os

sample_path = "sample_read.txt"
with open(sample_path, "w", encoding="utf-8") as f:
    f.write("Alice 85\n")
    f.write("Bob 92\n")
    f.write("Carol 78\n")
    f.write("Dave 95\n")
    f.write("Eve 88\n")

print("=== read() ===")
with open(sample_path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

print("=== readline() ===")
with open(sample_path, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(f"  > {line.strip()}")

print("\n=== readlines() ===")
with open(sample_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print(f"  Line {i}: {line.strip()}")

print("\n=== Iterating file object ===")
with open(sample_path, "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")

print("\n=== Parsed data ===")
records = []
with open(sample_path, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            records.append((parts[0], int(parts[1])))

for name, score in records:
    print(f"  {name}: {score}")

scores = [s for _, s in records]
print(f"\n  Max: {max(scores)}, Min: {min(scores)}, Avg: {sum(scores)/len(scores):.1f}")

print("\n=== read(10) ===")
with open(sample_path, "r", encoding="utf-8") as f:
    print(f"  First 10 chars: '{f.read(10)}'")

os.remove(sample_path)
print("\nTemp file removed.")
