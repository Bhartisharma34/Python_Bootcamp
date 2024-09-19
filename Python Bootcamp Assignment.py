# 1. Find the Age in year using python when birth year given.

from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
print(f"Your age is: {calculate_age(birth_year)}")


# 2. ⁠Create BMI calculator in python.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

# 3. ⁠Create Currency Convertor in python.

def currency_converter(amount, rate):
    return amount * rate

print("Currency Converter")

amount = float(input("Enter the amount in USD: "))
conversion_rate = float(input("Enter the conversion rate to the desired currency: "))

converted_amount = currency_converter(amount, conversion_rate)
print(f"The converted amount is: {converted_amount:.2f}")
