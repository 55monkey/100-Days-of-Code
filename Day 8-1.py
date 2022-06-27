# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple function
def greet():
  print("Hello")
  print("This is greeting")
  print("Nice weather")
greet()

#Function that allows for input
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"This is greeting {name}")
greet_with_name("Tanya")

#Function with more than 1 input
def greet_with_name(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
greet_with_name("Tanya", "London")

#Key word parameters
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
greet_with(location = "London", name = "Tanya")