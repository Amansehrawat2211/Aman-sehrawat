import pygame
import random

# Initialize
pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
black = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
snake_block = 10
speed = 15

font = pygame.font.SysFont(None, 30)


def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])


def show_score(score):
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, [10, 10])


def game():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = random.randrange(0, width - snake_block, snake_block)
    food_y = random.randrange(0, height - snake_block, snake_block)

    while not game_over:

        while game_close:
            screen.fill(white)
            msg = font.render("Game Over! Press C to play again or Q to quit", True, red)
            screen.blit(msg, [60, height // 2])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        draw_snake(snake_block, snake)
        show_score(length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, snake_block)
            food_y = random.randrange(0, height - snake_block, snake_block)
            length += 1

        clock.tick(speed)

    pygame.quit()


game()