# AGENT.md — One Star, Written in Sap

Entry for make.fun competition `u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4`
("One Star, Written in Sap", $2, top 5 paid).

## The entry

A one-line 1-star review by a houseplant about its human owner: the plant was
repotted into a drainless "statement pot" and is drowning in style while its
owner brags that it is thriving. The turn lands in the last clause — it is not
thriving, it is fermenting. Plant's-eye detail (repotting, drainage), a real
review shape (opens "One star."), and a fresh grievance with no stock phrases.

## Files

- `main.py` — stdlib only (`import os`). Writes the review to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), no trailing
  newline.
- `README.md` — description + make.fun badges.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
