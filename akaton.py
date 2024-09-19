import pygame
from gtts import gTTS
import sys
#
pygame.mixer.init()
BLACK = (0, 0, 0)
purple = (127, 0, 225)
GREEN = (0, 255, 0)
WIDTH = 155
HEIGHT = 155
MARGIN = 5
happy_list = []
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)
pygame.init()
happy = pygame.image.load("C:\\Users\\jbt\\Downloads\\pixil-frame-0 (5).png")
sad = pygame.image.load("C:\\Users\\jbt\\Downloads\\sad.png")



# Set the size for the image
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("SPECIAL READ")
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
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
            color = purple
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    x = 0
    y = 0
    z = 190
    u = 30
    grid.append([])
    screen.blit(happy, (-160, -80))
    happy = pygame.transform.scale(happy, (500, 400))
    screen.blit(sad, (1, -75))
    sad = pygame.transform.scale(sad, (500, 400))
    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = event.pos
        if happy.get_rect().collidepoint(x, y):
            sound_file = "sound_file.mp3"
            tts = gTTS(text='happy', lang='en')
            tts.save(sound_file)
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            print('clicked on image')
        # z, y = event.pos
        # if sad.get_rect().collidepoint(z, y):
        #     sound_file = "sound_file.mp3"
        #     tts = gTTS(text='sad', lang='en')
        #     tts.save(sound_file)
        #     sound = pygame.mixer.Sound(sound_file)
        #     sound.play()
        #     print('clicked on 2')
    pygame.display.update()
pygame.quit()


# width, height = 450, 500
# width, height = 550, 550
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Click on Emoji')
#
# redSquare = pygame.image.load("C:\\Users\\jbt\\Downloads\\pixil-frame-0 (1).png").convert()
# pic = pygame.image.load("C:\\Users\\jbt\\Downloads\\sad.png").convert()
# tierd = pygame.image.load("C:\\Users\\jbt\\Downloads\\download.png").convert()
#
# positions = [(0, 0), (101, 0), (201, 0)]
# positions = [(0, 0), (105, 0), (201, 0)]
# emotions = ['happy', 'sad', 'mad']
#
# # Create Rect objects for collision detection
# image_rects = [
#     redSquare.get_rect(topleft=positions[0]),
#     pic.get_rect(topleft=positions[1]),
#     tierd.get_rect(topleft=positions[2])
# ]
#
# screen.blit(redSquare, positions[0])
# screen.blit(pic, positions[1])
# screen.blit(tierd, positions[2])
# pygame.display.flip()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = event.pos
#             for i, rect in enumerate(image_rects):
#                 if rect.collidepoint(mouse_x, mouse_y):
#                     emotion = emotions[i]
#                     sound_file = f"{emotion}_sound.mp3"
#                     tts = gTTS(text=emotion, lang='en')
#                     tts.save(sound_file)
#                     sound = pygame.mixer.Sound(sound_file)
#                     sound.play()
#                     print(f'Clicked on {emotion} emoji')
#
# pygame.quit()
#
#






















# pygame.mixer.init()
# BLACK = (0, 0, 0)
# purple = (127, 0, 225)
# GREEN = (0, 255, 0)
# WIDTH = 155
# HEIGHT = 155
# MARGIN = 5
# happy_list = []
# grid = []
# for row in range(5):
#     grid.append([])
#     for column in range(5):
#         grid[row].append(0)
# pygame.init()
#
# happy = pygame.image.load("C:\\Users\\jbt\\Downloads\\pixil-frame-0 (1).png")
# sad = pygame.image.load("C:\\Users\\jbt\\Downloads\\pixil-frame-0 (3).png")
# # Set the size for the image
# WINDOW_SIZE = [800, 800]
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("SPECIAL READ")
# # Loop until the user clicks the close button.
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to one
#             grid[row][column] = 1
#             print("Click ", pos, "Grid coordinates: ", row, column)
#     screen.fill(BLACK)
#     # Draw the grid
#     for row in range(5):
#         for column in range(5):
#             color = purple
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
#     x = 30
#     y = 30
#     z = 190
#     grid.append([])
#     screen.blit(happy, (x, y))
#     sad_size = pygame.transform.scale(sad, (x,y))
#     screen.blit(sad, (z, y))
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         x, y = event.pos
#         if sad.get_rect().collidepoint(z, y):
#             sound_file = "sound_file.mp3"
#             tts = gTTS(text='sad', lang='en')
#             tts.save(sound_file)
#             sound = pygame.mixer.Sound(sound_file)
#             sound.play()
# #             print('clicked on image')
#     pygame.display.update()
# pygame.quit()
#









#
# for row in range(5):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(5):
#         grid[row].append(0)  # Append cell
# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# pygame.init()
# # Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [800, 800]
# screen = pygame.display.set_mode(WINDOW_SIZE)
# # Set title of screen
# pygame.display.set_caption("SPECIAL READ")
# width = 800
# height = 800
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('clicked on image')
# happy = pygame.image.load("C:\\Users\\jbt\\Downloads\\pixil-frame-0 (1).png").convert()
# x = 0
# y = 0
# screen.blit(happy, (x, y))

# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#             if happy.get_rect().collidepoint(x, y):
#                 sound_file = "sound_file.mp3"
#                 tts = gTTS(text='happy', lang='en')
#                 tts.save(sound_file)
#                 sound = pygame.mixer.Sound(sound_file)
#                 sound.play()
#                 print('clicked on image')
# pygame.display.update()
# pygame.quit()

#
#
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# # This sets the WIDTH and HEIGHT of each grid location
# WIDTH = 155
# HEIGHT = 155
# MARGIN = 5
# happy_list = []
# # array is simply a list of lists.
# grid = []
# for row in range(5):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(5):
#         grid[row].append(0)  # Append cell
# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# pygame.init()
# # Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [800, 800]
# screen = pygame.display.set_mode(WINDOW_SIZE)
# # Set title of screen
# pygame.display.set_caption("SPECIAL READ")
#
# # Loop until the user clicks the close button.
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to one
#             grid[row][column] = 1
#             print("Click ", pos, "Grid coordinates: ", row, column)
#     screen.fill(BLACK)
#     # Draw the grid
#     for row in range(5):
#         for column in range(5):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
#
#     clock.tick(60)
#     pygame.display.update()
# pygame.quit()

#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
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


# yes = pygame.image.load("C:\\Users\\jbt\\Downloads\\yes-sign-henrik-lehnerer.jpg")
# no = pygame.image.load("C:\\Users\\jbt\Downloads\\NO_large.webp")