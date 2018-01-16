import random
character = ['Wizzeling Wizard', 'Catastrophic Cat', 'Bobbeling Flightless Bumble Bee', 'Outrageous Ground Owl']
stone = {'blue': 'freeze time for 1 hour' , 'red': 'get 1 life', 'pink': 'get food', 'green': 'speak to the trees'}
blue_stone = 0
red_stone = 0
pink_stone = 0
green_stone = 0


def end():
	print('THE END')
	start_again()


def start_again():
	start_yes_no = input('Would you like to start again?\nYes/no?\n')
	if start_yes_no.lower() in ('yes', 'y'):
		start()
	elif start_yes_no.lower() in ('no' or 'n'):
		print("Goodbye")
		quit()
	elif start_yes_no.lower():
		print('I do not understand what you want to do.')
		start_again()

def stay_in_the_tree(stays):
	stay_yes_no = input('Do you still want to stay in the tree?\nYes/no?\n')
	if stay_yes_no.lower() in ('yes', 'y'):
		print('You are going to have to move sometime.')
		print(stays)
		if stays < 3:
			stay_in_the_tree(stays + 1)
		else:
			print('You have run out of time. You will have to sleep out in the dark and hope the Flying Wolves don\'t get you!')
	elif stay_yes_no.lower() in ('no' or 'n'):
		inspect_object()
	elif stay_yes_no.lower():
		print('I do not understand what you want to do.')
		stay_in_the_tree(stays)


# def owl_spend():
# 	home_holiday = input('You have enough money to go home now. Would you like spend the money on an Airber or a trip to Blackpool?\n')
# 	black = "blackpool"
# 	taxi = "airber"
# 	travel_words = home_holiday.lower()
# 	if taxi in travel_words:
# 		print('Yey! You can go home! But wait...oh deary me. You were too late and Walt got your spot. You die of sadness.')
# 		end()
# 	elif black in travel_words:
# 		print("Oh no! The animals have escaped from the zoo. A baboon sat on you and crushed you to death. Guess you should have gone home.")
# 		end()
# 	elif home_holiday.lower():
# 		owl_spend()

# def owl_healing():
# 	banana = input('A banana appears. Should you ask it to heal you?\n')
# 	if banana.lower() in ('yes', 'y'):
# 		print('How did you know it was the octopus in disguise? You are healed and can go save your nest from the pesky Walt.')
# 		print('CONGRATULATIONS')
# 		end()
# 	elif banana.lower() in ('no' or 'n'):
# 		print('The banana turned back into the octopus and laughed as it swam away. You were so distracted that you did not notice the shark. Too late!')
# 		end()
# 	elif banana.lower():
# 		owl_healing()
		
# def owl_ask_gull():
# 	print('Would you like to ask him to get the octopus?\n')
# 	ask_for_octopus = input('Yes/no?')
# 	if ask_for_octopus.lower() in ('yes', 'y'):
# 		owl_healing()
# 	elif ask_for_octopus.lower() in ('no' or 'n'):
# 		print('Oh no! That was your only chance to get the octopus. You died of sunstroke.')
# 		end()
# 	elif ask_for_octopus.lower():
# 		owl_ask_gull()
# print('You saw a large lake from up in the tree. Would you like to head for it or try to go around it?')

def pick_up():
	stone_found = random.choice(list(stone.keys()))
	stone_action = stone.get(stone_found)
	print('You have found a ' + stone_found + ' magic stone! This stone means you can ' + stone_action + '.')
		if stone_found == blue: 
			blue_stones_collected = blue_stone + 1
			print(blue_stones_collected)
		elif stone_found == red: 
			red_stones_collected = red_stone + 1
			print(red_stones_collected)
		elif stone_found == pink: 
			red_stones_collected = red_stone + 1
			print(red_stones_collected)



blue_stone = 0
red_stone = 0
pink_stone = 0
green_stone = 0

	# These could be randomly selected colours and each one could do something different. Need to have a number to collect them.
stone = {'blue': 'freeze time for 1 hour' , 'red': 'get 1 life', 'pink': 'get food', 'green': 'speak to the trees'}

def inspect_object():
	walk_to_object = input('When you get down from the tree you see a something shiny a few metres away.\nWould you like to go over to the object?\nYes/no?\n')
	if walk_to_object.lower() in ('yes', 'y'):
		pick_up()
	elif walk_to_object.lower() in ('no' or 'n'):
		print('Oh no! That was your only chance to get the octopus. You died of sunstroke.')
	elif walk_to_object.lower():
		print('poo')
		# owl_ask_gull()

def tree_view():
	down_stay = input('You can see your home over in the distance and the nice, safe, winding path you took to get you here ' +
		'but you will never get back if go the long way round. You are going to have to go through the deep forest past ' +
		'many obstacles to get back. Type 1 to climb down or 2 to stay in the tree.\n')
	climb_down = "1"
	stay = "2"
	activity_words = down_stay.lower()
	if climb_down in activity_words:
		inspect_object()
	elif stay in activity_words:
		print('If you stay in the tree too long you will never get home!')
		stay_in_the_tree(1)
	elif down_stay.lower():
		tree_view()

# jen='''

# uyhyrfdte

# nhvdc

# '''

def walk_or_climb():
	climb_walk = input("There are many magic stones in the forest. " +
		"These could be helpful to you if you want to get home quickly but be careful how you use them.\n" +
		" You are surrounded by trees, perhaps you could climb up to get a better view? Type c to climb or w to keep on walking.\n")
	climb = "c"
	walk = "w"
	travel_words = climb_walk.lower()
	if climb in travel_words:
		print("Excellent work. You have a much better view from up here.")
		tree_view()
	elif walk in travel_words:
		print("You come across a clearing and in the distance you see a pair of dogs.")
		# owl_job()
	elif travel_words.lower():
		walk_or_climb()


def lost_woods():
	begin = input("Yes/no?\n")
	if begin.lower() in ('yes', 'y'):
		print("You are lost in the Wild Woods of Woowoowoo. You need to get back to your home before darkness falls.")
		walk_or_climb()
	elif begin.lower() in ('no' or 'n'):
		start_again()
	elif begin.lower():
		start_again()



def start():
	name = input("Welcome to your adventure. Please tell me your name.")
	character_generated = random.choice(character)
	if character_generated == 'Outrageous Owl':
		indefinite_article = "an"
	else:
		indefinite_article = "a"
	print('\nWelcome ' + name + '. You are ' + indefinite_article + " " + character_generated + '.\nDo you wish to continue?')
	lost_woods()


if __name__ == "__main__":
    start()


#
# while True:
# 	cat = input("Which cat do you want to be?")
# 	if cat == 'Ralph':
# 		print("You are Ralph")
# 		break
	
# print("You are in a room with two doors, which door to take?")
# door = input("Left or Right?")

# if door.lower() == "left":
# 	print("You are in a wide chamber")
# elif door.lower() == "right":
# 	print("You are at a dark stairway")


# def myFunction(arg1, arg2):
# 	print ("hello ", arg1, " - ", arg2) 
