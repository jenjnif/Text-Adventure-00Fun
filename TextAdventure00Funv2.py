import random
character = ['Wizzeling Wizard', 'Catastrophic Cat', 'Bobbeling Flightless Bumble Bee', 'Outrageous Ground Owl']

stone = {'blue': 'freeze time' , 'red': 'get 1 life', 'pink': 'get food', 'green': 'speak to the trees'}
blue_stone = 0
red_stone = 0
pink_stone = 0
green_stone = 0

def process_input_for_name(user_input):
	character_generated = random.choice(character)
	if character_generated == 'Outrageous Owl':
		indefinite_article = "an"
	else:
		indefinite_article = "a"
	print('Welcome ' + user_input + '. You are ' + indefinite_article + " " + character_generated)
	return 1

def process_input_for_climb_walk(user_input):
	if user_input.lower() == "c":
		print("Excellent work. You have a much better view from up here.")
		return 2
	elif user_input.lower() == "w":
		print("You come across a clearing and in the distance you see a pair of dogs.")
		return
	else:
		print("Invalid input")
		return None

def process_input_for_tree_view(user_input):
	if user_input.lower() == "1":
		return 3
	elif user_input.lower() == "2":
		print("OK... stay here")
		return None
	else:
		print("Invalid input")
		return None

def process_input_for_inspect(user_input):
	if user_input.lower() in ("yes", "y"):
		process_input_for_pickup()
	elif user_input.lower() in ("no", "n"):
		print("You win at life")
		exit()
	else:
		print("Invalid input")
		return None

def process_input_for_pickup():
	global blue_stone
	global red_stone
	global pink_stone
	global green_stone
	stone_found = random.choice(list(stone.keys()))
	stone_action = stone.get(stone_found)
	print('You have found a ' + stone_found + ' magic stone! This stone means you can ' + stone_action + '.')
	if stone_found == 'blue':
		blue_stone = blue_stone + 1
		print('Just use the word \'blue\' and everything will freeze around you. Be wise when you use this.')
		# wall_cave()
	elif stone_found == 'red':
		red_stone = red_stone + 1
		print(red_stone)
		print('Just use the word \'red\' if you found yourself on the wrong side of death and you will be revived. You will know when to use this!')
		# wall_cave()
	elif stone_found == 'pink':
		pink_stone = pink_stone + 1
		print(pink_stone)
		print('Just use the word \'pink\' and food will be provided. Be wise when you use this.')
		# wall_cave()
	elif stone_found == 'green':
		green_stone = green_stone + 1
		print(green_stone)
		print('Just use the word \'green\' and the trees will listen. Be careful though, some trees are more helpful than others.')
		# wall_cave()

def process_input_for_gameover(user_input):
	if user_input.lower() in ("yes", "y"):
		print("GAME OVER... stay in school kids")
		exit()
	elif user_input.lower() in ("no", "n"):
		print("You win at life")
		exit()
	else:
		print("Invalid input")
		return None


scenes = [{
	"instructions": "Welcome to your adventure.",
	"input_text": "Please tell me your name.",
	"process": process_input_for_name
},{
	"instructions": "You are lost in the Wild Woods of Woowoowoo.""There are many magic stones in the forest. These could be helpful to you if you want to get home quickly but be careful how you use them.",
	"input_text": "You are surrounded by trees, perhaps you could climb up to get a better view? Type c to climb or w to keep on walking.",
	"process": process_input_for_climb_walk
},{
	"instructions": "You can see your home over in the distance and the nice, safe, winding path you took to get you here " +
		"but you will never get back if go the long way round. You are going to have to go through the deep forest past " +
		"many obstacles to get back.",
	"input_text": "Type 1 to climb down or 2 to stay in the tree.",
	"process": process_input_for_tree_view
},{
	"instructions": "When you get down from the tree you see a something shiny a few metres away.",
	"input_text": "Would you like to go over to the object? Yes/no?",
	"process": process_input_for_inspect
}]



def play_game():
	current_scene_index = 0
	while True:
		the_scene = scenes[current_scene_index]
		print_instruction(the_scene)
		the_input = get_input(the_scene)
		next_scene_index = process_input(the_scene, the_input)
		if next_scene_index is not None:
			current_scene_index = next_scene_index

def print_instruction(scene):
	print(scene["instructions"])

def get_input(scene):
	return input(scene["input_text"])

def process_input(scene, the_input):
	process_function = scene["process"]
	return process_function(the_input)

if __name__ == "__main__":
	play_game()