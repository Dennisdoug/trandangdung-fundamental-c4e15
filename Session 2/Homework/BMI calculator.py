x = int(input("Enter your weight in kg: "))
y = int(input("Enter your height in cm: "))
n = x * 10000 / (y ** 2)
print("Your BMI result is: ", n)
if n < 16:
   print("Severly Underweight")
elif n < 18.5:
   print("Underweight")
elif n < 25:
   print("Normal")
elif n < 30:
   print("Overweight")
else:
   print("Obese")
