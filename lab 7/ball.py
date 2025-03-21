import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
SPEED = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True
while running:
    pygame.time.delay(50)
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS > 0:
                ball_y -= SPEED
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS < HEIGHT:
                ball_y += SPEED
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS > 0:
                ball_x -= SPEED
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS < WIDTH:
                ball_x += SPEED

pygame.quit()