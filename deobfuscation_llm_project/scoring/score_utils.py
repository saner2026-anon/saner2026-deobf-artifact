import re

_SCORE = re.compile(r"\*{0,2}Final Score\*{0,2}\s*:\s*(\d{1,3})")

def extract_final_score(text: str) -> int | None:
    m = _SCORE.search(text or "")
    if not m:
        return None
    try:
        v = int(m.group(1))
        return v if 0 <= v <= 100 else None
    except:
        return None
