import time

ans_A = ["A","a"]
ans_B = ["B","b"]
ans_C = ["C","c"]
yes = ["Y","y","yes"]
no = ["N","n","no"]

#objects that can be taken
sword = 0
food = 0

required = ("\n use only A,B,C \n")

#story section wise starting with intro
def intro():
	print ("After a night out with friends, you awaken the "
  "next morning in a thick, dank forest. Head spinning and " 
  "fighting the urge to vomit, you stand and look around. The peace quickly fades when you hear a "
  "grotesque sound emitting behind you. A slobbering lion is "
  "running towards you. You will:")
	time.sleep(1)
	print("""A:pick a rock and throw it at the lion
	B:run
	C: lie down and get killed""")
	choice = input(">>> ") #1st choice
	if choice in ans_A:
		option_rock()
	elif choice in ans_B:
		option_run()
	elif choice in ans_C:
		print("you died")
	else:
		print(required)
		intro()

def option_rock():
	print("the lion got hit in the nose and roared in pain. he starts charging towards you again. Will you:")
	time.sleep(1)
	print("""A:run
	B:throw another rock
	C: run to a nearby house """)
	choice = input(">>> ") 
	if choice in ans_A:
		option_run()
	elif choice in ans_B:
		print("it missed the lion this time. you died")
	elif choice in ans_C:
		option_house()
	else:
		print(required)
		option_rock()

def option_house():
	print("before entering the house, you see a sword. do you pick it up. Y/N?")
	choice = input(">>> ")
	if choice in yes:
		sword =1
	else:
		sword = 0
	print("what next")
	time.sleep(1)
	print("""A:fight B:run""")
	choice = input(">>> ")
	if choice in ans_A:
		if sword >0:
			print("you fought the lion and killed it. you survived")
		else:
			print("you should have picked up the sword. you died")
	elif choice in ans_B:
		print("you silenetly get out of the house through the back and run")
		option_run()
	else:
		print(required)
		option_house()

def option_run():
	print("you run but the lion has cornered you now. you have to:")
	time.sleep(1)
	print("""A:hide B:pck up food C:fight""")
	choice = input(">>> ")
	if choice in ans_A:
		print("the lion found you and killed you")
	elif choice in ans_B:
		food = 1
		if food == 1:
			print("you gave it to the lion and you survived")
		else:
			print("you should have picked up the food. you died")
	elif choice in ans_C:
		if sword == 1:
			print("you fought the lion and killed it. you survived")
		else:
			print("you should have picked up the sword. you died")

intro()