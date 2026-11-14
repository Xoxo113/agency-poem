#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

The poem is embedded below and written byte-for-byte; the program is
deterministic and uses no network, randomness or clock.
"""

import os

POEM = """Running behind the bicycle,
one hand spread flat on the saddle,
I am all agency and no journey:
the wheels are spinning a morning that isn't mine.

"Don't let go," she says.
"I won't," I say —
the kindest lie a hand can tell.

Then the road opens ahead of her,
and my palm floats up like a bird
off a branch it never owned.

She never looks back.
That is how I know the riding is hers now —
not the hand on the saddle,
but the shaped air where it was.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = POEM.encode("utf-8")
    # The gate: UTF-8 text of 1 to 1,000 characters, not only whitespace.
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 1000, f"poem is {len(text)} characters"
    assert text.strip(), "poem is only whitespace"
    # Write to a temp file, verify the bytes round-trip, then rename into
    # place so /output/entry.txt never holds a partial write.
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "wb") as f:
        f.write(data)
    with open(tmp_path, "rb") as f:
        assert f.read() == data, "written bytes differ from the poem"
    os.replace(tmp_path, final_path)


if __name__ == "__main__":
    main()
