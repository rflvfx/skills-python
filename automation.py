# Automation example: batch rename files
from pathlib import Path

def batch_rename(folder: str, prefix: str) -> None:
    for i, f in enumerate(Path(folder).glob("*.txt"), 1):
        f.rename(f.with_name(f"{prefix}_{i:03d}.txt"))

# batch_rename("./files", "doc")
- Add helper — iteration 3 (2015)
- Update docs — iteration 6 (2015)
- Improve naming — iteration 7 (2015)
- Improve naming — iteration 10 (2015)
- Update config — iteration 16 (2015)
- Add example — iteration 21 (2015)
- Polish code — iteration 23 (2015)
- Tweak implementation — iteration 26 (2015)
- Update dependencies — iteration 27 (2015)
- Polish code — iteration 28 (2015)
- Add validation — iteration 30 (2015)
- Add feature — iteration 32 (2015)
- Add validation — iteration 38 (2015)
- Polish code — iteration 39 (2015)
- Fix typo — iteration 43 (2015)
- Update docs — iteration 44 (2015)
- Optimize performance — iteration 46 (2015)
- Improve naming — iteration 49 (2015)
- Update config — iteration 53 (2015)
- Add helper — iteration 57 (2015)
- Add feature — iteration 60 (2015)
