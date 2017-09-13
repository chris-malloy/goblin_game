# 1. Include pygame
# Include pygame which we got from pip
import pygame

# from the math module (built into python), gets the fabs method, this will be used later to 
# help with telling python the distance between objects
from math import fabs, hypot
from random import randint 

# to allow for random movement of npc objects
import random

# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play()

# 3. Create a screen with a particular size
# the screen size MUST be a tuple (can't change)
screen_size = (512,480)

# actually tell pygame to set the screen up and store it
# call set_mode against the disply method of the pygame method with the value store inside screen_size
pygame_screen = pygame.display.set_mode(screen_size)

# set game caption
pygame.display.set_caption("Goblin Chase")

# set up a var with our image
background_image = pygame.image.load("background.png")
hero_image = pygame.image.load("hero.png")
goblin_image = pygame.image.load("goblin.png")
monster_image = pygame.image.load("monster.png")
coin_image = pygame.image.load("coin.png")
coin_image_small = pygame.transform.scale(coin_image, (40, 40))

# init sound playback
pygame.mixer.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play()
# pygame.mixer.init(frequency = 440, size =- 16, channels = 2, buffer = 4096)
# does_pymusic_work = pygame.mixer.get_init()
# print does_pymusic_work

# goblin_music = pygame.mixer.Sound("music.wav")
# goblin_music.play(loops = -1)

# load a sound file
# goblin_music = pygame.mixer.music(music.wav)	


# 8. Set up the object locations
hero = {
	"x": 100,
	"y": 100,
	"speed": 3,
	"health": 200,
	"wins": 0,
	"losses": 0

}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 5,
	"health": 300,
	"dx": 1,
	"dy": 1
}

monster = {
	"x": 300,
	"y": 300,
	"speed": 2,
	"health": 200,
	"dx": 1,
	"dy": 1

}

