import pygame
import random
import csv
def reset():
    screen.blit(background, (0,0))
    pygame.display.flip()
    with open('Hangman.csv', 'r') as f:
        words = csv.reader(f)
        word = list()
        for x in words:
            word.extend(str.upper(random.choice(x)))
    return word, 0, 0
pygame.init()
random.seed()
screen = pygame.display.set_mode(size = (1366,768), flags = pygame.FULLSCREEN | pygame.NOFRAME | pygame.SCALED, vsync=1)
pygame.display.set_caption('Hangman')
background = pygame.image.load('Background.bmp').convert()
over = pygame.image.load('Over.bmp').convert()
over.set_colorkey((255,255,255))
retry = pygame.image.load('Retry.bmp').convert()
retry.set_colorkey((255,255,255))
cancel = pygame.image.load('Cancel.bmp').convert()
cancel.set_colorkey((255,255,255))
man = list()
man.append((pygame.image.load('Head.bmp').convert(), 1187, 420))
man.append((pygame.image.load('Body.bmp').convert(), 1208, 460))
man.append((pygame.image.load('Left.bmp').convert(), 1178, 465))
man.append((pygame.image.load('Right.bmp').convert(), 1212, 467))
man.append((man[2][0],1178, 527))
man.append((man[3][0],1212, 529))
for i in man:
    i[0].set_colorkey((255, 255, 255))
font = pygame.font.SysFont(random.choice(pygame.font.get_fonts()), 64)
word, correct, incorrect = reset()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            x = chr(pygame.key.get_pressed().index(True) + 61)
            if x not in word and incorrect<6:
                screen.blit(man[incorrect][0],man[incorrect][1:])
                incorrect+=1
                if incorrect == 6:
                    screen.blit(over,(375,76))
                    screen.blit(retry,(636,76))
                    screen.blit(cancel,(636,199))
            else:
                while x in word:
                    i = word.index(x)
                    text = font.render(word[i], True, (0,0,0))
                    screen.blit(text, (200 + i*64, 400))
                    word[i] = None
                    correct+=1
                    if correct ==  len(word):
                        word, correct, incorrect = reset()
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN and incorrect == 6:
            pos = pygame.mouse.get_pos()
            if pos[0] >=636 and pos[0] <=759:
                if pos[1] >= 76 and pos[1] <= 195:
                    word, correct, incorrect = reset()
                elif pos[1] >= 199 and pos[1] <= 322:
                    pygame.quit()
                    exit()