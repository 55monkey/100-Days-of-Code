import random

randomIntegeter = random.randint(1, 10)

print(randomIntegeter)

randomFloat = random.random() * 5

print(randomFloat)

love_score = random.randint(1, 100)

print(f"You love score is {love_score}.")


import random
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


#Lists
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California"]
print(states_of_america[0])

#adding new
states_of_america.append("NewState")
print(states_of_america)