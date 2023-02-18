days_of_plunder = int(input())
daily_plunder = int(input())
target_plunder = float(input())

total_plunder = 0

for each_day in range(1, days_of_plunder + 1):
    total_plunder += daily_plunder
    if each_day % 3 == 0:
        total_plunder += daily_plunder * 0.50

    if each_day % 5 == 0:
        total_plunder -= total_plunder * 0.30

if total_plunder >= target_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")

else:
    print(f"Collected only {(total_plunder / target_plunder) * 100:.2f}% of the plunder.")
