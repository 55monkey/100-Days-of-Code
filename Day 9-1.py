programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
#create an empty dictionary
empty_dictionary = {}
#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in a computer"

#loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# nesting
  capitals = {
    "France": "Paris",
    "Germany": "Berlin",
  }

# nesting a list in a dictionary
  travel_log = {
    {"France": "cities_vizited": ["Paris", "Lille", "Dijon"], "total_vizits": 12}
  }

# nesting  a dictionary in a list
  travel_log = [
    {
      "country": "France": "cities_vizited": ["Paris", "Lille", "Dijon"], "total_vizits": 12
  },
  {
    "country": "Germany": "cities_vizited": ["Berlin", "Munchen", "Berg"], "total_vizits": 12
  },
  ]
