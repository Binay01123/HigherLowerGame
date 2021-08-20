import art
import random
from game_data import data
from replit import clear
answer = True
score = 0 

def random_people():
  random_index = random.randint(0,len(data)-1)
  random_name = data[random_index]["name"]
  random_detail = data[random_index]["description"]
  random_location = data[random_index]["country"]
  random_people.A = data[random_index]["follower_count"]
  print(f"Compare A: {random_name}, a {random_detail}, from {random_location}")

def random_people2():
  random_index = random.randint(0,len(data)-1)
  random_name = data[random_index]["name"]
  random_detail = data[random_index]["description"]
  random_location = data[random_index]["country"]
  random_people2.B = data[random_index]["follower_count"]
  print(f"Compare B: {random_name}, a {random_detail}, from {random_location}")


def analysis():
  global score
  global answer
  if score > 0 and answer is True:
    print(f"You are Right !! Your score is {score}")
  elif score >=0 and answer is False:
    print(f" Sorry that's incorrect ! your score is {score}")
  

while answer is True:
  clear()
  print(art.logo)

  analysis()
  random_people()
  A = random_people.A

  print(art.vs)

  random_people2()
  B = random_people2.B

  print(A)
  print(B)
  print(score)

  user_answer = input("Who has more follower? : 'A' or 'B'?  ").lower()

  if user_answer =='a':
    user_answer = A
    if A > B:
      score += 1 
    else:
      answer = False
  elif user_answer =='b':
    user_answer = B
    if B > A:
      score += 1
    else:
      answer = False
  

clear()
print(art.logo)
analysis()  


