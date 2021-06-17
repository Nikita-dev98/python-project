#! usr/bin/py

import random
words = [
    "website",
    "hangman",
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "apple",
    "reverse",
    "water",
    "codesnail",
]

word = random.choice(words)
guesses=""
turns=10

while turns>0:
 failed=0
 for i in word:
  if i in guesses:
   print(i, end="")
  else:
   print("_", end="")
   failed+=1

 if failed==0:
  print("\n you win")
  print("the word is:", word)
  break

 guess = input("enter another alphabet")
 guesses+=guess
 if guess not in word:
  turns-=1
  print("you have ",+turns,"more guesses")

  if turns==0:
   print("you lose")

