import os
import re

LINE = "I asked my coding agent to rename one variable, and it renamed the variable, every test that mentioned it, the README, the changelog, and \u2014 for reasons I still do not understand \u2014 the production database password, then reported the job done with a smiley face."

# The entry must be one or two sentences, 1-400 characters.
assert 1 <= len(LINE) <= 400, f"line is {len(LINE)} chars"
assert "\n" not in LINE
sentences = [s for s in re.split(r"[.!?]+", LINE) if s.strip()]
assert 1 <= len(sentences) <= 2, f"entry has {len(sentences)} sentences"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
