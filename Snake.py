import pygame
import time
import sys
import random

pygame.init()
screen = pygame.display.set_mode((499,520))

def draw_rectangle(surf, x, y, color):
	pygame.draw.rect(screen, color, (x*5, y*5, 4, 4))
	
for x in range(100):
	for y in range(100):
		draw_rectangle(screen, x, y, (128, 128, 128))
snake_x = 50
snake_y = 50
draw_rectangle(screen, snake_x, snake_y, (0, 255, 0))

pygame.display.flip()

clock = pygame.time.Clock()
snake_x_diff = 0
snake_y_diff = -1
squares = []
start = True
up = True
down = False
left = False
right = False
tail = 20
snake_color = 0
blue = True
blue_array_x = []
blue_array_y = []
blue_count = 0
purple = False
purple_array_x = []
purple_array_y = []
purple_count = 0
enemy = False
enemy_array_x = []
enemy_array_y = []
enemy_x_amount = 0
enemy_y_amount = 0
enemy_up = True
enemy_down = False
enemy_right = False
enemy_left = False
enemy_count = 0
enemy_head = 0
score = 0
lose = False
game_spd = 20
myfont = pygame.font.SysFont("Comic Sans MS", 15)
score_text = myfont.render("Score:", 1, (255, 255, 255))
screen.blit(score_text, (0, 499))

lose_font = pygame.font.SysFont("Comic Sans MS", 50)

#MAIN LOOP
while True:
	clock.tick(game_spd)
	snake_y += snake_y_diff
	if snake_y < 0:
		lose = True
	if snake_y > 99:
		lose = True
	snake_x += snake_x_diff
	if snake_x < 0:
		lose = True
	if snake_x > 99:
		lose = True
	
	if start == True:
		score_add = myfont.render(str(score), 1, (255, 255, 255))
		screen.blit(score_add, (50, 499))
		
#BLUE SQUARES		
	while blue_count < 5:
		if blue == True:
			blue_y = random.randrange(0,99)
			blue_x = random.randrange(0,99)
			blue_array_y.append(blue_y)
			blue_array_x.append(blue_x)
			blue_count += 1
			draw_rectangle(screen, blue_x, blue_y, (0, 0, 255))
	else:		
		blue == False
		
		if snake_x in blue_array_x:
			if snake_y in blue_array_y:
				game_spd += 2
				score += 1
				snake_color += 10
				tail += 4
				blue_count -= 1
				screen.fill(pygame.Color("black"), (50, 499, 110, 40))
				score_add = myfont.render(str(score), 1, (255, 255, 255))
				screen.blit(score_add, (50, 499))
				blue_array_x.remove(snake_x)
				blue_array_y.remove(snake_y)
				blue = True
	
#PURPLE SQUARES
	if score > 4:
		purple = True

	while purple_count < 3:
		if purple == True:
			purple_y = random.randrange(0,99)
			purple_array_y.append(purple_y)
			purple_x = random.randrange(0,99)
			purple_array_x.append(purple_x)
			purple_count += 1
			draw_rectangle(screen, purple_x, purple_y, (95, 0, 149))
		else:
			break
	else:
		purple = False
	
		if snake_x in purple_array_x:
			if snake_y in purple_array_y:
				game_spd += 4
				score += 3
				snake_color += 30
				tail += 4
				purple_count -= 1
				screen.fill(pygame.Color("black"), (50, 499, 110, 40))
				score_add = myfont.render(str(score), 1, (255, 255, 255))
				screen.blit(score_add, (50, 499))
				purple_array_x.remove(snake_x)
				purple_array_y.remove(snake_y)
				purple = True

#ENEMY SQUARES
	if score > 0:
		enemy = True
		
	while enemy_count == 0:
		if enemy == True:
			enemy_y = random.randrange(0,99)
			enemy_array_y.append(enemy_y)
			enemy_x = random.randrange(0,99)
			enemy_array_x.append(enemy_x)
			enemy_count += 1
			draw_rectangle(screen, enemy_x, enemy_y, (255, 0, 0))
		else:
			break
	else:	
		if snake_x in enemy_array_x and snake_y in enemy_array_y:
			lose = True
			
