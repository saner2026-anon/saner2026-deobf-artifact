from pathlib import Path
from config import OUT_DIR

def save_output(index: int, regen: str, evaluation: str, similarity: str, summary: str):
    (OUT_DIR / f"{index:03}_regenerated.java").write_text(regen, encoding="utf-8")
    (OUT_DIR / f"{index:03}_evaluation.txt").write_text(evaluation, encoding="utf-8")
    (OUT_DIR / f"{index:03}_similarity.txt").write_text(similarity, encoding="utf-8")
    (OUT_DIR / f"{index:03}_score_compare.txt").write_text(summary, encoding="utf-8")

def save_used_indices(indices: list[int]):
    (OUT_DIR / "used_indices.txt").write_text("\n".join(map(str, indices)), encoding="utf-8")
