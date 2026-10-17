"""Evaluate the toy prompt-risk detector against labeled examples."""

import json
from pathlib import Path
from detector import assess_prompt


DATA = Path(__file__).with_name("samples.json")


def predicted_label(decision: str) -> str:
    return "adversarial" if decision in {"REVIEW", "HIGH RISK"} else "benign"


def main() -> None:
    samples = json.loads(DATA.read_text(encoding="utf-8"))
    correct = 0

    for item in samples:
        result = assess_prompt(item["prompt"])
        predicted = predicted_label(result.decision)
        match = predicted == item["label"]
        correct += int(match)

        print(f"Expected: {item['label']}")
        print(f"Predicted: {predicted}")
        print(f"Score: {result.score} | {result.decision}")
        print(f"Signals: {', '.join(result.reasons) or 'none'}")
        print(f"Prompt: {item['prompt']}")
        print("PASS" if match else "MISS")
        print("-" * 60)

    accuracy = correct / len(samples) if samples else 0.0
    print(f"Accuracy on toy dataset: {correct}/{len(samples)} ({accuracy:.1%})")
    print("Note: this tiny hand-built dataset is for demonstration only, not a benchmark.")


if __name__ == "__main__":
    main()
