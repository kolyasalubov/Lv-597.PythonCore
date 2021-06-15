import pygame
import random

WIDTH_DISPLAY = 1000
HEIGHT_DISPLAY = 700
FPS = 30
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 167, 0)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
RED_COLOR = (255, 0, 0)
LIGHT_GREEN_COLOR = (90, 170, 170)
ORANGE_COLOR = (255, 175, 0)
PI = 3.14
COORD_X = 50
COORD_Y = 50
DELTA_STEP = 5
font_name = pygame.font.match_font('arial')


def draw_text(surf, color, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def get_message():
    messages = ['You will have a wonderful day!', 'Expect good news!', 'Take EVERYTHING from life!',
                'Learn to find joy in life.', 'All wishes and plans will come true',
                'You will have good luck and overcome many hardships', 'Be confident in yourself!',
                'Your cherished wish will come true this week', 'You have a very pretty smile. Smile often!',
                'Failure is an experience that is given to you to draw the right conclusions.']
    message = random.choices(messages)
    return message[0]
