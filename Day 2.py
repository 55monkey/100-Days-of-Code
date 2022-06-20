#Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
#Check the data type of two_digit_number
print(type(two_digit_number))
#Get the first and second digits using subscripting
# then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add two digits together
two_digit_number = first_digit + second_digit
print(two_digit_number)


a = str(123)
print(type(a))

print(str(70)+ str(700))
print(70 + float(3.16))

a = str(123)
print(type(a))

a = 1235
print(type(a))

#String
nam_char = len (input("What is your name?"))
new_num_char = str(nam_char)
print("Your name has" + new_num_char + "characters.")

#Data Types

#String
print("Hello"[3])

print("1234" + "46457")

#Intiger
print(1234 + 464577)
print(2453_73645_8477)

#Floats
3.154

#Boolean
True
False


