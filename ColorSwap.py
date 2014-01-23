import pygame
import sys

pygame.init()
 
screen = pygame.display.set_mode([610,610])
  
fps = 30
   
Clock = pygame.time.Clock()
    
WHITE = 255,255,255
BLUE = 0,0,255
GREEN = 0,255,0
RED = 255,0,0

COLS = 10
ROWS = 10

BLOCK = 50
SPACE = 10

grid = [[''for i in xrange(ROWS)]for i in xrange(COLS)]
posx, posy = SPACE, SPACE
for i in xrange(ROWS):
    for j in xrange(COLS):
        grid[i][j] = ([WHITE, posx, posy])
        posy = posy+BLOCK+SPACE
    posx = posx+BLOCK+SPACE
    posy = SPACE

def draw_grid():
    for i in xrange(ROWS):
        for j in xrange(COLS):
            pygame.draw.rect(screen, grid[i][j][0], (grid[i][j][1], grid[i][j][2], BLOCK, BLOCK))

def is_square_clicked(mousepos):
    x, y = mousepos
    for i in xrange(ROWS):
        for j in xrange(COLS):
            if x >= grid[i][j][1] and x <= grid[i][j][1] + BLOCK:
                if y >= grid[i][j][2] and y <= grid[i][j][2] + BLOCK: 
                    if grid[i][j][0] == WHITE:
                        grid[i][j][0] = BLUE
                    elif grid[i][j][0] == BLUE:
                        grid[i][j][0] = GREEN
                    elif grid[i][j][0] == GREEN:
                        grid[i][j][0] = RED
                    elif grid[i][j][0] == RED:
                        grid[i][j][0] = WHITE

clicked = False
while __name__ == '__main__':
    tickFPS = Clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (Clock.get_fps()))
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mousepos = pygame.mouse.get_pos()
            is_square_clicked(mousepos)
            clicked = True
    pygame.display.update()