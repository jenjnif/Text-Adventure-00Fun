import random
character = ['Wizzeling Wizard', 'Catastrophic Cat', 'Bobbeling Flightless Bumble Bee', 'Outrageous Ground Owl']

def end():
	print('THE END')
	start_again()


def start_again():
	print("Would you like to start again?\n")
	start_yes_no = input('Yes/no?\n')
	if start_yes_no.lower() in ('yes', 'y'):
		start()
	elif start_yes_no.lower() in ('no' or 'n'):
		print("Goodbye")
		quit()
	elif start_yes_no.lower():
		start_again()

# def continue_game():
# 	continue_yes_no = input('Yes/no?')
# 	if continue_yes_no.lower() in ('yes', 'y'):
# 		walk_or_climb()
# 	elif continue_yes_no.lower() in ('no' or 'n'):
# 		print("Goodbye")
# 		quit()
# 	elif continue_yes_no.lower():
# 		start_again()

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


# def owl_job():
# 	print("Would you like to get a job? Yes/no?\n")
# 	job = input('Yes/no?')
# 	if job.lower() in ('yes', 'y'):
# 		print('Congratulations, you got a job as an ice cream taster.')
# 		owl_spend()
# 	elif job.lower() in ('no' or 'n'):
# 		print('You treat your life as one long holiday and get suffocated by a sea cucumber.')
# 		end()
# 	elif job.lower():
# 		owl_job()


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
# 	print("Would you like to ask him to get the octopus?\n")
# 	ask_for_octopus = input('Yes/no?')
# 	if ask_for_octopus.lower() in ('yes', 'y'):
# 		owl_healing()
# 	elif ask_for_octopus.lower() in ('no' or 'n'):
# 		print('Oh no! That was your only chance to get the octopus. You died of sunstroke.')
# 		end()
# 	elif ask_for_octopus.lower():
# 		owl_ask_gull()

# def owl_hide():
# 	hide = input('Do you want to hide?\n')
# 	if hide.lower() in ('yes', 'y'):
# 		print('You stayed hidden for too long and died of starvation.')
# 		end()
# 	elif hide.lower() in ('no' or 'n'):
# 		owl_ask_gull()
# 	elif hide.lower():
# 		owl_hide()


# def owl_sea_gym():
# 	sea_gym = input("Would you like to get some fresh air at the seaside or work your wing at the gym?\n")
# 	sea = "sea"
# 	gym = "gym"
# 	activity_words = sea_gym.lower()
# 	if sea in activity_words:
# 		print('You see a gull. It is Perdue!')
# 		owl_hide()
# 	elif gym in activity_words:
# 		print('Someone is not paying attention to their body. Leg work is not going to help you back up that tree. You die of exhaustion.')
# 		end()
# 	elif sea_gym.lower():
# 		owl_sea_gym()

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
		# owl_sea_gym()
	elif walk in travel_words:
		print("You come across a clearing and in the distance you see a pair of dogs.")
		owl_job()
	elif travel_words.lower():
		# walk_or_climb()


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
		indefiniteArticle = "an"
	else:
		indefiniteArticle = "a"
	print('\nWelcome ' + name + '. You are ' + indefiniteArticle + " " + character_generated + '.\nDo you wish to continue?')
	lost_woods()


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
