# ============================================================
# Case Study 5: Text Compression Using Character Runs (RLE)
# Uses: strings, while loops, nested loops, conditions
# ============================================================

print("Run-Length Encoder (press Enter on an empty line to quit)")

while True:
    s = input("\nEnter text: ")
    if s == "":
        print("Goodbye!")
        break

    encoded = ""
    i = 0
    while i < len(s):
        ch = s[i]
        run = 1
        # count how many times this character repeats consecutively
        while i + run < len(s) and s[i + run] == ch:
            run = run + 1
        encoded = encoded + ch + str(run)      # e.g. "aaa" -> "a3"
        i = i + run                            # jump past the whole run

    print("Original :", s, "(length", len(s), ")")
    print("Encoded  :", encoded, "(length", len(encoded), ")")

    if len(encoded) < len(s):
        saved = len(s) - len(encoded)
        percent = saved * 100 / len(s)
        print("Result   : Compression BENEFICIAL - saved", saved,
              "characters (" + str(round(percent, 1)) + "%)")
    elif len(encoded) == len(s):
        print("Result   : No change in size - encoding not beneficial, keep original")
    else:
        extra = len(encoded) - len(s)
        print("Result   : Encoding made it", extra, "characters LONGER - not beneficial, keep original")
