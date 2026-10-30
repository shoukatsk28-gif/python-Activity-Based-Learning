# ============================================================
# Case Study 6: Nested Loop Calendar Generator
# Uses: nested loops, strings, validation, conditions
# ============================================================

# ---- Input with validation ----
while True:
    t = input("Number of days in the month (28-31): ").strip()
    if t.isdigit() and 28 <= int(t) <= 31:
        days = int(t)
        break
    print("Invalid! A month has 28, 29, 30 or 31 days.")

while True:
    t = input("Starting weekday (1=Mon, 2=Tue, ... 7=Sun): ").strip()
    if t.isdigit() and 1 <= int(t) <= 7:
        start = int(t)
        break
    print("Invalid! Enter a number from 1 to 7.")

month_name = input("Month name (for the title): ").strip()

# ---- Print the calendar ----
print()
print("      " + month_name)
print("Mo Tu We Th Fr Sa Su")

day = 1                                  # next date to print
for week in range(6):                    # a month needs at most 6 week-rows
    if day > days:
        break                            # all dates printed, stop early
    line = ""
    for column in range(1, 8):           # columns 1 (Mon) .. 7 (Sun)
        if week == 0 and column < start:
            line = line + "   "          # blank cell before the 1st
        elif day > days:
            line = line + "   "          # blank cell after the last date
        else:
            if day < 10:
                line = line + " " + str(day) + " "    # width = 3 characters
            else:
                line = line + str(day) + " "
            day = day + 1
    print(line)
