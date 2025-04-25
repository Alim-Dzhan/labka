import pygame
import sys
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("images/clock.png").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

minute_hand = pygame.image.load("images/min_hand.png").convert_alpha()
second_hand = pygame.image.load("images/sec_hand.png").convert_alpha()

clock = pygame.time.Clock()

def blit_rotate_center(surface, image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surface.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = 360 - (minute / 60) * 360
    second_angle = 360 - (second / 60) * 360

    screen.blit(background, (0, 0))
    
    blit_rotate_center(screen, minute_hand, minute_angle, CENTER)
    blit_rotate_center(screen, second_hand, second_angle, CENTER)

    pygame.display.flip()
    clock.tick(60)