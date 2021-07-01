import pygame,sys
from Classes.snake import testprint

testprint()

pygame.init()
screen = pygame.display.set_mode((300,400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


