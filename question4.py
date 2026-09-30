#Monthly Allowance & Savings Planner

monthly_pocket_money = float(input("monthly pocket money:"))
canteen = float(input("canteen fee:"))
transport = float(input("transport fee:"))
shopping = float(input("shopping:"))
savings = monthly_pocket_money - (canteen + transport + shopping)
is_budget_safe = savings >= 0

print("Remaining savings:", savings)
print("Is budget safe:", is_budget_safe)
