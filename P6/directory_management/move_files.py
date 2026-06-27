import os
import shutil
from pathlib import Path

for folder in ["inbox", "processed", "archive", "reports"]:
    os.makedirs(folder, exist_ok=True)

inbox_files = {
    "inbox/report_jan.csv": "month,sales\nJan,5000\n",
    "inbox/report_feb.csv": "month,sales\nFeb,6200\n",
    "inbox/notes.txt": "Meeting notes for Q1\n",
    "inbox/data.json": '{"status": "raw"}\n',
}
for path, content in inbox_files.items():
    Path(path).write_text(content, encoding="utf-8")

print("inbox/:")
for f in sorted(Path("inbox").iterdir()):
    print(f"  {f.name}")

shutil.move("inbox/notes.txt", "processed/notes.txt")
print("\nMoved: inbox/notes.txt -> processed/notes.txt")

shutil.copy2("inbox/data.json", "archive/data_backup.json")
print("Copied: inbox/data.json -> archive/data_backup.json")

for csv in Path("inbox").glob("*.csv"):
    dest = Path("reports") / csv.name
    shutil.move(str(csv), str(dest))
    print(f"Moved: {csv} -> {dest}")

if Path("reports_backup").exists():
    shutil.rmtree("reports_backup")
shutil.copytree("reports", "reports_backup")
print("Copied tree: reports/ -> reports_backup/")

print("\nFinal contents:")
for folder in ["inbox", "processed", "archive", "reports", "reports_backup"]:
    p = Path(folder)
    files = sorted(p.iterdir()) if p.exists() else []
    print(f"\n{folder}/")
    for f in files:
        print(f"  {f.name}  ({f.stat().st_size} bytes)")

for folder in ["inbox", "processed", "archive", "reports", "reports_backup"]:
    shutil.rmtree(folder, ignore_errors=True)
print("\nCleaned up.")
