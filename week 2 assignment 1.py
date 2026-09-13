weight_lbs=float(input("Enter your weight in pounds (lbs): "))
height_feet = float(input("Enter your height in feet (ft): "))
height_inches = float(input("Enter your height in inches (in): "))
height_inches = height_feet * 12 + height_inches

bmi = (weight_lbs * 703) / (height_inches ** 2)
        
print(f"\nYour calculated BMI is: {round(bmi, 1)}")

print("\nLEGEND for BMI Scale")
print("A BMI of less than 18.5 is underweight")
print("A BMI of Greater than 18.8 and less than 24.9 is normal")
print("A BMI of Greater than 25 and less than 29.9 is overweight")
print("A BMI of Greater than 30 is Obese")