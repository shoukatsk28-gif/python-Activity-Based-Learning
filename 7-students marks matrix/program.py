# ============================================================
# Case Study 7: Student Marks Matrix Analysis
# Uses: nested lists, nested loops, row/column statistics
# ============================================================

names = ["Anil", "Bhavya", "Chitra", "Deepak", "Eshwar", "Fatima"]
subjects = ["Maths", "Physics", "Chemistry", "Python"]
marks = [                       # nested list: one row per student
    [78, 82, 59, 91],
    [92, 88, 95, 97],
    [45, 38, 52, 60],
    [30, 42, 38, 55],
    [66, 71, 48, 80],
    [55, 49, 40, 72],
]
PASS_MARK = 35          # below this in any subject = fail in that subject
LOW_AVERAGE = 60        # subject average below this is flagged as weak

rows = len(marks)
cols = len(subjects)

# ---- Row-wise statistics ----
totals = []
averages = []
for r in range(rows):
    t = 0
    for c in range(cols):
        t = t + marks[r][c]
    totals.append(t)
    averages.append(t / cols)

# ---- Print the marks table ----
print("MARKS TABLE")
header = "Name".ljust(8)
for s in subjects:
    header = header + s.ljust(11)
print(header + "Total  Average")
for r in range(rows):
    line = names[r].ljust(8)
    for c in range(cols):
        line = line + str(marks[r][c]).ljust(11)
    print(line + str(totals[r]).ljust(7) + str(round(averages[r], 2)))

# ---- Column-wise statistics ----
print("\nSUBJECT STATISTICS")
weak_subjects = []
for c in range(cols):
    col_total = 0
    highest = marks[0][c]
    lowest = marks[0][c]
    high_name = names[0]
    low_name = names[0]
    for r in range(rows):
        value = marks[r][c]
        col_total = col_total + value
        if value > highest:
            highest = value
            high_name = names[r]
        if value < lowest:
            lowest = value
            low_name = names[r]
    avg = col_total / rows
    print(subjects[c].ljust(10), "average", str(round(avg, 2)).ljust(6),
          "highest", highest, "(" + high_name + ")",
          "lowest", lowest, "(" + low_name + ")")
    if avg < LOW_AVERAGE:
        weak_subjects.append(subjects[c])

# ---- Top performer(s): handles ties ----
best = totals[0]
for t in totals:
    if t > best:
        best = t
top = []
for r in range(rows):
    if totals[r] == best:
        top.append(names[r])
print("\nTOP PERFORMER(S):", ", ".join(top), "with total", best)

# ---- Weak subjects ----
if len(weak_subjects) == 0:
    print("No subject has an average below", LOW_AVERAGE)
else:
    print("LOW-AVERAGE SUBJECT(S) (below " + str(LOW_AVERAGE) + "):", ", ".join(weak_subjects))

# ---- Students failing any subject ----
print("\nSUBJECT FAILURES (below " + str(PASS_MARK) + ")")
anyone = False
for r in range(rows):
    failed = []
    for c in range(cols):
        if marks[r][c] < PASS_MARK:
            failed.append(subjects[c])
    if len(failed) > 0:
        print(names[r], "failed in", ", ".join(failed))
        anyone = True
if not anyone:
    print("None")

# ---- Rank list (bubble sort on an index list) ----
order = list(range(rows))
for i in range(rows - 1):
    for j in range(rows - 1 - i):
        if totals[order[j]] < totals[order[j + 1]]:
            order[j], order[j + 1] = order[j + 1], order[j]
print("\nRANK LIST")
for position in range(rows):
    idx = order[position]
    print(position + 1, names[idx], totals[idx])
