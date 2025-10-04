import pygame
import random
import sys

# Constants
GRID_SIZE = 50
CELL_SIZE = 12
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def random_position(snake):
    while True:
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if pos not in snake:
            return pos

def draw_cell(surface, color, pos):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = [(GRID_SIZE//2, GRID_SIZE//2)]
    direction = RIGHT
    food = random_position(snake)
    growing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != DOWN:
                    direction = UP
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != UP:
                    direction = DOWN
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != RIGHT:
                    direction = LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != LEFT:
                    direction = RIGHT

        # Move snake
        head_x, head_y = snake[0]
        delta_x, delta_y = direction
        new_head = ((head_x + delta_x) % GRID_SIZE, (head_y + delta_y) % GRID_SIZE)

        # Check collision with self
        if new_head in snake:
            break  # Game over

        snake.insert(0, new_head)

        # Check food collision
        if new_head == food:
            food = random_position(snake)
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_cell(screen, RED, food)
        for pos in snake:
            draw_cell(screen, GREEN, pos)
        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (WINDOW_SIZE//2 - text.get_width()//2, WINDOW_SIZE//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == "__main__":
    main()