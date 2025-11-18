from pathlib import Path
from config import PROMPT_DIR, PROMPT_PATH

def load_deobfuscation_prompt() -> str:
    if PROMPT_PATH:
        p = Path(PROMPT_PATH)
        if not p.exists():
            raise FileNotFoundError(f"Prompt file not found: {p}")
        return p.read_text(encoding="utf-8")

    pdir = Path(PROMPT_DIR)
    if not pdir.exists():
        raise FileNotFoundError(f"Prompt directory not found: {pdir}")

    txt_files = sorted(pdir.glob("*.txt"))
    if not txt_files:
        raise FileNotFoundError(f"No .txt prompt files in {pdir}")

    return txt_files[0].read_text(encoding="utf-8")
