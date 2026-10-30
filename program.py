# ============================================================
# Case Study 8: Tuple-Based Employee Shift Conflict Detection
# Uses: tuples, tuple unpacking, lists, nested loops
# ============================================================

# Each shift is a tuple: (employee, day, start_hour, end_hour) in 24-hour time
shifts = [
    ("E01", "Mon", 9, 17),
    ("E02", "Mon", 9, 13),
    ("E01", "Mon", 16, 20),     # overlaps with E01's first shift
    ("E03", "Tue", 8, 16),
    ("E02", "Mon", 12, 18),     # overlaps with E02's first shift
    ("E03", "Tue", 16, 22),     # touches (not overlaps) E03's first shift
    ("E04", "Wed", 14, 10),     # invalid: ends before it starts
    ("E01", "Tue", 9, 17),
    ("E01", "Tue", 17, 23),     # back-to-back, no conflict
    ("E05", "Thu", 6, 26),      # invalid: hour above 24
]

# ---- Step 1: separate valid and invalid shifts ----
valid_shifts = []
print("=== VALIDATION ===")
for shift in shifts:
    emp, day, start, end = shift                  # unpacking
    if start < 0 or end > 24 or start >= end:
        print("INVALID shift:", shift)
    else:
        valid_shifts.append(shift)
print("Valid shifts:", len(valid_shifts), "| Invalid shifts:", len(shifts) - len(valid_shifts))

# ---- Step 2: compare every pair of valid shifts ----
print("\n=== CONFLICTS ===")
conflict_employees = []
conflict_count = 0
for i in range(len(valid_shifts)):
    for j in range(i + 1, len(valid_shifts)):
        e1, d1, s1, f1 = valid_shifts[i]
        e2, d2, s2, f2 = valid_shifts[j]
        if e1 == e2 and d1 == d2:                 # same employee, same day
            if s1 < f2 and s2 < f1:               # interval overlap test
                latest_start = s1
                if s2 > s1:
                    latest_start = s2
                earliest_end = f1
                if f2 < f1:
                    earliest_end = f2
                overlap = earliest_end - latest_start
                print(e1, d1, ":", (s1, f1), "overlaps", (s2, f2), "->", overlap, "hour(s)")
                conflict_count = conflict_count + 1
                if e1 not in conflict_employees:
                    conflict_employees.append(e1)

if conflict_count == 0:
    print("No conflicts found.")
else:
    print("\nTotal conflicts:", conflict_count)
    print("Employees with conflicting schedules:", ", ".join(conflict_employees))
