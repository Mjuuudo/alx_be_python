monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = float(monthly_income) - float(monthly_expenses)

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
