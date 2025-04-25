import pygame
import random
import sys
import time
import psycopg2

#  1. НАСТРОЙКА POSTGRES

def connect_db():
    """Подключение к PostgreSQL. Обновите данные для подключения, если необходимо."""
    return psycopg2.connect(
        host="localhost",
        dbname="snake",    
        user="postgres",
        password="Alimzhan05032007"  
    )

def get_user_id(username):
    """Возвращает user_id из таблицы 'users'; создает, если не существует."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                # Создать нового пользователя
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id

def load_progress(user_id):
    """Возвращает последний известный счёт и уровень пользователя, или (0,0), если их нет."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level 
                FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            row = cur.fetchone()
            return row if row else (0, 0)

def save_progress(user_id, score, level):
    """Вставить текущий счёт и уровень в таблицу 'user_score'."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()
    print(f"Прогресс сохранен: user_id={user_id}, score={score}, level={level}")



USERNAME = input("Введите ваш никнейм: ")
USER_ID = get_user_id(USERNAME)
score, level = load_progress(USER_ID)

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (80, 80, 80)
YELLOW = (255, 255, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Опциональные звуки
eat_sound = None
crash_sound = None
try:
    eat_sound = pygame.mixer.Sound("coin.mp3")
    crash_sound = pygame.mixer.Sound("crash.mp3")
except:
    print("Опционально: поместите 'eat.wav' и 'crash.wav' в ту же папку, если хотите звук.")

#  3. УРОВНИ И СТЕНЫ   

def get_level(score):
    """Возвращает уровень в зависимости от счёта игрока."""
    if score < 5:
        return 0
    elif score < 10:
        return 1
    else:
        return 2

def get_speed(level):
    """Базовая скорость для каждого уровня."""
    if level == 0:
        return 8
    elif level == 1:
        return 12
    else:
        return 15

def get_walls_for_level(level):
    """Генерация набора координат стен для каждого уровня."""
    walls = set()
    # Уровень 0: только границы
    if level >= 0:
        for x in range(GRID_WIDTH):
            walls.add((x, 0))
            walls.add((x, GRID_HEIGHT - 1))
        for y in range(GRID_HEIGHT):
            walls.add((0, y))
            walls.add((GRID_WIDTH - 1, y))

    # Уровень 1: добавляем простую диагональ
    if level >= 1:
        for i in range(5, 15):
            walls.add((i, i))

    # Уровень 2: добавляем несколько блоков в центре
    if level >= 2:
        for i in range(10, 20):
            walls.add((i, GRID_HEIGHT - i))

    return walls

#  4. ПЕРЕМЕННЫЕ ИГРЫ  

snake = [(5, 5)]
direction = (1, 0)
game_over = False

food = (0, 0)
food_timer = time.time()
FOOD_LIFETIME = 5
food_value = 1

# Определим функцию для появления еды НЕ на стенах или змее
def spawn_food():
    global food, food_value, food_timer
    while True:
        candidate = (
            random.randint(1, GRID_WIDTH - 2),
            random.randint(1, GRID_HEIGHT - 2)
        )
        if candidate not in walls and candidate not in snake:
            food = candidate
            break
    food_value = random.choice([1, 2, 3])
    food_timer = time.time()

level = get_level(score)
speed = get_speed(level)
walls = get_walls_for_level(level)
spawn_food()


#  5. ОСНОВНЫЕ ФУНКЦИИ   

def draw_all():
    """Отображает всю игровую сцену."""
    win.fill(GREEN)

    # Отображаем стены
    for wx, wy in walls:
        pygame.draw.rect(win, GRAY, (wx*CELL_SIZE, wy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отображаем еду
    pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    txt = font.render(str(food_value), True, BLACK)
    win.blit(txt, (food[0]*CELL_SIZE + 5, food[1]*CELL_SIZE))

    # Отображаем змею
    for sx, sy in snake:
        pygame.draw.rect(win, BLACK, (sx*CELL_SIZE, sy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Счёт и уровень
    s1 = font.render(f"Пользователь: {USERNAME}", True, WHITE)
    s2 = font.render(f"Счёт: {score}", True, WHITE)
    s3 = font.render(f"Уровень: {level}", True, WHITE)
    win.blit(s1, (10, 10))
    win.blit(s2, (10, 40))
    win.blit(s3, (10, 70))

    pygame.display.update()

def update_snake():
    """Двигает змею, проверяет столкновения, появляется новая еда, обновляет глобальные переменные (счёт, уровень, стены, скорость)."""
    global game_over, score, level, speed, walls

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # Проверка на столкновение с собой или со стенами
    if new_head in snake or new_head in walls:
        if crash_sound: crash_sound.play()
        game_over = True
        return

    # Проверка на границу
    if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        if crash_sound: crash_sound.play()
        game_over = True
        return

    # Добавляем новую голову
    snake.insert(0, new_head)

    # Если съели еду
    if new_head == food:
        if eat_sound: eat_sound.play()
        global food_value
        score += food_value
        spawn_food()
        # Возможно обновим уровень/скорость/стены
        new_level = get_level(score)
        if new_level != level:
            level = new_level
            speed = get_speed(level)
            walls = get_walls_for_level(level)
    else:
        snake.pop()

    # Время жизни еды
    if time.time() - food_timer > FOOD_LIFETIME:
        spawn_food()

def pause_game():
    """Пауза в игре, сохраняет в БД, ожидает ввода пользователя (продолжить или выйти)."""
    save_progress(USER_ID, score, level)

    paused_text = font.render("Пауза: Нажмите C для продолжения, Q для выхода", True, YELLOW)
    paused = True
    while paused:
        win.fill(BLACK)
        win.blit(paused_text, (WIDTH//2 - paused_text.get_width()//2, HEIGHT//2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    save_progress(USER_ID, score, level)
                    pygame.quit()
                    sys.exit()


#  6. ОСНОВНОЙ ЦИКЛ ИГРЫ   

while True:
    clock.tick(speed)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_p:
                    pause_game()

        update_snake()
        draw_all()
    else:
        # Состояние "Игра завершена"
        win.fill(BLACK)
        go_text = font.render("Игра завершена! Нажмите R для перезапуска", True, YELLOW)
        sc_text = font.render(f"Итоговый счёт: {score}", True, WHITE)
        win.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 30))
        win.blit(sc_text, (WIDTH//2 - sc_text.get_width()//2, HEIGHT//2 + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Сброс
                    snake = [(5,5)]
                    direction = (1,0)
                    score, level = 0, 0
                    speed = get_speed(level)
                    walls = get_walls_for_level(level)
                    spawn_food()
                    game_over = False

                    
''' 
DROP TABLE IF EXISTS user_score;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    score INTEGER NOT NULL,
    level INTEGER NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM users;
SELECT * FROM user_score;
'''