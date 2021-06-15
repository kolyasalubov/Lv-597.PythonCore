from game_settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("My first game")
player_image = pygame.image.load('./image.jpg').convert()
player_image.set_colorkey(WHITE_COLOR)
text = 'Click on the ball to find out your prediction for the day'

run = True
clock = pygame.time.Clock()

while run:
    screen.blit(player_image, (0, 0))
    red_ball = pygame.draw.circle(screen, RED_COLOR, (200, 500), 50)
    blue_ball = pygame.draw.circle(screen, LIGHT_BLUE_COLOR, (500, 500), 50)
    pink_ball = pygame.draw.circle(screen, PINK_COLOR, (800, 500), 50)
    x_range = list(range(150, 251)) + list(range(450+551)) + list(range(750, 851))
    y_range = list(range(450, 551))
    draw_text(screen, LIGHT_GREEN_COLOR, text, 30, WIDTH_DISPLAY / 2, 10)
    pygame.display.update()
    message = get_message()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_position = pygame.mouse.get_pos()
            if player_position[0] in x_range and player_position[1] in y_range:
                draw_text(screen, ORANGE_COLOR, message, 30, WIDTH_DISPLAY / 2, HEIGHT_DISPLAY/2)
            pygame.display.update()
            pygame.time.delay(2000)
    clock.tick(FPS)


