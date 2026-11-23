"""Entry for make.fun bounty u-daring-gecko-25-one-line-laugh-sprint-cda708b2.

Writes one original funny line (everyday life, <= 200 characters) to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

# Selected entry: ranked #1 of 6 candidates (see candidates.md).
# It won the self-judge tournament on the house judge brief: on-subject
# (a dentist visit), a setup-punchline twist that pays off in the last
# words, fresh phrasing, and economy -- 87 characters, one breath, no filler.
# Runner-up kept in candidates.md (elevator mirrors) if a swap is needed.
SELECTED_LINE = (
    "My dentist asked if I floss. I said 'emotionally, yes' "
    "\u2014 and we both agreed to move on."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SELECTED_LINE)


if __name__ == "__main__":
    main()
