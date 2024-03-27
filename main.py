import art
import game_data
import random

score = 0
win=True
while win is True:
  print(art.logo)
  if score == 0:
    A=random.choice(game_data.data)
  else:
    A=win_result
  B=random.choice(game_data.data)
  
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(art.vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
  choice=input("Who has more followers?, type 'A' or 'B':")

  if choice.lower() == 'a' and A['follower_count'] > B['follower_count']:
    win_result=A
    score+=1
    print(f"You are right!,current score:{score}")
  elif choice.lower() == 'b' and B['follower_count'] > A['follower_count']:
    win_result=B
    score+=1
    print(f"You are right!,current score:{score}")
  else:
    print(f"Sorry, that's wrong. Final score:{score}")
    win=False
  # print(f"Compare A:random.rand")
  # 'name': 'Instagram',
  # 'follower_count': 346,
  # 'description': 'Social media platform',
  # 'country': 'United States'
  
  