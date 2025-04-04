import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Pygame Music Player")

pygame.font.init()
font = pygame.font.Font(None, 30)

music_dir = "music"
playlist = [os.path.join(music_dir, song) for song in os.listdir(music_dir) if song.endswith(".mp3")]

if not playlist:
    print("No songs found in the 'music' folder!")
    exit()

current_track = 0
is_playing = False

pygame.mixer.music.load(playlist[current_track])

def play_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.play()
        is_playing = True
    else:
        pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.pause()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill((255, 255, 255))

    instructions = font.render("P: Play | S: Stop | N: Next | B: Previous | Q: Quit", True, (0, 0, 0))
    screen.blit(instructions, (20, 50))

    track_name = font.render(f"Now Playing: {os.path.basename(playlist[current_track])}", True, (0, 0, 255))
    screen.blit(track_name, (20, 100))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()
            elif event.key == pygame.K_q:
                running = False

pygame.quit()