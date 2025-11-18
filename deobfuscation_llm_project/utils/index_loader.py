import json
import os
from pathlib import Path

def parse_indices_from_env() -> list[int]:
    raw = os.getenv("INDICES", "")
    if not raw.strip():
        return []
    return [int(x.strip()) for x in raw.split(",")]

def parse_indices_from_cli(args) -> list[int]:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--indices")
    parser.add_argument("--indices-file")
    p = parser.parse_args(args)

    if p.indices:
        return [int(x.strip()) for x in p.indices.split(",")]

    if p.indices_file:
        f = Path(p.indices_file)
        if not f.exists():
            raise FileNotFoundError(p.indices_file)
        txt = f.read_text().strip()
        try:
            arr = json.loads(txt)
            if isinstance(arr, list):
                return [int(x) for x in arr]
        except:
            pass
        return [int(l.strip()) for l in txt.splitlines() if l.strip()]

    return []
