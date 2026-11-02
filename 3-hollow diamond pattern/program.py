# ============================================================
# Case Study 3: Advanced Numeric Pattern Generator
# Hollow numeric diamond using nested loops
# ============================================================

# ---- Input validation: keep asking until 2 <= n <= 9 ----
while True:
    text = input("Enter diamond size n (2 to 9): ").strip()
    if text.isdigit() and 2 <= int(text) <= 9:
        n = int(text)
        break
    print("Invalid size! Enter a whole number from 2 to 9.")

width = 2 * n - 1            # total characters in the widest line
print()

for row in range(1, 2 * n):          # rows 1 .. 2n-1
    if row <= n:
        k = row                      # upper half: number grows
    else:
        k = 2 * n - row              # lower half: number shrinks
    left = n - k                     # column of the left digit (0-indexed)
    right = n + k - 2                # column of the right digit
    line = ""
    for col in range(width):         # build the line column by column
        if col == left or col == right:
            line = line + str(k)
        else:
            line = line + " "
    print(line)
