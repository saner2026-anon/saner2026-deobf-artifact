import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")

DATASET_PATH = Path(os.getenv(
    "DATASET_PATH",
    "Java-de-obfuscation-dataset.jsonl"
))

PROMPT_DIR = Path(os.getenv(
    "DEOBFUSCATION_PROMPT_DIR",
    "prompts"
))

PROMPT_PATH = os.getenv("DEOBFUSCATION_PROMPT_PATH", None)

PREV_EVAL_DIR = Path(os.getenv("PREV_EVAL_DIR", "previous_evaluations"))

OUT_DIR = Path("output")
OUT_DIR.mkdir(exist_ok=True)
