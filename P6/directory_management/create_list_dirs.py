import os
import shutil
from pathlib import Path

print(f"Current directory: {os.getcwd()}")

single_dir = Path("my_project")
if not single_dir.exists():
    os.mkdir(single_dir)
print(f"Created: {single_dir}")

os.makedirs("my_project/src/utils", exist_ok=True)
for d in ["my_project/data/raw", "my_project/data/processed", "my_project/tests", "my_project/docs"]:
    os.makedirs(d, exist_ok=True)

files = {
    "my_project/src/main.py": "print('Hello!')\n",
    "my_project/src/utils/helpers.py": "def helper(): pass\n",
    "my_project/data/raw/data.csv": "id,name\n1,Alice\n",
    "my_project/tests/test_main.py": "def test_main(): pass\n",
    "my_project/README.md": "# My Project\n",
}
for path, content in files.items():
    Path(path).write_text(content, encoding="utf-8")

print("\nos.listdir('my_project'):")
for entry in sorted(os.listdir("my_project")):
    kind = "DIR " if Path("my_project/" + entry).is_dir() else "FILE"
    print(f"  {kind}  {entry}")

print("\nos.walk():")
for root, dirs, filenames in os.walk("my_project"):
    level = root.replace("my_project", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")
    for file in filenames:
        print(f"{indent}  {file}")

print("\n.py files:")
for f in sorted(Path("my_project").rglob("*.py")):
    print(f"  {f}")

original = os.getcwd()
os.chdir("my_project")
print(f"\nChanged to: {os.getcwd()}")
os.chdir(original)
print(f"Back to:    {os.getcwd()}")

os.makedirs("my_project/empty_temp", exist_ok=True)
os.rmdir("my_project/empty_temp")
print("Removed empty dir: my_project/empty_temp")

shutil.rmtree("my_project")
print("Removed: my_project/")
