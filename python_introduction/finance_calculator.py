income = input("Enter your monthly income:")
total_monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = float(income) - float(total_monthly_expenses)


Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(Projected_Savings)}")
