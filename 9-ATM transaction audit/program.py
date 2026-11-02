# ============================================================
# Case Study 9: Multi-Stage ATM Transaction Audit
# Uses: tuples, unpacking, lists, loops, conditions
# ============================================================

OPENING_BALANCE = 10000
MIN_BALANCE = 500            # balance must never fall below this
PER_WITHDRAWAL_LIMIT = 5000
DAILY_WITHDRAWAL_LIMIT = 10000
TRANSFER_LIMIT = 20000

# (type, amount, target account)   D = deposit, W = withdraw, T = transfer
transactions = [
    ("D", 5000, ""),
    ("W", 2000, ""),
    ("W", 2000, ""),
    ("W", 2000, ""),          # 3rd identical withdrawal in a row -> suspicious
    ("W", 6000, ""),          # above per-withdrawal limit
    ("T", 3000, "ACC205"),
    ("D", -200, ""),          # invalid amount
    ("W", 5000, ""),          # would exceed daily limit
    ("W", 4000, ""),
    ("T", 1600, "ACC310"),    # would break minimum balance
    ("X", 100, ""),           # unknown type
    ("T", 500, ""),           # missing target account
    ("D", 300, ""),
    ("D", 300, ""),
    ("D", 300, ""),           # 3 identical deposits -> suspicious
]

balance = OPENING_BALANCE
withdrawn_today = 0
accepted = 0
rejected = []                # list of (number, reason) tuples
suspicious = []              # list of transaction numbers
last_key = ("", 0)           # previous (type, amount)
run_length = 0               # how many times in a row the same transaction appeared

print("Opening balance:", balance)
print("No  Type Amount  Status    Balance")

number = 0
for t in transactions:
    number = number + 1
    kind, amount, target = t               # tuple unpacking
    reason = ""

    # ---- validation ----
    if kind != "D" and kind != "W" and kind != "T":
        reason = "unknown transaction type"
    elif amount <= 0:
        reason = "amount must be positive"
    elif kind == "W":
        if amount > PER_WITHDRAWAL_LIMIT:
            reason = "exceeds per-withdrawal limit"
        elif withdrawn_today + amount > DAILY_WITHDRAWAL_LIMIT:
            reason = "exceeds daily withdrawal limit"
        elif balance - amount < MIN_BALANCE:
            reason = "minimum balance would be broken"
    elif kind == "T":
        if target == "":
            reason = "missing target account"
        elif amount > TRANSFER_LIMIT:
            reason = "exceeds transfer limit"
        elif balance - amount < MIN_BALANCE:
            reason = "minimum balance would be broken"

    # ---- apply the transaction ----
    if reason == "":
        if kind == "D":
            balance = balance + amount
        elif kind == "W":
            balance = balance - amount
            withdrawn_today = withdrawn_today + amount
        else:
            balance = balance - amount
        accepted = accepted + 1
        status = "OK"
    else:
        rejected.append((number, reason))
        status = "REJECTED"

    # ---- suspicious repeated pattern (same type+amount 3 times in a row) ----
    if (kind, amount) == last_key:
        run_length = run_length + 1
    else:
        run_length = 1
        last_key = (kind, amount)
    if run_length == 3:
        suspicious.append(number)

    print(str(number).ljust(3), kind.ljust(4), str(amount).ljust(7), status.ljust(9), balance)

# ---- audit summary ----
print("\n===== AUDIT SUMMARY =====")
print("Transactions processed :", len(transactions))
print("Accepted               :", accepted)
print("Rejected               :", len(rejected))
for num, why in rejected:
    print("   #" + str(num), "-", why)
print("Suspicious patterns at :", suspicious if len(suspicious) > 0 else "none")
print("Total withdrawn today  :", withdrawn_today)
print("Final balance          :", balance)
