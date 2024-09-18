import pygame
from gtts import gTTS
import sys

pygame.init()
# board = [[0 for x in range(5)] for row in range(5)]
# cols, rows = 5, 5
# cell_size = 130
# window_size = (cols * cell_size, rows * cell_size)



pygame.mixer.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('clicked on image')
happy = pygame.image.load("C:\\Users\\jbt\\Downloads\\happy.png").convert()

x = 0
y = 0
screen.blit(happy, (x, y))
pygame.display.flip()

running = True
while running:
    # screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if happy.get_rect().collidepoint(x, y):
                sound_file = "sound_file.mp3"
                tts = gTTS(text='happy', lang='en')
                tts.save(sound_file)
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
                print('clicked on image')




























#
#
#
#
#


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 155
HEIGHT = 155
MARGIN = 5
happy_list = []
# array is simply a list of lists.
grid = []
for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(5):
        grid[row].append(0)  # Append cell
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
pygame.init()
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set title of screen
pygame.display.set_caption("SPECIAL READ")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
    screen.fill(BLACK)
    # Draw the grid
    for row in range(5):
        for column in range(5):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])

    clock.tick(60)
    pygame.display.update()
pygame.quit()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#







# row_happy = 100
# col_happy = 200
# x = 200
# y = 200
# happy = pygame.image.load("C:\\Users\\jbt\\Downloads\\happy.png")
# sad = pygame.image.load("C:\\Users\\jbt\\Downloads\\sad.png")
# happy_SIZE = (x,y)
# # sad_SIZE = (x,y)
# screen = pygame.display.set_mode((500, 500))
# pygame.init()
# done = False
#
# c = (0, 150, 255)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     for x in range(0, 450, 100):
#         pygame.draw.line(screen,c,(1,x),(600,x),2)
#         pygame.draw.line(screen,c,(x,1),(x,600),2)
#
#     screen.blit(happy,(0,0))
#     # screen.blit(sad,(50,0))
#
#     pygame.display.update()
# pygame.quit()
#
#
#
# #
# #
# #         pygame.display.set_caption('image')
# #         screen.blit(happy, (happy_SIZE))
# # pygame.display.flip()
# # status = True
