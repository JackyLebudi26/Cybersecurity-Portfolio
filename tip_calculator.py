meal = input("How much was the meal? ")
percent = input("What percentage would you like to tip? ")

meal_amount = float(meal[1:])

tip_percentage = float(percent[:-1]) / 100

tip_amount = meal_amount * tip_percentage

print(f"Leave ${tip_amount:.2f}")