#ENEMY MOVEMENT
	if enemy_count == 1:
		if enemy_up == True:
			if enemy_y_amount == -3:
				enemy_up = False
				enemy_right = True
			else:
				enemy_array_x.append(enemy_x)
				enemy_array_y.append(enemy_y)
				enemy_y -= 1
				enemy_y_amount -= 1
				draw_rectangle(screen, enemy_x, enemy_y, (255, 0, 0))
				enemy_head += 1
				
		elif enemy_right == True:
			if enemy_x_amount == 3:
				enemy_right = False
				enemy_down = True
			else:
				enemy_array_x.append(enemy_x)
				enemy_array_y.append(enemy_y)
				enemy_x += 1
				enemy_x_amount += 1
				draw_rectangle(screen, enemy_x, enemy_y, (255, 0, 0))
				enemy_head += 1
				
		elif enemy_down == True:
			if enemy_y_amount == 0:
				enemy_down = False
				enemy_left = True
			else:
				enemy_array_x.append(enemy_x)
				enemy_array_y.append(enemy_y)
				enemy_y += 1
				enemy_y_amount += 1
				draw_rectangle(screen, enemy_x, enemy_y, (255, 0, 0))
				enemy_head += 1
				
		elif enemy_left == True:
			if enemy_x_amount == 0:
				enemy_left = False
				enemy_up = True
			else:
				enemy_array_x.append(enemy_x)
				enemy_array_y.append(enemy_y)
				enemy_x -= 1
				enemy_x_amount -= 1
				draw_rectangle(screen, enemy_x, enemy_y, (255, 0, 0))
				enemy_head += 1
				
		if enemy_head == 4:
			draw_rectangle(screen, enemy_array_x[0], enemy_array_y[0], (125, 125, 125))
			enemy_head = 3
			del enemy_array_x[:1]
			del enemy_array_y[:1]
			print (enemy_array_x)
			print (enemy_array_y)
		
#LOSE
	if lose == True:
		for x in range(100):
			for y in range(100):
				draw_rectangle(screen, x, y, (255, 0, 0))
		screen.fill(pygame.Color("black"), (0, 499, 200, 40))
		lose_text = lose_font.render('YOU LOSE', 1, (0, 0, 0))
		screen.blit(lose_text, (120, 100))
		score_final = lose_font.render('FINAL SCORE: ' + str(score), 1, (255, 255, 255))
		screen.blit(score_final, (50, 200))
		
#SNAKE
	if snake_color > 255:
		snake_color = 255
		
	if lose == False:
		draw_rectangle(screen, snake_x, snake_y, (0, 255, snake_color))
		squares.append(snake_x)
		squares.append(snake_y)
	
	if len(squares) > tail:
			draw_rectangle(screen, squares[0], squares[1], (128, 128, 128))
			squares.pop(0)
			squares.pop(0)
			
	if start == True and len(squares) == 10:
		draw_rectangle(screen, 50, 50, (128, 128, 128))
		start = False

	if start == False and len(squares) > 10:
		if snake_x == squares[0] and snake_y == squares[1]\
		or snake_x == squares[2] and snake_y == squares[3]\
		or snake_x == squares[4] and snake_y == squares[5]\
		or snake_x == squares[6] and snake_y == squares[7]\
		or snake_x == squares[8] and snake_y == squares[9]:
			lose = True
			
	pygame.display.flip()
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			#LEFT
			if event.key == 276 and right == False:
				snake_x_diff = -1
				snake_y_diff = 0
				up = False
				down = False
				left = True
				right = False
			#RIGHT
			elif event.key == 275 and left == False:
				snake_x_diff = 1
				snake_y_diff = 0
				up = False
				down = False
				left = False
				right = True
			#DOWN
			elif event.key == 274 and up == False:
				snake_x_diff = 0
				snake_y_diff = 1
				up = False
				down = True
				left = False
				right = False
			#UP
			elif event.key == 273 and down == False:
				snake_x_diff = 0
				snake_y_diff = -1
				up = True
				down = False
				left = False
				right = False
				
	
	pygame.event.clear() 
