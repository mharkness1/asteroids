import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	AsteroidField.containers = (updatable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		#limit the framerate 
		clock.tick(60)
		dt = 1/60

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		
		for item in updatable:
			item.update(dt)
		
		for item in asteroids:
			if item.collision(player):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if item.collision(shot):
					shot.kill()
					item.split()

		for item in drawable:
			item.draw(screen)

		#FPS Calculator
		fps = clock.get_fps()
		pygame.display.set_caption(f"FPS: {fps:.2f}")

		pygame.display.flip()

if __name__ == "__main__":
	main()
