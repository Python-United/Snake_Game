import pygame, sys, random
from pygame.math import Vector2
from pygame.locals import *
import moviepy.editor as mp

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
        self.losing_sound = pygame.mixer.Sound('Sound/losing.wav')

    def color_snake(self):

        global snake_color
        self.head_up = pygame.image.load(f'Graphics/Snake_color/{snake_color}/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(f'Graphics/Snake_color/{snake_color}/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(f'Graphics/Snake_color/{snake_color}/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(f'Graphics/Snake_color/{snake_color}/head_left.png').convert_alpha()
        self.tail_up = pygame.image.load(f'Graphics/Snake_color/{snake_color}/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(f'Graphics/Snake_color/{snake_color}/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(f'Graphics/Snake_color/{snake_color}/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(f'Graphics/Snake_color/{snake_color}/tail_left.png').convert_alpha()
        self.body_vertical = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_horizontal.png').convert_alpha()
        self.body_tr = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_bl.png').convert_alpha()

    def draw_snake(self):

        self.color_snake()
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def play_losing_sound(self):
        if main_game.main_minue_dialog == 2:
            self.losing_sound.set_volume(0)
        else:
            self.losing_sound.set_volume(0.2)
        self.losing_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()
        self.randomize_po()
        self.randomize_po2()
        self.randomize_po3()
        self.randomize_po4()
        self.randomize_po5()
        self.randomize_po6()
        self.randomize_po7()
        self.randomize_po8()
        self.randomize_po9()
        self.randomize_po10()
        self.fruit=None
        self.fruit_pic=pygame.image.load(f'Graphics/Fruits/green_apple.png').convert_alpha()
        self.posion=pygame.image.load('Graphics/Fruits/polsen_apple.png').convert_alpha()



    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.fruit_pic, fruit_rect)



    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(2, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        fruit_list = ['apricot.png', 'banana.png', 'green_apple.png', 'mango.png', 'red_apple.png', 'strawberry.png']
        self.fruit = fruit_list[random.randint(0, 5)]
        self.fruit_pic = pygame.image.load(f'Graphics/Fruits/{self.fruit}').convert_alpha()

    def draw_fruit_po(self):
        global pn
        if pn==1 or pn==2 or pn==3 or pn==4 or pn==5 or pn==6 or pn==7 or pn==8 or pn==9 or pn==10:
            fruit_rect2 = pygame.Rect(int(self.pos2.x * cell_size), int(self.pos2.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect2)
        if pn == 2 or pn == 3 or pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect3 = pygame.Rect(int(self.pos3.x * cell_size), int(self.pos3.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect3)
        if pn == 3 or pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect4 = pygame.Rect(int(self.pos4.x * cell_size), int(self.pos4.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect4)
        if pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect5 = pygame.Rect(int(self.pos5.x * cell_size), int(self.pos5.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect5)
        if pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect6 = pygame.Rect(int(self.pos6.x * cell_size), int(self.pos6.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect6)
        if pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect7 = pygame.Rect(int(self.pos7.x * cell_size), int(self.pos7.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect7)
        if pn == 7 or pn == 8 or pn == 9 or pn == 10:
            fruit_rect8 = pygame.Rect(int(self.pos8.x * cell_size), int(self.pos8.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect8)
        if pn == 8 or pn == 9 or pn == 10:
            fruit_rect9 = pygame.Rect(int(self.pos9.x * cell_size), int(self.pos9.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect9)
        if pn == 9 or pn == 10:
            fruit_rect10 = pygame.Rect(int(self.pos10.x * cell_size), int(self.pos10.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect10)
        if pn == 10:
            fruit_rect11 = pygame.Rect(int(self.pos11.x * cell_size), int(self.pos11.y * cell_size), cell_size, cell_size)
            screen.blit(self.posion, fruit_rect11)

    def randomize_po(self):
        self.x2 = random.randint(0, cell_number - 1)
        self.y2 = random.randint(2, cell_number - 1)
        self.pos2 = Vector2(self.x2, self.y2)

    def randomize_po2(self):
        self.x3 = random.randint(0, cell_number - 1)
        self.y3 = random.randint(2, cell_number - 1)
        self.pos3 = Vector2(self.x3, self.y3)

    def randomize_po3(self):
        self.x4 = random.randint(0, cell_number - 1)
        self.y4 = random.randint(2, cell_number - 1)
        self.pos4 = Vector2(self.x4, self.y4)

    def randomize_po4(self):
        self.x5 = random.randint(0, cell_number - 1)
        self.y5 = random.randint(2, cell_number - 1)
        self.pos5 = Vector2(self.x5, self.y5)

    def randomize_po5(self):
        self.x6 = random.randint(0, cell_number - 1)
        self.y6 = random.randint(2, cell_number - 1)
        self.pos6 = Vector2(self.x6, self.y6)

    def randomize_po6(self):
        self.x7 = random.randint(0, cell_number - 1)
        self.y7 = random.randint(2, cell_number - 1)
        self.pos7 = Vector2(self.x7, self.y7)

    def randomize_po7(self):
        self.x8 = random.randint(0, cell_number - 1)
        self.y8 = random.randint(2, cell_number - 1)
        self.pos8 = Vector2(self.x8, self.y8)

    def randomize_po8(self):
        self.x9 = random.randint(0, cell_number - 1)
        self.y9 = random.randint(2, cell_number - 1)
        self.pos9 = Vector2(self.x9, self.y9)

    def randomize_po9(self):
        self.x10 = random.randint(0, cell_number - 1)
        self.y10 = random.randint(2, cell_number - 1)
        self.pos10 = Vector2(self.x10, self.y10)

    def randomize_po10(self):
        self.x11 = random.randint(0, cell_number - 1)
        self.y11 = random.randint(2, cell_number - 1)
        self.pos11 = Vector2(self.x11, self.y11)
