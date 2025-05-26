import random


prompt = input("Do you want to roll the dice? (Yes/No): ").lower()
choices = ["yes", "no"]


while prompt not in choices:
  print("Invalid choice!!")
  prompt = input("Do you want to roll the dice? (Yes/No): ")

if prompt == "yes":

  while True:

    try:

      no_of_rolls = int(input("How many times do you want to roll the dice? "))
      if no_of_rolls <= 0:
        print("Don't be dumb, input a positive number")
      else:
        break
    except ValueError:
      print("Please input a number")
      


  for i in range(1, no_of_rolls + 1):
      first_value = random.randint(1,6)
      second_value = random.randint(1,6)
      print(f"roll {i}: ({first_value}, {second_value})")
      print(f"You rolled the dice {i} times")


elif prompt == "no":
  print("Okay, but we hope to see you soon")

else:
  print("Please input a valid choice")
