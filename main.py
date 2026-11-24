import os

TEXT = "I put up missing posters for my dog all over the neighborhood, with my phone number in tear-off tabs. This morning every tab was gone, and someone had written under his photo: FOUND YOU."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
