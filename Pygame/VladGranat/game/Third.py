import pygame
pygame.init()

win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__000.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__001.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__002.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__003.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__004.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__005.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__006.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__007.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__008.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__009.png")]
walkLeft = [pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__000.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__001.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__002.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__003.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__004.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__005.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__006.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__007.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__008.png"),
pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Run__back__009.png")]
bg = pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\jungle2.jpg")
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\parallax-forest-front-trees.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\parallax-forest-lights.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\parallax-forest-middle-trees.png")
char = pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__000.png")
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__001.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__002.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__003.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__004.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__005.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__006.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__007.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__008.png"),
# pygame.image.load("C:\VandPy\Lv-597.PythonCore\Lesson 9\game\Idle__009.png")

x = 50
y = 250
width = 4
height = 6
vel = 10

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 700 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()