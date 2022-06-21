#Conditions
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry youare unable to ride the rollercoaster")


#Nesteed Conditions
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry youare unable to ride the rollercoaster")


#Exercise Odd and Even Numbers
number = int(input("Which number do you want to check? "))

#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder)
else:
  print("This is an odd number.")
