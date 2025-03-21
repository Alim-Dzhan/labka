import pygame
import sys
import datetime as dt

pygame.init()
pygame.mixer.init()

pygame.font.init()
font = pygame.font.Font(None, 30)

i = 0
pause_start_time = None  
elapsed_pause_time = dt.timedelta(0)  
music_pos = 0  

pygame.mixer.music.load("music/sound.mp3")

def play_music():
    global music_pos
    pygame.mixer.music.play(start=music_pos)  

def stop_music():
    global music_pos
    music_pos = pygame.mixer.music.get_pos() / 1000  
    pygame.mixer.music.stop()  

WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("images/clock.png").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

minute_hand = pygame.image.load("images/min_hand.png").convert_alpha()
second_hand = pygame.image.load("images/sec_hand.png").convert_alpha()

clock = pygame.time.Clock()
start_time = dt.datetime.now()  

def blit_rotate_center(surface, image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surface.blit(rotated_image, new_rect.topleft)

def clock_on_off():
    global pause_start_time, elapsed_pause_time

    if pause_start_time:
        current_time = pause_start_time - start_time - elapsed_pause_time
    else:
        current_time = dt.datetime.now() - start_time - elapsed_pause_time

    minutes = current_time.seconds // 60
    seconds = current_time.seconds % 60

    minute_angle = 360 - (minutes / 60) * 360
    second_angle = 360 - (seconds / 60) * 360

    blit_rotate_center(screen, minute_hand, minute_angle, CENTER)
    blit_rotate_center(screen, second_hand, second_angle, CENTER)

play_music()
running = True

while running:
    screen.blit(background, (0, 0))
    clock_on_off()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause_start_time is None:  
                    pause_start_time = dt.datetime.now()
                    stop_music()
                else:  
                    elapsed_pause_time += dt.datetime.now() - pause_start_time
                    pause_start_time = None
                    play_music()

            elif event.key == pygame.K_q:
                running = False

    clock.tick(60)
