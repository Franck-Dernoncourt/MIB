##############################################################################################################
# 
# 2002-01-23: Initial release by Timothy Downs, inputbox written for my map editor
# 2011-01-01: Revision by Franck Dernoncourt <franck.dernoncourt@gmail.com> to make it compilable 
#             with pygame2exe.py (solve font issues, see http://www.pygame.org/pcr/inputbox/index.php#MESSAGES)
#
# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to
#
##############################################################################################################

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key

def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    #fontobject = pygame.font.Font(None, 18)
    fontobject=pygame.font.SysFont('Arial', 18)
    
    
    pygame.draw.rect(screen, (0, 0, 0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()

def ask(screen, question):
    "ask(screen, question) -> answer"
    current_string = []
    display_box(screen, question + ": " + string.join(current_string, ""))
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
            print "ok"
        elif inkey == K_RETURN or K_KP_ENTER:
            break
        elif 65 <= inkey <= 90 or 97 <= inkey <= 122: # Accept only letters
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + string.join(current_string, ""))
    return string.join(current_string, "")
