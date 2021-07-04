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


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.main_minue_dialog=1
        self.play = False
        self.level_up_sound = pygame.mixer.Sound('Sound/next_level.mp3')



    def main_minue(self):
        global play_intro
        if play_intro:
            self.intro_vedio()
        sound_background(True,'main_minue')
        grass_color = (149, 53, 83)
        grass_rect = pygame.Rect(0, 0, 40*20, 40*20)
        pygame.draw.rect(screen, grass_color, grass_rect)
        # score_text = str('Welcome to Snake Game')
        score_text = str('WELCOME TO SNAKE GAME')
        score_surface = game_font.render(score_text, True, 	(255, 164, 94))
        score_x = int(cell_size/2 * cell_number)
        score_y = int(3 * cell_number)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)
        logo = pygame.image.load('Graphics/logo.png').convert_alpha()
        logo = pygame.transform.scale(logo, (150, 150))
        logo_rect = pygame.Rect(int(8.5 * cell_size), int(5.5 * cell_size), cell_size, cell_size)
        screen.blit(logo, logo_rect)
        button_setting = pygame.image.load('Graphics/playing.png').convert_alpha()
        button_setting = pygame.transform.scale(button_setting, (200, 100))
        logo_rect_button_setting = pygame.Rect(int(cell_size * (cell_number-12.2)), int(cell_size * (cell_number-6)), 50,50)
        screen.blit(button_setting, logo_rect_button_setting)

        rules = pygame.image.load('Graphics/rules.png').convert_alpha()
        rules = pygame.transform.scale(rules, (30, 30))
        rules_rect = pygame.Rect(int(cell_size * (cell_number-10.2)), int(cell_size * (cell_number-8.5)), 50,50)
        screen.blit(rules, rules_rect)

        rules_text = str('RULES')
        rules_surface = rules_font.render(rules_text, True, 	(255, 164, 94))
        rules_x = int(cell_size / 2 * cell_number+9)
        rules_y = int(25.1 * cell_number)
        rules_rect = rules_surface.get_rect(center=(rules_x, rules_y))
        screen.blit(rules_surface, rules_rect)




    def intro_vedio(self):
        clip = mp.VideoFileClip('Graphics/Intro/1212.mp4')
        clip.preview()
        global play_intro
        play_intro=False



    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()


    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.fruit.draw_fruit_po()
        global snake_color
        global pn
        snake_color = snake_color_list[int(pn)]
        self.snake.draw_snake()
        self.draw_score()
        if self.main_minue_dialog == 1:
            self.main_minue()
        elif self.main_minue_dialog == 0:
            sound_background(False, 'play_ground')
        elif self.main_minue_dialog == 2:
            self.win_minue()

        if self.main_minue_dialog==3:
            self.game_over_page()

        if self.main_minue_dialog==4:
            self.rules_page()



    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            if self.fruit.fruit == 'banana.png':
                global score
                score += 10
            else:
                score += 5
                self.snake.add_block()
            self.fruit.randomize()
            self.snake.play_crunch_sound()
        if self.fruit.pos2 == self.snake.body[0]:
            if score!=0 and score-10>=0:
                score -= 10
            elif score - 10 <0:
                self.game_over()
            self.snake.play_losing_sound()
            self.fruit.randomize_po()
            self.snake.add_block()

        if pn == 2 or pn == 3 or pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos3 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po2()
                self.snake.add_block()
        if pn == 3 or pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos4 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po3()
                self.snake.add_block()
        if pn == 4 or pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos5 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po4()
                self.snake.add_block()
        if pn == 5 or pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos6 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po5()
                self.snake.add_block()
        if pn == 6 or pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos7 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po6()
                self.snake.add_block()
        if pn == 7 or pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos8 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po7()
                self.snake.add_block()
        if pn == 8 or pn == 9 or pn == 10:
            if self.fruit.pos9 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po8()
                self.snake.add_block()
        if pn == 9 or pn == 10:
            if self.fruit.pos10 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po9()
                self.snake.add_block()
        if pn == 10:
            if self.fruit.pos11 == self.snake.body[0]:
                if score != 0 and score - 10 >= 0:
                    score -= 10
                self.snake.play_losing_sound()
                self.fruit.randomize_po10()
                self.snake.add_block()

        pos_list=[self.fruit.pos2,self.fruit.pos3,self.fruit.pos4,self.fruit.pos5,self.fruit.pos6,self.fruit.pos7,
                  self.fruit.pos8,self.fruit.pos9,self.fruit.pos10,self.fruit.pos11]

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        for i in range(len(pos_list)):
            if self.fruit.pos == pos_list[i]:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 2 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                if self.snake.body == [Vector2(5, 10), Vector2(5, 10), Vector2(4, 10)]:
                    self.snake.reset()
                else:

                    self.game_over()


    def game_over(self):
       global score
       score = 0
       self.snake.reset()
       main_game.play = False
       if self.main_minue_dialog != 2:
            self.snake.play_losing_sound()
            self.main_minue_dialog=3



    def game_over_page(self):
        sound_background(True,'game_over')
        background_color = (149, 53, 83)
        background_rect = pygame.Rect(0, 0, 40*20, 40*20)
        pygame.draw.rect(screen, background_color, background_rect)
        score_surface = game_font.render(str('Game Over').upper(), True,(255, 164, 94))
        score_x = int(cell_size/2 * cell_number)
        score_y = int(3 * cell_number)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)
        logo = pygame.image.load('Graphics/logo.png').convert_alpha()
        logo = pygame.transform.scale(logo, (150, 150))
        logo_rect = pygame.Rect(int(8.5 * cell_size), int(5.5 * cell_size), cell_size, cell_size)
        screen.blit(logo, logo_rect)
        button_setting = pygame.image.load('Graphics/playAgain.png').convert_alpha()
        button_setting = pygame.transform.scale(button_setting, (200, 100))
        logo_rect_button_setting = pygame.Rect(int(cell_size * (cell_number-12.2)), int(cell_size * (cell_number-6)), 50,50)
        screen.blit(button_setting, logo_rect_button_setting)

        back = pygame.image.load('Graphics/back.png').convert_alpha()
        back = pygame.transform.scale(back, (50, 50))
        back_rect = pygame.Rect(int(2 * cell_size), int(17 * cell_size), cell_size, cell_size)
        screen.blit(back, back_rect)

        home_text = str('HOME').upper()
        home_surface = rules_font.render(home_text, True, (255, 164, 94))
        score_x = int(4.3 * cell_size)
        score_y = int(35.2 * cell_number)
        home_rect = home_surface.get_rect(center=(score_x, score_y))
        screen.blit(home_surface, home_rect)

    def draw_grass(self):
        number=[1,2,3,4,5,6,7,8,9,10,11]
        background_number = number[pn]
        background_img = pygame.image.load(f'Graphics/background/ground{background_number}.png').convert_alpha()
        background = pygame.transform.scale(background_img, (20*cell_size, 20*cell_size))
        background_rect = pygame.Rect(0, 0, cell_size, cell_size)
        screen.blit(background, background_rect)
        s = pygame.Surface((20*40, cell_size * 2), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        screen.blit(s, (0, 0))

    def draw_score(self):
        if len(self.snake.body)==3:
            score_text = str(score)
            self.levels(score)
        else:
            score_text = str(score)
            self.levels(score)
        score_surface = game_font.render(score_text, True, (200, 200, 200))
        score_x = int(2.3*cell_size)
        score_y = int(cell_size)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        fruit_score_rect = fruit_score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(fruit_score_rect.left, fruit_score_rect.top, fruit_score_rect.width + score_rect.width + 6,
                              fruit_score_rect.height)
        screen.blit(score_surface, score_rect)
        screen.blit(fruit_score, fruit_score_rect)


    def levels(self,value):
        global pn
        if not self.main_minue_dialog == 1:
            if value <= 50:
               self.show_level_once('1')
               pn = 1
            elif 50 < value <= 100:
                self.show_level_once('2')
                pn = 2
            elif 100 < value <= 150:
                self.show_level_once('3')
                pn = 3
            elif 150 < value <= 200:
                self.show_level_once('4')
                pn = 4
            elif 200 < value <= 250:
                self.show_level_once('5')
                pn = 5
            elif 250 < value <= 300:
                self.show_level_once('6')
                pn = 6
            elif 300 < value <= 350:
                self.show_level_once('7')
                pn = 7
            elif 350 < value <= 400:
                self.show_level_once('8')
                pn = 8
            elif 400 < value <= 450:
                self.show_level_once('9')
                pn = 9
            elif 450 < value < 500:
                self.show_level_once('10')
                pn = 10
            else:
                self.main_minue_dialog = 2
                self.play = False

    def win_minue(self):

        sound_background(True,'win_ground')
        background_color = (149, 53, 83)
        background_rect = pygame.Rect(0, 0, 40*20, 40*20)
        pygame.draw.rect(screen, background_color, background_rect)
        score_text = str('Congratulations').upper()
        score_surface = game_font.render(score_text, True, 	(255, 164, 94))
        score_x = int(cell_size/2 * cell_number)
        score_y = int(3 * cell_number)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

        score_text = str('You Completed All Levels').upper()
        score_surface = game_font.render(score_text, True, (255, 164, 94))
        score_x = int(cell_size / 2 * cell_number)
        score_y = int(8 * cell_number)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)


        logo = pygame.image.load('Graphics/logo.png').convert_alpha()
        logo = pygame.transform.scale(logo, (150, 150))
        logo_rect = pygame.Rect(int(8.5 * cell_size), int(5.5 * cell_size), cell_size, cell_size)
        screen.blit(logo, logo_rect)
        button_setting = pygame.image.load('Graphics/playAgain.png').convert_alpha()
        button_setting = pygame.transform.scale(button_setting, (200, 100))
        logo_rect_button_setting = pygame.Rect(int(cell_size * (cell_number-12.2)), int(cell_size * (cell_number-6)), 50,50)
        screen.blit(button_setting, logo_rect_button_setting)



    def show_level_once(self,value):

        global level_name
        if value!=level_name and value!='1':
            self.level_up_sound.set_volume(0.2)
            self.level_up_sound.play()
        level_img = pygame.image.load(f'Graphics/levels/level_{value}.jpg').convert_alpha()
        level_img = pygame.transform.scale(level_img, (50, 65))
        level_rect = pygame.Rect(9*cell_size, cell_size*0.1, cell_size, cell_size)
        screen.blit(level_img, level_rect)
        level_name = value

    def rules_page(self):
        background_color = (149, 53, 83)
        background_rect = pygame.Rect(0, 0, 40 * 20, 40 * 20)
        pygame.draw.rect(screen, background_color, background_rect)

        rules_text = str('RULES').upper()
        rules_surface = game_font.render(rules_text, True, (255, 164, 94))
        score_x = int(cell_size / 2 * cell_number)
        score_y = int(3 * cell_number)
        rules_rect = rules_surface.get_rect(center=(score_x, score_y))
        screen.blit(rules_surface, rules_rect)

        back = pygame.image.load('Graphics/back.png').convert_alpha()
        back = pygame.transform.scale(back, (50, 50))
        back_rect = pygame.Rect(int(2 * cell_size), int(17* cell_size), cell_size, cell_size)
        screen.blit(back, back_rect)

        home_text = str('HOME').upper()
        home_surface = rules_font.render(home_text, True, (255, 164, 94))
        score_x = int(4.3*cell_size)
        score_y = int(35.2* cell_number)
        home_rect = home_surface.get_rect(center=(score_x, score_y))
        screen.blit(home_surface, home_rect)

        apricot = pygame.image.load('Graphics/Fruits/apricot.png').convert_alpha()
        apricot = pygame.transform.scale(apricot, (40, 40))
        apricot_rect = pygame.Rect(int(4 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(apricot, apricot_rect)
        green_apple = pygame.image.load('Graphics/Fruits/green_apple.png').convert_alpha()
        green_apple = pygame.transform.scale(green_apple, (40, 40))
        green_apple_rect = pygame.Rect(int(5 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(green_apple, green_apple_rect)
        red_apple = pygame.image.load('Graphics/Fruits/red_apple.png').convert_alpha()
        red_apple = pygame.transform.scale(red_apple, (40, 40))
        red_apple_rect = pygame.Rect(int(6 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(red_apple, red_apple_rect)
        strawberry = pygame.image.load('Graphics/Fruits/strawberry.png').convert_alpha()
        strawberry = pygame.transform.scale(strawberry, (40, 40))
        strawberry_rect = pygame.Rect(int(7 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(strawberry, strawberry_rect)
        strawberry = pygame.image.load('Graphics/Fruits/strawberry.png').convert_alpha()
        strawberry = pygame.transform.scale(strawberry, (40, 40))
        strawberry_rect = pygame.Rect(int(7 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(strawberry, strawberry_rect)
        mango = pygame.image.load('Graphics/Fruits/mango.png').convert_alpha()
        mango = pygame.transform.scale(mango, (40, 40))
        mango_rect = pygame.Rect(int(8 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(mango, mango_rect)
        right = pygame.image.load('Graphics/right.png').convert_alpha()
        right = pygame.transform.scale(right, (40, 40))
        right_rect = pygame.Rect(int(9.3 * cell_size), int(5 * cell_size), cell_size, cell_size)
        screen.blit(right, right_rect)
        point_text = str('+5').upper()
        point_surface = point_font.render(point_text, True, (255, 164, 94))
        score_x = int(12 * cell_size)
        score_y = int(11 * cell_number)
        point_rect = point_surface.get_rect(center=(score_x, score_y))
        screen.blit(point_surface, point_rect)
        fruit = pygame.image.load('Graphics/Fruits/fruits.png').convert_alpha()
        fruit = pygame.transform.scale(fruit, (50, 50))
        fruit_rect = pygame.Rect(int(13 * cell_size), int(5 * cell_size-10), cell_size, cell_size)
        screen.blit(fruit, fruit_rect)

        polsen_apple = pygame.image.load('Graphics/Fruits/polsen_apple.png').convert_alpha()
        polsen_apple = pygame.transform.scale(polsen_apple, (40, 40))
        polsen_apple_rect = pygame.Rect(int(6 * cell_size), int(7 * cell_size), cell_size, cell_size)
        screen.blit(polsen_apple, polsen_apple_rect)
        right = pygame.image.load('Graphics/right.png').convert_alpha()
        right = pygame.transform.scale(right, (40, 40))
        right_rect = pygame.Rect(int(9.3 * cell_size), int(7 * cell_size), cell_size, cell_size)
        screen.blit(right, right_rect)
        point_text = str('-10').upper()
        point_surface = point_font.render(point_text, True, (255, 164, 94))
        score_x = int(12 * cell_size)
        score_y = int(7.5 * cell_size)
        point_rect = point_surface.get_rect(center=(score_x, score_y))
        screen.blit(point_surface, point_rect)
        fruit = pygame.image.load('Graphics/Fruits/fruits.png').convert_alpha()
        fruit = pygame.transform.scale(fruit, (50, 50))
        fruit_rect = pygame.Rect(int(13 * cell_size), int(7 * cell_size - 10), cell_size, cell_size)
        screen.blit(fruit, fruit_rect)

        banana = pygame.image.load('Graphics/Fruits/banana.png').convert_alpha()
        banana = pygame.transform.scale(banana, (40, 40))
        banana_rect = pygame.Rect(int(6 * cell_size), int(9 * cell_size), cell_size, cell_size)
        screen.blit(banana, banana_rect)
        right = pygame.image.load('Graphics/right.png').convert_alpha()
        right = pygame.transform.scale(right, (40, 40))
        right_rect = pygame.Rect(int(9.3 * cell_size), int(9 * cell_size), cell_size, cell_size)
        screen.blit(right, right_rect)
        point_text = str('+10').upper()
        point_surface = point_font.render(point_text, True, (255, 164, 94))
        score_x = int(12 * cell_size)
        score_y = int(9.5 * cell_size)
        point_rect = point_surface.get_rect(center=(score_x, score_y))
        screen.blit(point_surface, point_rect)
        fruit = pygame.image.load('Graphics/Fruits/fruits.png').convert_alpha()
        fruit = pygame.transform.scale(fruit, (50, 50))
        fruit_rect = pygame.Rect(int(13 * cell_size), int(9 * cell_size - 10), cell_size, cell_size)
        screen.blit(fruit, fruit_rect)

        point_text = str('you need to pass 10 levels to win').upper()
        point_surface = point_font.render(point_text, True, (255, 164, 94))
        score_x = int(10 * cell_size)
        score_y = int(12 * cell_size)
        point_rect = point_surface.get_rect(center=(score_x, score_y))
        screen.blit(point_surface, point_rect)

        point_text = str('each level need 50 points to pass').upper()
        point_surface = point_font.render(point_text, True, (255, 164, 94))
        score_x = int(10 * cell_size)
        score_y = int(14 * cell_size)
        point_rect = point_surface.get_rect(center=(score_x, score_y))
        screen.blit(point_surface, point_rect)
