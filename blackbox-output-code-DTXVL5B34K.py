import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 5, 5
ball_radius = 20

# Paddle properties
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 30
paddle_speed = 10

# Clock for FPS
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    
    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy
    
    # Ball collision with paddle
    if (ball_y + ball_radius >= paddle_y and
        paddle_x <= ball_x <= paddle_x + paddle_width and
        ball_dy > 0):
        ball_dy = -ball_dy
    
    # Ball falls off screen (game over)
    if ball_y > HEIGHT:
        print("Game Over!")
        running = False
    
    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Draw paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()