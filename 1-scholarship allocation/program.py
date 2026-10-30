# ============================================================
# Case Study 2: Smart Parking Fee Management
# Uses: strings, validation, lists, loops, conditions
# ============================================================

# Parallel lists: index 0 = BIKE, 1 = CAR, 2 = TRUCK
types = ["BIKE", "CAR", "TRUCK"]
rate_per_hour = [10, 20, 40]     # Rs. per hour (part hour counts as full hour)
daily_cap = [80, 150, 300]       # maximum charge for one 24-hour block
OVERNIGHT_FEE = 50               # Rs. for every midnight crossed
PENALTY_LIMIT = 48 * 60          # minutes; staying longer than 48 hours is penalised
PENALTY = 200                    # Rs.

again = "y"
while again == "y":
    print("\n--- New Parking Ticket ---")
    valid = True
    vehicle = input("Vehicle type (BIKE/CAR/TRUCK): ").strip().upper()
    if vehicle not in types:
        print("ERROR: unknown vehicle type.")
        valid = False

    minutes_of_day = []              # will hold entry and exit time in minutes
    if valid:
        for label in ["entry", "exit"]:
            t = input("Enter " + label + " time (HH:MM, 24-hour): ").strip()
            # Validate the format character by character
            if len(t) == 5 and t[2] == ":" and t[0:2].isdigit() and t[3:5].isdigit():
                hh = int(t[0:2])
                mm = int(t[3:5])
                if hh <= 23 and mm <= 59:
                    minutes_of_day.append(hh * 60 + mm)
                else:
                    print("ERROR: hour must be 0-23 and minute 0-59.")
                    valid = False
                    break
            else:
                print("ERROR: time must look like 09:30.")
                valid = False
                break

    nights = 0
    if valid:
        n_text = input("Midnights crossed (0 = same date, 1 = exit next day...): ").strip()
        if n_text.isdigit():
            nights = int(n_text)
        else:
            print("ERROR: midnights must be a whole number.")
            valid = False

    if valid:
        total_minutes = nights * 1440 + minutes_of_day[1] - minutes_of_day[0]
        if total_minutes <= 0:
            print("ERROR: exit time must be after entry time.")
            valid = False

    if valid:
        k = types.index(vehicle)
        full_days = total_minutes // 1440           # complete 24-hour blocks
        left_over = total_minutes % 1440            # minutes in last partial block
        hours = left_over // 60
        if left_over % 60 > 0:
            hours = hours + 1                       # round part hour UP
        last_block = hours * rate_per_hour[k]
        if last_block > daily_cap[k]:
            last_block = daily_cap[k]               # apply daily cap
        parking = full_days * daily_cap[k] + last_block
        overnight = nights * OVERNIGHT_FEE
        penalty = 0
        if total_minutes > PENALTY_LIMIT:
            penalty = PENALTY
        total = parking + overnight + penalty

        print("\n----- PARKING BILL -----")
        print("Vehicle        :", vehicle)
        print("Duration       :", total_minutes // 60, "h", total_minutes % 60, "min")
        print("Parking charge : Rs.", parking)
        print("Overnight fee  : Rs.", overnight)
        print("Penalty        : Rs.", penalty)
        print("TOTAL          : Rs.", total)

    again = input("\nAnother ticket? (y/n): ").strip().lower()
print("Thank you!")
