# ============================================================
# Case Study 1: University Scholarship Allocation
# Uses: lists, tuples, tuple unpacking, loops, conditions
# ============================================================

# ---- Policy constants (change these to test other policies) ----
SUBJECTS = ["Maths", "Physics", "Programming"]
MIN_AGGREGATE = 60.0     # minimum average marks (%)
MIN_SUBJECT = 40         # minimum marks in EVERY subject
MIN_ATTENDANCE = 75      # minimum attendance (%)
MAX_INCOME = 300000      # maximum yearly family income (Rs.)
QUOTA = 3                # number of scholarships available

# ---- Applicant data: (id, name, [marks], attendance, income) ----
students = [
    ("S101", "Asha",   [88, 92, 79], 95, 250000),
    ("S102", "Bhanu",  [75, 80, 90], 82, 180000),
    ("S103", "Charan", [90, 70, 85], 90, 120000),
    ("S104", "Divya",  [55, 38, 70], 88, 150000),
    ("S105", "Esha",   [95, 96, 97], 70, 100000),
    ("S106", "Farhan", [60, 62, 58], 80, 450000),
    ("S107", "Gita",   [70, 72, 68], 91, 200000),
    ("S108", "Harsh",  [45, 50, 48], 85, 90000),
    ("S109", "Isha",   [80, 85, 75], 77, 280000),
    ("S110", "Jaya",   [65, 66, 64], 76, 290000),
]

eligible = []    # will hold (id, name, total, first_subject_marks, income, attendance)
print("=== STEP 1: ELIGIBILITY CHECK ===")

for record in students:
    sid, name, marks, attendance, income = record   # tuple unpacking

    total = 0
    for m in marks:
        total = total + m
    aggregate = total / len(marks)

    reasons = []                                    # list of failed conditions
    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate " + str(round(aggregate, 2)) + " < " + str(MIN_AGGREGATE))
    for i in range(len(marks)):
        if marks[i] < MIN_SUBJECT:
            reasons.append(SUBJECTS[i] + " " + str(marks[i]) + " < " + str(MIN_SUBJECT))
    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance " + str(attendance) + " < " + str(MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("income " + str(income) + " > " + str(MAX_INCOME))

    if len(reasons) == 0:
        eligible.append((sid, name, total, marks[0], income, attendance))
        print(sid, name, "-> ELIGIBLE (aggregate", str(round(aggregate, 2)) + ")")
    else:
        print(sid, name, "-> REJECTED:", "; ".join(reasons))

# ---- Ranking using bubble sort ----
# Tie-break order: 1) higher total, 2) higher Maths marks,
#                  3) lower income, 4) smaller ID
n = len(eligible)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = eligible[j]
        b = eligible[j + 1]
        b_is_better = False
        if b[2] > a[2]:
            b_is_better = True
        elif b[2] == a[2]:
            if b[3] > a[3]:
                b_is_better = True
            elif b[3] == a[3]:
                if b[4] < a[4]:
                    b_is_better = True
                elif b[4] == a[4] and b[0] < a[0]:
                    b_is_better = True
        if b_is_better:
            eligible[j], eligible[j + 1] = b, a     # swap

print()
print("=== STEP 2: RANKED LIST (Quota =", QUOTA, ") ===")
print("Rank  ID    Name     Total  Maths  Income   Result")
rank = 1
for sid, name, total, maths, income, att in eligible:
    if rank <= QUOTA:
        result = "AWARDED"
    else:
        result = "WAITLIST"
    print(str(rank).ljust(5), sid.ljust(5), name.ljust(8), str(total).ljust(6),
          str(maths).ljust(6), str(income).ljust(8), result)
    rank = rank + 1

if len(eligible) == 0:
    print("No eligible applicants.")
