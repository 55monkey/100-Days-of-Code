#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

#calculating the average student height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])



total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

number_students = 0
for student in student_heights:
  number_students += 1
print(number_students)

avarage_height = round(total_height / number_students)

print(avarage_height)

#Calculating the highest score from a List of scores

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")