coin = {
	"x": 400,
	"y": 400,
	"speed": 5
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

# 4. Create a loop (while)

# Create a boolean for whether a game should be running or not.
game_on = True
hero_alive = True
tick = 0
while game_on:
	tick += 1
	print tick
	# we are inside the main game loop.
	# is will keep running, as long as our bool is true

	# 5. Add a quit event (Python needs a n escape)
	# Pygame comes with an event loop! (sort of like JS)

	# this for loop sets all possible game conditions
	for event in pygame.event.get():
		# quit event
		if (event.type == pygame.QUIT):
			# the user clicked the red x in the top left
			game_on = False

		# tells python to listen for a key pushed down and set key_down value to True 
		# for each coresponding key
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			# tell pygame up key (273)
			if event.key == keys['up']:
				# user pressed up!!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys['down']:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys['left']:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			elif event.key == keys['right']:
				# hero['x'] += hero['speed']
				keys_down['right'] = True

		# tells pythong to listen for a key to be released and set key_down value to False
		# for each coresponding key
		elif event.type == pygame.KEYUP:
			# the user let go of a key. See if it's one that matters
			if event.key == keys['up']:
				# user let go of the upkey. Flip the bool
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	# tells python how much to iterate 2 dimensional movement for respective key and direction of movement		
	# # adjusting speed is as easy as adjusting the key value in the respective character dictionary	
	if keys_down['up']:
		if hero['y'] > 0:
			hero['y'] -= hero['speed']
	elif keys_down['down']:
		if hero['y'] < (480 - 32):
			hero['y'] += hero['speed']
	if keys_down['left']:
		if hero['x'] > 0:
			hero['x'] -= hero['speed']
	elif keys_down['right']:
		if hero['x'] < (512-64):
			hero['x'] += hero['speed']

	# one movement option
	# random movement
	# goblin_dx = goblin['x'] - hero['x']
	# goblin_dy = goblin['y'] - hero['y']
	monster_dx = monster['x'] - hero['x']
	monster_dy = monster['y'] - hero['y']
	 
	# goblin_dist = hypot(goblin_dx,goblin_dy)
	monster_dist = hypot(monster_dx, monster_dy)
	# print dist
	# goblin_dx = goblin_dx / goblin_dist
	# goblin_dy = goblin_dy / goblin_dist
	monster_dx = monster_dx / monster_dist
	monster_dy = monster_dy / monster_dist
	# print dx, dy
	# goblin['x'] += goblin_dx * goblin['speed']
	# goblin['y'] += goblin_dy * goblin['speed']
	monster['x'] -= monster_dx * monster['speed']
	monster['y'] -= monster_dy * monster['speed']

	if tick % 1 == 0:
	# change directions!
		goblin['dx'] = randint(-1,1)
		goblin['dy'] = randint(-1,1)
		goblin['x'] += goblin['dx'] * goblin['speed']
		goblin['y'] += goblin['dy'] * goblin['speed']

	# monster['x'] += monster['dx'] * monster['speed']
	# monster['y'] += monster['dy'] * monster['speed']

	# another movement option
	# ultimately this code does not work.  Using the hypotenuse is much better
	# trying a new movement method for monster
	# this works for correcting when x,y values are > but not for <.  google for help
	# if (monster['x'] != hero['x']): 
	# 	if monster['x'] > hero['x']:
	# 		monster['x'] -= monster['speed']
	# 	elif monster['x'] < hero['x']:
	# 		monster['x'] += monster['speed']
	# 	else:
	# 		continue
	# if (monster['y'] != hero['y']):
	# 	if monster['y'] > hero['y']:
	# 		monster['y'] -= monster['speed']
	# 	elif monster['y'] < hero['y']:
	# 		monster['x'] += monster['speed']
	# 	else: 
	# 		continue




	# COLLISION DETECTION!!!
	# fabs - function absolute value.  we need this because of left and down movements are negative values
	# we can use this to generate a win or lose condition, and add interations between objects

	# adding win condition - hero attacked goblin
	distance_to_goblin = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_to_goblin < 32:
		# the hero and goblin are touching!
		# this is our win condition
		# print "collision!"
		# hero['wins'] += 1
		if goblin['health'] > 0:
			goblin['health'] -= 1
		else:
			continue
		if goblin['health'] == 0:
			won_game = font.render("You Win!", True, (0,0,0))
			pygame_screen.blit(won_game, [256,240])
			hero['wins'] += 1
		# else: 
		# print "not touching"

	# add collision to monster.  if monster touches hero, hero looses health	
	distance_to_monster = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if distance_to_monster < 32:
		if hero['health'] > 0:
			hero['health'] -= 1
		else:
			continue
		if hero['health'] == 0:
			lose_game = font.render("Too bad, you lose.", True, (0,0,0))
			pygame_screen.blit(lose_game, [256,240])
			hero['losses'] += 1
			
	# add coin speed key to hero speed key if coin does not exist
	# come back later to set coin_exist to false instead moving coin offscreen
	distance_to_coin = fabs(hero['x'] - coin['x']) + fabs(hero['y'] - coin['y'])
	if distance_to_coin < 28:
		hero['speed'] += coin['speed']
		coin['x'] = 1000
		coin['y'] = 1000 

	# create win condition






	# 6. Fill in the screen with images to create backgrounds, characters, items,
	# projectiles, ect.

	# use blit to set iomage - it takes 2 arguments...
	# 1. What do you wan to draw?
	# 2. Where do you want to draw it?
	# background image to add
	pygame_screen.blit(background_image, [0,0])

	# Make a font so we can write on the screen
	# will use default font from host machine
	font = pygame.font.Font(None, 25)

	# display wins
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	# display losses
	lose_text = font.render("Losses: %d" % (hero['losses']), True, (0,0,0))
	pygame_screen.blit(lose_text, [380,40])

	# display hero health
	# change hero health color to yellow if he has coin later
	hero_health = font.render("Hero Health: %d" % (hero['health']), True, (0,0,0))
	pygame_screen.blit(hero_health, [40,55])

	#display goblin health
	goblin_health = font.render("Goblin Health: %d" % (goblin['health']), True, (0,0,0))
	pygame_screen.blit(goblin_health, [40,70])

	# display monster health
	monster_health = font.render("Monster Health: %d" % (monster['health']), True, (0,0,0))
	pygame_screen.blit(monster_health, [40, 85])

	# character locations have to in brackets in brackets 
	# the syntax is - location.blit(thing to add, thing to add[x key], thing to add[y key])

	# display hero
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])
	# display goblin
	pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])
	# display monster
	pygame_screen.blit(monster_image, [monster['x'], monster['y']])
	# display coin
	pygame_screen.blit(coin_image_small, [coin['x'], coin['y']])

	# 7. Repeat 6 over and over over...

	# 8. add the flip method, which will allow the host machine to continuely
	# ask for loctions of specified objects and display them.
	# locations will be updated each time the screen refreshes
	pygame.display.flip()



















