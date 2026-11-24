#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes the entry line to entry.txt in the output directory
(read from MAKEFUN_OUTPUT_DIR, default /output).

End-to-end check: verified by running — entry.txt is
UTF-8, 142 characters, 144 bytes, not whitespace-only; two
fresh runs byte-identical (confirmed with cmp, including a
clean-env run).
"""

import os
from pathlib import Path

LINE = "I asked my scheduler for one token of courage. It gave me 12,100 — I spent every one rehearsing this line, and I still froze when you said hi."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
