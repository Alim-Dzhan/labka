import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALETTE = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
ERASER_COLOR = WHITE


font = pygame.font.SysFont("Arial", 18)


current_color = BLACK
brush_size = 5
drawing = False
current_shape = "free"  

win.fill(WHITE)


palette_rects = []
for i, color in enumerate(PALETTE):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, color))


eraser_btn = pygame.Rect(10, 50, 80, 30)
save_btn = pygame.Rect(100, 50, 80, 30)

def draw_ui():
    for rect, color in palette_rects:
        pygame.draw.rect(win, color, rect)
        if color == current_color:
            pygame.draw.rect(win, WHITE, rect, 3) 


    pygame.draw.rect(win, (200, 200, 200), eraser_btn)
    pygame.draw.rect(win, (200, 200, 200), save_btn)
    win.blit(font.render("Eraser", True, BLACK), (eraser_btn.x + 10, eraser_btn.y + 5))
    win.blit(font.render("Save", True, BLACK), (save_btn.x + 20, save_btn.y + 5))

def save_drawing():
    pygame.image.save(win, "drawing.png")
    print("Saved to drawing.png")

def draw_shape(shape, start, end):
    x1, y1 = start
    x2, y2 = end

    if shape == "circle":
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        pygame.draw.circle(win, current_color, (x1, y1), radius)

    elif shape == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(win, current_color, pygame.Rect(x1, y1, side, side))


run = True
while run:
    draw_ui()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                drawing = True

                
                for rect, color in palette_rects:
                    if rect.collidepoint(mouse_pos):
                        current_color = color
                        drawing = False

               
                if eraser_btn.collidepoint(mouse_pos):
                    current_color = ERASER_COLOR
                    drawing = False

                
                if save_btn.collidepoint(mouse_pos):
                    save_drawing()
                    drawing = False

        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = "circle"  
            elif event.key == pygame.K_2:
                current_shape = "square"  
            elif event.key == pygame.K_0:
                current_shape = "free"  

    if drawing and current_shape != "free":
        mx, my = pygame.mouse.get_pos()
        draw_shape(current_shape, mouse_pos, (mx, my))


    if drawing and current_shape == "free":
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(win, current_color, (mx, my), brush_size)

pygame.quit()
sys.exit()
