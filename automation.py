# Automation example: batch rename files
from pathlib import Path

def batch_rename(folder: str, prefix: str) -> None:
    for i, f in enumerate(Path(folder).glob("*.txt"), 1):
        f.rename(f.with_name(f"{prefix}_{i:03d}.txt"))

# batch_rename("./files", "doc")
- Add helper — iteration 3 (2015)
- Update docs — iteration 6 (2015)
- Improve naming — iteration 7 (2015)
