meal_cost = float(input("Enter the cost of the meal: $"))

tax_rate = 0.08

tax_amount = meal_cost * tax_rate
tip_amount = meal_cost * 0.18
total_cost = meal_cost + tax_amount + tip_amount

print("Tax: ${:.2f}".format(tax_amount))
print("Tip: ${:.2f}".format(tip_amount))
print("Grand Total: ${:.2f}".format(total_cost))
