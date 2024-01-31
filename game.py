import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Race Track")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

# Set up player variables
car_width, car_height = 40, 60
car_img = pygame.image.load('218071.png').convert_alpha()  # Load car image with transparency
car_img = pygame.transform.scale(car_img, (car_width, car_height))
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 100
car_speed = .2
car_angle = 0

# Main game loop
while True:
    screen.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement and rotation
    dx, dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_RIGHT]:
        dx += 1
    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1

    # Calculate car angle based on movement direction
    if dx != 0 or dy != 0:
        if dx == 0:
            if dy > 0:
                car_angle = 90
            else:
                car_angle = 270
        else:
            car_angle = math.degrees(math.atan2(dy, dx)) - 90
        car_angle %= 360

    # Move the car
    car_x += dx * car_speed
    car_y += dy * car_speed

    # Boundary checking
    if car_x < 50:
        car_x = 50
    elif car_x > WIDTH - 50 - car_width:
        car_x = WIDTH - 50 - car_width
    if car_y < 50:
        car_y = 50
    elif car_y > HEIGHT - 150 - car_height:
        car_y = HEIGHT - 150 - car_height

    # Draw race track
    pygame.draw.rect(screen, GREEN, (50, 50, WIDTH - 100, HEIGHT - 150), 10)

    # Rotate and draw car
    rotated_car = pygame.transform.rotate(car_img, car_angle)
    car_rect = rotated_car.get_rect(center=(car_x + car_width / 2, car_y + car_height / 2))
    screen.blit(rotated_car, car_rect.topleft)

    # Update display
    pygame.display.flip()
