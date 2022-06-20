# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

# Rounding
print(round(8 /3, 2))

# without converting to int double // - intiger, single / - float
print(8 // 3)

#combning to a string (f-String)
score = 0
height = 1.5
iswinning = True
print(f"Your score is {score}, Your height is {height}, You are winning is {iswinning}")