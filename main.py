import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	clock = pygame.time.Clock()

	while True:
		#limit the framerate 
		clock.tick(60)
		dt = 1/60

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		player.update(dt)
		player.draw(screen)

		#FPS Calculator
		fps = clock.get_fps()
		pygame.display.set_caption(f"FPS: {fps:.2f}")

		pygame.display.flip()

if __name__ == "__main__":
	main()
