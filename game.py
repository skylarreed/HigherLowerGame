from game_data import data
from art import logo, vs
import random
import os
winning = True
play = True
person1 = {}
person2 = {}
def rand_person():
  return data[random.randint(0,49)]
def person_infoA():
  print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
def person_infoB():
  print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
print(logo)
def higher_follower():
  if person1['follower_count'] > person2['follower_count']:
    return "a"
  else:
    return "b"
while play == True:
  winning = True
  score = 0
  while winning == True:
    person1 = rand_person()
    person2 = rand_person()
    guess = ''
    if person1 == person2:
      person2 = rand_person()
    person_infoA()
    print(vs)
    person_infoB()
    guess = input("\nWhich has more followers?: ('a' or 'b'): ")
    if guess == 'a':
      if higher_follower() == 'a':
        print("\nThat is correct you earned 1 point towards your score!")
        score += 1
      else:
        print(f"\nGood try, your final score was {score}")
        winning = False
        if input("\nWould you like to play again? Type ('y' or 'n'): ") == 'n':
          play = False
    if guess == 'b':
      if higher_follower() == 'b':
        print("\nThat is correct you earned 1 point towards your score!")
        score += 1
      else:
        print(f"\nGood try, your final score was {score}")
        winning = False
        if input("\nWould you like to play again? Type ('y' or 'n'): ") == 'n':
          play = False
    os.system('clear')
