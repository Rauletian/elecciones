
import pygame
import random


size = width, height = 400, 400
block_size=10
start=(0,0)
color=(255, 255, 255, 255)
game_speed=1.5
radius=7.5


pygame.font.init()

def main_screen(size):
	screen = pygame.Surface(size)
	return screen

def create_grid(size, block_size):
	pos=[]
	for i in range(0,int(width/block_size)):
		for j in range(0,int(height/block_size)):
			pos.append([i,j])
	return pos





def snake(posx,posy,color,screen):
	pygame.draw.rect(screen,color,[posx,posy,block_size,block_size],block_size)
	


def apples(screen,color,pos_circlex, pos_circley, block_size):
	apple=pygame.draw.rect(screen,color,[pos_circlex,pos_circley,block_size,block_size],block_size)
	
	return apple
	





                    
var=True


def main(var,game_speed):
	pos=create_grid(size,block_size)
	posx=pos[0][0]
	posy=pos[0][1]
	pos_circlex=random.randint(	0,400)
	pos_circley=random.randint(0,400)


	while var:
		screen=pygame.display.set_mode(size)
		pygame.display.set_caption('Snake')
		snake(posx,posy,color,screen)
		pygame.display.update()
		apples(screen,color,pos_circlex, pos_circley, block_size)
		pygame.display.update()
		if posx<0 or posx>width:
			var=False

		elif posy<0 or posy>height:
			var=False
		
		elif round(pos_circlex+2)==posx*block_size and round(pos_circley+2)==posy*block_size:
			for event in pygame.event.get():
			
				if event.type==pygame.KEYDOWN:
					
					if event.key==pygame.K_LEFT:
						snake(posx,posy,color,screen)
						snake(posx+1,posy,color,screen)
						pygame.display.update()

						
					elif event.key==pygame.K_RIGHT:
						snake(posx,posy,color,screen)
						snake(posx-1,posy,color,screen)
						pygame.display.update()
					elif event.key==pygame.K_DOWN:
						snake(posx,posy,color,screen)
						snake(posx,(posy-1),color,screen)
						pygame.display.update()
					

					elif event.key==pygame.K_UP:
						snake(posx,posy,color,screen)
						snake(posx,(posy+1),color,screen)
						pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				var=False

			if event.type==pygame.KEYDOWN:
		
				if event.key==pygame.K_LEFT:
					posx-=game_speed*block_size

					snake(posx,posy,color,screen)
					pygame.display.update()
		                    
				elif event.key==pygame.K_RIGHT:
					posx+=game_speed*block_size
					snake(posx,posy,color,screen)
					pygame.display.update()
				elif event.key==pygame.K_DOWN:
					posy+=game_speed*block_size
					snake(posx,posy,color,screen)
					pygame.display.update()

				

				elif event.key==pygame.K_UP:
					posy-=game_speed*block_size
					snake(posx,posy,color,screen)
					pygame.display.update()

				

				

		


					
																																		                

           		
 
           
               

		
		
		



main(var,game_speed)		



  
