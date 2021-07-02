
from Classes.Bases import *
from Classes.Main import *

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()
while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	screen.fill((175,215,70))
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)

