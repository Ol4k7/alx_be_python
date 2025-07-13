# Prompt for user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Use the exact formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Print the results
print("Your monthly savings are ${:.0f}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${:.0f}.".format(projected_savings))
