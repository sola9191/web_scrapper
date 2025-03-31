from random import randint
print("welcome to python casino: ")
pc_choice = randint(0, 10)

playing = True

while playing: 
  user_choice=int(input("Choose number."))
  if user_choice == pc_choice:
      print("you won")
      playing = False
  elif user_choice > pc_choice:
      print(f"lower!")
  elif user_choice < pc_choice:
      print(f"higher!")
"""
distance = 0

while distance < 20 :
  print("I'm reunning: ", distance, "km")
  distance +=1"
"""