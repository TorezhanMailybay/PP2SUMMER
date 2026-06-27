import os
import shutil
from pathlib import Path
from datetime import datetime

src = Path("source.txt")
src.write_text("Line 1\nLine 2\nLine 3\nImportant data here!\n", encoding="utf-8")
print(f"Created: {src}")

shutil.copy(src, "source_copy.txt")
print("Copied to: source_copy.txt")

shutil.copy2(src, "source_copy2.txt")
print("Copied with metadata to: source_copy2.txt")

backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
shutil.copy2(src, backup_dir / f"source_{timestamp}.txt")
print(f"Backup created in: {backup_dir}/")

shutil.move("source_copy.txt", "renamed_source.txt")
print("Moved source_copy.txt -> renamed_source.txt")

def safe_delete(path):
    p = Path(path)
    if p.exists():
        p.unlink()
        print(f"Deleted: {p}")
    else:
        print(f"Not found: {p}")

safe_delete("renamed_source.txt")
safe_delete("source_copy2.txt")

shutil.rmtree(backup_dir)
print(f"Removed directory: {backup_dir}")

print(f"\nFile info for {src}:")
print(f"  Exists: {src.exists()}")
print(f"  Size:   {src.stat().st_size} bytes")
print(f"  Path:   {src.resolve()}")
print(f"  Suffix: {src.suffix}")

safe_delete(src)
