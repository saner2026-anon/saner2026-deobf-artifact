import json
from prompts.load_prompt import load_deobfuscation_prompt
from llm.regenerate import regenerate_deobfuscation
from llm.evaluate_quality import evaluate_deobfuscation
from llm.evaluate_similarity import evaluate_similarity
from scoring.score_utils import extract_final_score
from scoring.prev_score import load_previous_score
from utils.index_loader import parse_indices_from_env, parse_indices_from_cli
from utils.dataset_loader import load_dataset
from utils.io_utils import save_output, save_used_indices

def process(indices):
    prompt = load_deobfuscation_prompt()
    used = []

    for idx, line in enumerate(load_dataset()):
        if idx not in indices:
            continue

        item = json.loads(line)
        if item.get("language") != "java":
            print(f"[{idx:03}] Skip")
            continue

        obf = item.get("obfuscated_code")
        ref = item.get("deobfuscated_code")

        print(f"[{idx:03}] Regenerating...")
        try:
            regen = regenerate_deobfuscation(obf, prompt)
        except Exception as e:
            regen = f"__DEOBFUSCATION_ERROR__\n{e}"

        print(f"[{idx:03}] Evaluating...")
        try:
            evaluation = evaluate_deobfuscation(obf, regen, ref)
        except Exception as e:
            evaluation = f"__EVALUATION_ERROR__\n{e}"

        print(f"[{idx:03}] Similarity...")
        try:
            similarity = evaluate_similarity(ref, regen)
        except Exception as e:
            similarity = f"__SIMILARITY_ERROR__\n{e}"

        prev = load_previous_score(idx)
        new = extract_final_score(evaluation)
        improved = None if prev is None or new is None else (new > prev)

        summary = (
            f"Index: {idx}\n"
            f"Previous Score: {prev if prev is not None else 'N/A'}\n"
            f"New Score: {new if new is not None else 'N/A'}\n"
            f"Improved: "
            f"{('YES' if improved else 'NO') if improved is not None else 'UNKNOWN'}\n"
        )

        save_output(idx, regen, evaluation, similarity, summary)
        used.append(idx)
        print(f"[{idx:03}] Done✓")

    save_used_indices(used)
    print("Finished.")

if __name__ == "__main__":
    import sys
    cli_indices = parse_indices_from_cli(sys.argv[1:])
    env_indices = parse_indices_from_env()
    indices = cli_indices if cli_indices else env_indices
    if not indices:
        print("No indices provided.")
    else:
        process(indices)
