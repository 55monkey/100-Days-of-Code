#For loop with range

total = 0
for number in range(2, 101, 2):
  total += number
print(total)

#or

total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)

#FizzBuzz game

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    elif number % 3 == 0:
      print("Fizz")
    elif number % 5 == 0:
      print("Buzz")
    else:
      print(number)