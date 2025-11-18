from pathlib import Path
from scoring.score_utils import extract_final_score
from config import PREV_EVAL_DIR

def load_previous_score(index: int) -> int | None:
    f = PREV_EVAL_DIR / f"{index:03}_evaluation.txt"
    if not f.exists():
        return None
    txt = f.read_text(encoding="utf-8", errors="ignore")
    return extract_final_score(txt)
