while True:
	name = input("Welcome to your cat text adventure. Please choose your cat name.")
	print("Hi " + name)

while True:
	cat = input("Which cat do you want to be?")
	if cat == 'Ralph':
		print("You are Ralph")
		break
	
print("You are in a room with two doors, which door to take?")
door = input("Left or Right?")

if door.lower() == "left":
	print("You are in a wide chamber")
elif door.lower() == "right":
	print("You are at a dark stairway")


def myFunction(arg1, arg2):
	print ("hello ", arg1, " - ", arg2) 