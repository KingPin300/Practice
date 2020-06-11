import pygame
pygame.init()

WIDTH = 1200
HEIGHT = 600
BORDER = 20

screen = pygame.display.set_mode((WIDTH,HEIGHT))

fg = pygame.Color("white")

pygame.draw.rect(screen, fg, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fg, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fg, pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))
pygame.display.flip()

while True:
	e = pygame.event.poll()
	if e.type == pygame.QUIT:
		break
