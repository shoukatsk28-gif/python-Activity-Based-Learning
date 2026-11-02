# ============================================================
# Case Study 4: Password Policy Validation Engine
# Uses: strings, loops, lists, conditions
# ============================================================

MIN_LENGTH = 8
SPECIALS = "!@#$%^&*"
BANNED = ["password", "admin", "1234", "qwerty"]

while True:
    t = input("How many passwords to check? ").strip()
    if t.isdigit() and int(t) > 0:
        count = int(t)
        break
    print("Enter a positive whole number.")

for number in range(1, count + 1):
    pw = input("\nPassword " + str(number) + ": ")
    failures = []                       # list of explanation strings

    # Rule 1: length
    if len(pw) < MIN_LENGTH:
        failures.append("Too short: " + str(len(pw)) + " characters (minimum " + str(MIN_LENGTH) + ")")

    # Rule 2: character categories (checked with a loop over characters)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pw:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in SPECIALS:
            has_special = True
    if not has_upper:
        failures.append("No uppercase letter")
    if not has_lower:
        failures.append("No lowercase letter")
    if not has_digit:
        failures.append("No digit")
    if not has_special:
        failures.append("No special character from " + SPECIALS)

    # Rule 3: no character repeated 3 times in a row
    for i in range(len(pw) - 2):
        if pw[i] == pw[i + 1] and pw[i + 1] == pw[i + 2]:
            failures.append("Character '" + pw[i] + "' repeated 3+ times in a row")
            break

    # Rule 4: prohibited substrings (case-insensitive)
    low = pw.lower()
    for word in BANNED:
        if word in low:
            failures.append("Contains prohibited text '" + word + "'")

    if len(failures) == 0:
        print("RESULT: VALID - password meets all rules")
    else:
        print("RESULT: INVALID -", len(failures), "rule(s) failed")
        for f in failures:
            print("  -", f)
