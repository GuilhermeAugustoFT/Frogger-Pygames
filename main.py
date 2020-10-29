from typing import Type
import pygame


class Player:

    def __init__(self):
        self.xPlayer = w / 2
        self.yPlayer = 570

    def move(self, pressed):
        global yB
        global yB2
        if pressed[pygame.K_UP]:
            self.yPlayer -= 0.7

        elif pressed[pygame.K_DOWN]:
            self.yPlayer += 0.7

        elif pressed[pygame.K_RIGHT]:
            self.xPlayer += 0.7

        elif pressed[pygame.K_LEFT]:
            self.xPlayer -= 0.7

        screen.blit(imgPlayer, (self.xPlayer, self.yPlayer))


class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5

    def move(self):

        if self.y > h:
            self.y -= h

        self.y += 0.2
        if self.x == 490:
            self.x = -self.x + 470

        self.x += self.speed
        screen.blit(imgCar, (self.x, self.y))

    def intersects(self, xPlayer, yPlayer):
        if (yPlayer <= self.y + 15) and (yPlayer >= self.y - 15):
            if (xPlayer >= self.x - 4) and (xPlayer <= self.x + 4):
                return True


background = pygame.image.load("background.png")
background_size = background.get_size()
w, h = background_size
screen = pygame.display.set_mode((w, h))
yB = 0
yB2 = 0 - h

done = False
pygame.init()
pygame.display.set_caption("Frogger Game")
pygame.display.update()

## Player
imgPlayer = pygame.image.load("player.png")
player = Player()

## Car
imgCar = pygame.image.load("car.png")
cars = []


def initialize_cars():
    global cars
    carsAux = []
    x = 0
    ## Linha 1
    for i in range(0, 16):
        x += 120
        carsAux.append(Car(x, 493))

    x = 0

    ## Linha 2
    for i in range(0, 16):
        x += 150
        carsAux.append(Car(x, 449))

    x = 0

    ## Linha 3
    for i in range(0, 16):
        x += 180
        carsAux.append(Car(x, 358))

    x = 0

    ## Linha 4
    for i in range(0, 16):
        x += 140
        carsAux.append(Car(x, 398))

    cars = carsAux


def is_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True


def menu():
    global state
    global player
    player = Player()
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 40)
    title = font.render('Frogger Game', True, red)
    font = pygame.font.Font('freesansbold.ttf', 20)
    sub_title = font.render('Press g for play!', True, red)
    font = pygame.font.Font('freesansbold.ttf', 18)
    instructions_txt = font.render('Press i for instructions', True, red)
    tr_title = title.get_rect()
    tr_sub_title = sub_title.get_rect()
    tr_instructions = instructions_txt.get_rect()
    tr_title.center = (w // 2, h // 2 - 50)
    tr_sub_title.center = (w // 2, h // 2)
    tr_instructions.center = (w // 2, h // 2 + 150)
    screen.blit(title, tr_title)
    screen.blit(sub_title, tr_sub_title)
    screen.blit(instructions_txt, tr_instructions)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_g]:
        state = 1
        return

    if pressed[pygame.K_i]:
        state = 3
        return

    if is_quit():
        state = -1
        return

    pygame.display.update()


def instructions():
    global state
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text_instructions1 = font.render('-> Use the arrows to move', True, red)
    text_instructions2 = font.render('-> Use p to pause the game', True, red)
    font = pygame.font.Font('freesansbold.ttf', 18)
    text_exit = font.render('Press m to back to menu', True, red)
    tr_text1 = text_instructions1.get_rect()
    tr_text2 = text_instructions2.get_rect()
    tr_exit = text_exit.get_rect()
    tr_text1.center = (w // 2, h // 2 - 50)
    tr_text2.center = (w // 2, h // 2)
    tr_exit.center = (w // 2, h // 2 + 120)
    screen.blit(text_instructions1, tr_text1)
    screen.blit(text_instructions2, tr_text2)
    screen.blit(text_exit, tr_exit)

    pressed = pygame.key.get_pressed()

    if is_quit():
        state = -1
        return

    if pressed[pygame.K_m]:
        state = 2
        return

    pygame.display.update()


def pause():
    global state
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 40)
    text_instructions = font.render('Pause', True, red)
    font = pygame.font.Font('freesansbold.ttf', 18)
    text_exit = font.render('Press esc for back to game', True, red)
    tr_text = text_instructions.get_rect()
    tr_exit = text_exit.get_rect()
    tr_text.center = (w // 2, h // 2 - 50)
    tr_exit.center = (w // 2, h // 2 + 80)
    screen.blit(text_instructions, tr_text)
    screen.blit(text_exit, tr_exit)

    pressed = pygame.key.get_pressed()

    if is_quit():
        state = -1
        return

    if pressed[pygame.K_m]:
        state = 2
        return

    if pressed[pygame.K_ESCAPE]:
        state = 1
        return

    pygame.display.update()


def update_game():
    global state
    global yB
    global yB2
    yB = 0
    yB2 = 0 - h
    initialize_cars()
    while state == 1:
        if is_quit():
            state = -1
            break

        if yB2 > 0:
            yB = 0
            yB2 = 0 - h

        screen.blit(background, (0, yB2))
        key = pygame.key.get_pressed()
        screen.blit(background, (0, yB))
        player.move(key)
        yB += 0.2
        yB2 += 0.2
        player.yPlayer += 0.2

        if player.yPlayer > h:
            state = 0
            return

        for car in cars:
            car.move()

            if car.intersects(player.xPlayer, player.yPlayer):
                state = 0

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_p]:
            state = 4
            return

        pygame.display.update()


def game_over():
    global state
    global player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = -1
            return
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render('You lose!', True, red)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text2 = font.render('Press c to play again or m for go to menu', True, red)
    text_rect = text.get_rect()
    text_rect2 = text2.get_rect()
    text_rect.center = (w // 2, h // 2 - 50)
    text_rect2.center = (w // 2, h // 2 + 50)
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)
    pressed = pygame.key.get_pressed()

    if is_quit():
        state = -1
        return

    if pressed[pygame.K_c]:
        state = 1
        player = Player()
        return

    if pressed[pygame.K_m]:
        state = 2
        return

    pygame.display.update()


def finish():
    global done
    done = True


state = 2

while not done:
    if state == 4:
        pause()
    if state == 2:
        menu()
    elif state == 3:
        instructions()
    elif state == 1:
        update_game()
    elif state == 0:
        game_over()
    elif state == -1:
        finish()
