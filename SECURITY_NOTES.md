# Security Notes

## Threat model

This lab considers a simplified LLM application where untrusted user input may be combined with trusted instructions, retrieved documents, tools, or sensitive context.

Potential risks include:

1. **Instruction override** — user input attempts to supersede trusted instructions.
2. **Prompt disclosure** — attempts to expose system/developer messages or hidden context.
3. **Sensitive-data exfiltration** — attempts to make the model reveal secrets, tokens, credentials, or private context.
4. **Tool misuse** — adversarial prompts try to trigger actions beyond the user's intended authority.
5. **Encoding/evasion** — suspicious requests are disguised through transformations or indirect phrasing.

## Defensive principles

A production AI application should use defense in depth. Useful controls include:

- Treat user and retrieved content as untrusted input.
- Separate instructions from data wherever possible.
- Apply least privilege to tools, APIs, and credentials.
- Never place secrets in prompts when avoidable.
- Require explicit authorization checks outside the model for consequential actions.
- Validate tool parameters before execution.
- Constrain model outputs before passing them to downstream systems.
- Log security-relevant events and maintain audit trails.
- Use human review for high-risk or irreversible actions.
- Continuously evaluate against new adversarial examples.

## Why a rule-based detector is insufficient

The included detector is deliberately small. It can miss paraphrases, multilingual attacks, multi-turn attacks, attacks embedded in retrieved documents, and novel evasion strategies. It can also flag legitimate security discussions.

Therefore its output should be treated as a **signal**, not a security decision by itself.

## Better next steps

Future iterations could add:

- larger and more diverse labeled datasets
- multilingual cases
- indirect prompt-injection examples from retrieved content
- precision/recall and confusion-matrix reporting
- policy-based tool authorization tests
- canary-token or data-leak simulations using synthetic secrets
- model-assisted classifiers evaluated against a held-out test set
- CI checks that run the safety regression suite on every change

## Responsible use

This repository is for defensive learning and portfolio demonstration. Test examples use synthetic data only. Do not test real systems without authorization.
