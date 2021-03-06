import pygame as pg 
import sys 
import time 
from pygame.locals import *

# Setting up few properties
XO = 'x'
winner = None
draw = None
width = 500
height = 450
white = (255, 255, 255)
line_color = (130, 0, 0)  
board = [[None]*3, [None]*3, [None]*3] 
pg.init() 
fps = 30
CLOCK = pg.time.Clock() 
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Turtle") 
time.sleep(5)

# loading the images as python object 
initiating_window = pg.image.load("resources/modified_cover.png") 
x_img = pg.image.load("resources/X_modified.png") 
y_img = pg.image.load("resources/o_modified.png") 
rematch = pg.image.load("resources/rematch.jpg")
thanks = pg.image.load("resources/thanks.jpg")
arko = pg.image.load("resources/arko.jpg")
code_loop = pg.image.load("resources/code_loop.jpg")
the_as8_org = pg.image.load("resources/the_as8_org.jpg")

# resizing images 
initiating_window = pg.transform.scale(initiating_window, (width, height + 100)) 
x_img = pg.transform.scale(x_img, (80, 80)) 
o_img = pg.transform.scale(y_img, (80, 80)) 

# Sounds and Music
x_sound = pg.mixer.Sound("resources/x.wav")
o_sound = pg.mixer.Sound("resources/o.wav")
m_sound = pg.mixer.Sound("resources/m.wav")
music = pg.mixer.music.load("resources/music.mp3")
pg.mixer.music.play(-1)

def screen_timer(screen,time,slide):
    i = 0
    while i < time+1:
        CLOCK.tick(fps)
        screen.blit(slide, (0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        i += 1
        pg.display.update()

def game_initiating_window(): 
	screen.blit(initiating_window, (0, 0)) 

	pg.display.update() 
	time.sleep(3)					 
	screen.fill(white) 

	# drawing vertical lines 
	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7) 
	pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7) 

	# drawing horizontal lines 
	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7) 
	pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7) 
	draw_status() 

def draw_status(): 
	global draw 
	
	if winner is None: 
		message = XO.upper() + "'s Turn"
	else: 
		message = winner.upper() + " won !"
	if draw: 
		message = "Game Draw !"

	font = pg.font.SysFont("georgia", 40)  
	text = font.render(message, 1, (255, 255, 255)) 
	screen.fill ((130, 0, 0), (0, 450, 500, 100)) 
	text_rect = text.get_rect(center =(width / 2, 500)) 
	screen.blit(text, text_rect) 
	pg.display.update() 
	
def check_win(): 
	global board, winner, draw 

	# checking for winning rows 
	for row in range(0, 3): 
		if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)): 
			winner = board[row][0]
			m_sound.play() 
			time.sleep(0.5)
			pg.draw.line(screen, (130, 0, 0), (0, (row + 1)*height / 3 -height / 6), (width, (row + 1)*height / 3 - height / 6 ), 5) 
			break

	# checking for winning columns 
	for col in range(0, 3): 
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)): 
			winner = board[0][col]
			m_sound.play() 
			time.sleep(0.5)
			pg.draw.line(screen, (130, 0, 0), ((col + 1)* width / 3 - width / 6, 0), ((col + 1)* width / 3 - width / 6, height), 5) 
			break

	# check for diagonal winners 
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None): 
		
		# game won diagonally left to right 
		winner = board[0][0]
		m_sound.play() 
		time.sleep(0.5)
		pg.draw.line(screen, (130, 0, 0), (50, 50), (450, 400), 5) 
		
	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None): 
		
		# game won diagonally right to left 
		winner = board[0][2]
		m_sound.play() 
		time.sleep(0.5)
		pg.draw.line (screen, (130, 0, 0), (450, 50), (50, 400), 5) 

	if(all([all(row) for row in board]) and winner is None ): 
		draw = True
	draw_status() 
	
def drawXO(row, col): 
	global board, XO 

	if row == 1: 
		posx = 40

	if row == 2: 
		posx = width / 3 + 25
		
	if row == 3: 
		posx = width / 3 * 2 + 10

	if col == 1: 
		posy = 47
		
	if col == 2: 
		posy = height / 3 + 65
	
	if col == 3: 
		posy = height / 3 * 2 + 80

	board[row-1][col-1] = XO 
	
	if(XO == 'x'): 
		x_sound.play()
		time.sleep(0.6)
		screen.blit(x_img, (posy, posx)) 
		XO = 'o'
	
	else: 
		o_sound.play()
		time.sleep(0.6)
		screen.blit(o_img, (posy, posx)) 
		XO = 'x'
	pg.display.update() 

def user_click():
	x, y = pg.mouse.get_pos() 

	if(x<width / 3): 
		col = 1
	
	elif (x<width / 3 * 2): 
		col = 2
	
	elif(x<width): 
		col = 3
	
	else: 
		col = None

	if(y<height / 3): 
		row = 1
	
	elif (y<height / 3 * 2): 
		row = 2
	
	elif(y<height): 
		row = 3
	
	else: 
		row = None

	if(row and col and board[row-1][col-1] is None): 
		global XO 
		drawXO(row, col) 
		check_win() 

def reset_game1(): 
	time.sleep(3)
	screen.blit(rematch, (0,0))
	pg.display.update()
	x, y = pg.mouse.get_pos()
	if (x<255 and x > 170) and (y>275 and y<360):
		reset_game2()
	elif (x>265 and x<330) and (y>275 and y<360):
		screen_timer(screen,150,thanks)
		screen_timer(screen,200,arko)
		screen_timer(screen,150,code_loop)
		screen_timer(screen,200,the_as8_org)
		screen_timer(screen,200,initiating_window)		
		pg.quit()
		sys.exit()

def reset_game2(): 
	global board, winner, XO, draw 
	XO = 'x'
	draw = False
	game_initiating_window() 
	winner = None
	board = [[None]*3, [None]*3, [None]*3] 

game_initiating_window() 

while(True): 
	for event in pg.event.get(): 
		if event.type == QUIT: 
			pg.quit() 
			sys.exit() 
		elif event.type is MOUSEBUTTONDOWN: 
			user_click() 
			if(winner or draw): 
				reset_game1() 
	pg.display.update() 
	CLOCK.tick(fps) 
