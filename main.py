import os

ENTRY = (
    "One star. She repotted me into a 'statement pot' with no drainage hole, "
    "so now I drown in style while she tells guests I'm thriving \u2014 "
    "I am not thriving, I am fermenting."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
