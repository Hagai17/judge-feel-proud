#!/usr/bin/env python3
"""Entry for make.fun bounty: Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (256 characters) to /output/entry.txt and
prints it. The scene: a father teaches his son to shave; years later the
son, grown taller, shaves the father -- the same mirror, the same chin
resting on a head, the roles quietly reversed.

Why this scene (duel record in candidates.md): the published judge brief
weighs, in order, a real family scene, heartfelt affection over stuck-on
sentiment, a light recognisable laugh, economy, and one specific fresh
detail. The mirrored chin-on-head beat carries the affection physically
rather than declaring it, and the father's closing line ('Now we're
even') is the small wry turn a family would actually laugh at. The draft
beat the strongest sampled field entries in both orders under the brief;
the saturated field lanes (a place set for a grandparent who has died,
burnt toast, the wobbly table) were avoided entirely.
"""

import os

# The scene is built from its beats, in order: the lesson, the reversal,
# the small failure, the father's verdict. Joined, they are one breath.
BEATS = [
    "My father taught me to shave standing behind me at the mirror, his chin "
    "resting on my head.",
    "Last winter his hands shook too much, so I stood behind him and rested "
    "my chin on his head.",
    "I nicked him once.",
    "He wiped the blood, grinning: 'Good. Now we're even.'",
]

ENTRY = " ".join(BEATS)


def main() -> None:
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1 to 280
    # characters that is not only whitespace. Fail loudly here rather
    # than be silently invalid before the judge.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
