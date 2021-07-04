from Classes.Fruit import FRUIT
from Classes.Snake import SNAKE
from Classes.Bases import *

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