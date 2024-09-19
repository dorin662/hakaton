import pygame
import pygame_menu
from gtts import gTTS
import os
import playsound

pygame.init()
surface = pygame.display.set_mode((600, 500))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def play_sound(sound_file):
    playsound.playsound(sound_file)


def start_the_game():
    images_sounds = [
        ('C:/Users/jbt/Downloads/SHIRT.png', "angry.mp3"),
        ("C:/Users/jbt/Downloads/ME.webp", "happy.mp3"),
        ("C:/Users/jbt/Downloads/HAT.jfif", "me.mp3"),
        ('C:/Users/jbt/Downloads/bomb.png', "no.mp3"),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, (_, sound_file) in enumerate(images_sounds):
                    img_rect = pygame.Rect(100 + i * 150, 200, 100, 100)
                    if img_rect.collidepoint(event.pos):
                        play_sound(sound_file)

        surface.fill('white')

        # show images
        for i, (img_file, _) in enumerate(images_sounds):
            image = pygame.image.load(img_file)
            image = pygame.transform.scale(image, (100, 100))
            surface.blit(image, (100 + i * 150, 200))

        pygame.display.update()


def text_speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    playsound.playsound('output.mp3')
    os.remove('output.mp3')


def level_menu():
    font = pygame.font.Font(None, 36)
    user_input = ''
    input_active = True

    back_button_font = pygame.font.Font(None, 28)
    back_button = back_button_font.render("Back to Home", True, (255, 255, 255))
    back_button_rect = back_button.get_rect(center=(400, 400))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running = False  # exit home page
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    # reading
                    text_speak(user_input)
                    user_input = ''  # restart input
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # del key
                else:
                    user_input += event.unicode  # print giving key

        surface.fill((0, 0, 0))

        # show input text
        text = font.render('please enter your word:', True, (230, 230, 230))
        text_surfac = font.render('- ', True, (240, 240, 240))
        text_surface = font.render(user_input, True, (255, 255, 255))
        surface.blit(text, (50, 200))
        surface.blit(text_surfac, (80, 300))
        surface.blit(text_surface, (100, 300))

        # print home page button
        surface.blit(back_button, back_button_rect)
        pygame.display.update()

    return  #home page


mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='')
mainmenu.add.button('Board', start_the_game)
mainmenu.add.button('Text', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()