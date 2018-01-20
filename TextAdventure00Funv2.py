
def process_input_for_woods(user_input):
	if user_input.lower() == "left":
		print("You chose to go left...")
		return 1
	elif user_input.lower() == "right":
		print("You chose to go right...")
		return 2
	else:
		print("Invalid input")
		return None

def process_input_for_building(user_input):
	if user_input.lower() == "yes":
		return 2
	elif user_input.lower() == "no":
		print("OK... stay here")
		return None
	else:
		print("Invalid input")
		return None

def process_input_for_school(user_input):
	if user_input.lower() == "yes":
		print("GAME OVER... stay in school kids")
		exit()
	elif user_input.lower() == "no":
		print("You win at life")
		exit()
	else:
		print("Invalid input")
		return None



scenes = [{
	"instructions": "You are in a woods",
	"input_text": "Do you want to go right or left?",
	"process": process_input_for_woods
},{
	"instructions": "You are in a building",
	"input_text": "Do you want to open the door?",
	"process": process_input_for_building
},{
	"instructions": "You are in a school",
	"input_text": "Do you want to leave?",
	"process": process_input_for_school

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