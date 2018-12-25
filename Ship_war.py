import pygame

pygame.init()
white_color = (255, 255, 255)
blue_color = (1, 1, 232)
green_color = (55, 238, 2)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Coding...")
clock = pygame.time.Clock()

space_ship = pygame.Rect(10, 10, 45, 45)

def ship(x, y):
    space_ship = pygame.Rect(x, y, 45, 45)
    pygame.draw.rect(game_display, blue_color, space_ship)

x = (display_width - 780)
y = (display_height - ((580/2) + 45))

x_change_position = 0
y_change_position = 0
speed = 4
FPS = 60

exit_game = False


while exit_game != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_change_position -= speed

            elif event.key == pygame.K_s:
                y_change_position += speed

            if event.key == pygame.K_a:
                x_change_position -= speed

            elif event.key == pygame.K_d:
                x_change_position += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_change_position = 0

            elif event.key == pygame.K_s:
                y_change_position = 0

            if event.key == pygame.K_a:
                x_change_position = 0

            elif event.key == pygame.K_d:
                x_change_position = 0

    x += x_change_position
    y += y_change_position

    game_display.fill(green_color)
    ship(x, y)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
