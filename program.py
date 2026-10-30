# ============================================================
# Case Study 10: Disaster Relief Supply Allocation
# Uses: lists, nested lists, tuples, unpacking, sorting, loops
# ============================================================

items = ["Food kits", "Water cans", "Medicine kits"]
stock = [500, 400, 200]                 # available stock of each item

# area tuple: (name, population, urgency)   urgency 1 = most urgent, 3 = least
areas = [
    ("Riverside",    1200, 1),
    ("Hilltop",       800, 2),
    ("Coastal Town", 2000, 1),
    ("Old Market",    500, 3),
]
# nested list: demand[i][j] = units of item j required by area i
demand = [
    [300, 250, 120],
    [200, 150,  60],
    [400, 300, 100],
    [150, 100,  40],
]

# ---- Priority order: lower urgency number first; larger population breaks ties ----
order = list(range(len(areas)))
for i in range(len(order) - 1):
    for j in range(len(order) - 1 - i):
        name1, pop1, urg1 = areas[order[j]]
        name2, pop2, urg2 = areas[order[j + 1]]
        swap = False
        if urg2 < urg1:
            swap = True
        elif urg2 == urg1 and pop2 > pop1:
            swap = True
        if swap:
            order[j], order[j + 1] = order[j + 1], order[j]

# ---- Allocation (policy: serve areas in priority order; give what is available) ----
allocation = []
for i in range(len(areas)):
    allocation.append([0, 0, 0])
remaining = stock[:]                    # copy of the stock list

for idx in order:
    for j in range(len(items)):
        need = demand[idx][j]
        if remaining[j] >= need:
            give = need
        else:
            give = remaining[j]         # only what is left
        allocation[idx][j] = give
        remaining[j] = remaining[j] - give

# ---- Report ----
print("PRIORITY ORDER:")
position = 1
for idx in order:
    name, pop, urg = areas[idx]
    print(" ", position, name, "(urgency " + str(urg) + ", population " + str(pop) + ")")
    position = position + 1

print("\nALLOCATION (given / demanded):")
total_unmet = 0
for idx in order:
    name = areas[idx][0]
    line = name.ljust(13)
    for j in range(len(items)):
        line = line + items[j] + " " + str(allocation[idx][j]) + "/" + str(demand[idx][j]) + "  "
        total_unmet = total_unmet + (demand[idx][j] - allocation[idx][j])
    print(line)

print("\nUNMET DEMAND BY AREA:")
for idx in order:
    name = areas[idx][0]
    parts = []
    for j in range(len(items)):
        short = demand[idx][j] - allocation[idx][j]
        if short > 0:
            parts.append(items[j] + ": " + str(short))
    if len(parts) == 0:
        print(" ", name, "- fully served")
    else:
        print(" ", name, "-", ", ".join(parts))

print("\nREMAINING STOCK:")
for j in range(len(items)):
    print(" ", items[j], "=", remaining[j])
print("Total unmet units:", total_unmet)
