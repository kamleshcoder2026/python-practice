# Simple BMI Calculator

# 1. Ask the user for their weight and height
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# 2. Convert height from cm to meters (1 meter = 100 cm)
height_m = height_cm / 100

# 3. Calculate the BMI score using the formula: weight / (height * height)
bmi = weight / (height_m * height_m)

# 4. Round the BMI to 2 decimal places to make it look clean
bmi = round(bmi, 2)

# 5. Show the BMI to the user
print("------------------------------")
print("Your BMI is:", bmi)

# 6. Check if the person is healthy or unhealthy based on the BMI score
if bmi < 18.5:
    print("Status: Underweight (Unhealthy)")
elif bmi <= 24.9:
    print("Status: Healthy weight (Healthy)")
elif bmi <= 29.9:
    print("Status: Overweight (Unhealthy)")
else:
    print("Status: Obese (Unhealthy)")
print("------------------------------")
