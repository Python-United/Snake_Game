import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
# playlist = list()
# playlist.append('Sound/Play_ground3.mp3')
# playlist.append('Sound/Play_ground.mp3')
# playlist.append('Sound/Play_ground2.mp3')


snake_color_list=['blue','black','grey','green','light-blue','orange','red','yellow','purple','brown','brown']

snake_color = snake_color_list[0]
#
# pygame.mixer.music.load(playlist[0])
# pygame.mixer.music.queue(playlist[1])
# pygame.mixer.music.set_endevent(pygame.USEREVENT)
# pygame.mixer.music.play()
# pygame.mixer.music.set_volume(.1)
font = pygame.font.Font('Font/Astral Groove.ttf', 25)
#font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 40

cell_number = 20
SPEED = 80

class SnakeGameAI:

    def __init__(self, w=800, h=800):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((cell_number * BLOCK_SIZE, cell_number * BLOCK_SIZE))


        background_img = pygame.image.load(f'Graphics/background/ground4.png').convert_alpha()
        background = pygame.transform.scale(background_img, (20 * 40, 20 * 40))
        background_rect = pygame.Rect(0, 0, 40, 40)
        self.display.blit(background, background_rect)
        s = pygame.Surface((20 * 40, 40 * 2), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        self.display.blit(s, (0, 0))

        pygame.display.set_caption('United_Python')
        self.clock = pygame.time.Clock()
        self.reset()
        self.fruit = None
        self.fruit_pic = pygame.image.load(f'Graphics/Fruits/green_apple.png').convert_alpha()
        self.posion = pygame.image.load('Graphics/Fruits/polsen_apple.png').convert_alpha()

    def draw_grass(self):
        background_img = pygame.image.load(f'Graphics/background/ground4.png').convert_alpha()
        background = pygame.transform.scale(background_img, (20 * 40, 20 * 40))
        background_rect = pygame.Rect(0, 0, 40, 40)
        self.display.blit(background, background_rect)
        s = pygame.Surface((20 * 40, 44 * 2), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        self.display.blit(s, (0, 0))


    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food_posion()
        self._place_food()
        self.frame_iteration = 0


    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE-1 )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(4, (self.h-BLOCK_SIZE-1 )//BLOCK_SIZE )*BLOCK_SIZE
        fruit_list = ['apricot.png', 'banana.png', 'green_apple.png', 'mango.png', 'red_apple.png', 'strawberry.png']
        self.fruit = fruit_list[random.randint(0, 5)]
        self.fruit_pic = pygame.image.load(f'Graphics/Fruits/{self.fruit}').convert_alpha()
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def _place_food_posion(self):
        x = random.randint(0, (self.w-BLOCK_SIZE-1 )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(4, (self.h-BLOCK_SIZE-1 )//BLOCK_SIZE )*BLOCK_SIZE


        self.posion = pygame.image.load('Graphics/Fruits/polsen_apple.png').convert_alpha()
        self.food2 = Point(x, y)
        if self.food2 in self.snake or self.food == self.food2:
            self._place_food_posion()




    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. move
        self._move(action) # update the head
        self.snake.insert(0, self.head)

        # 3. check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):

            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. place new food or just move

        if self.head == self.food:

            if self.fruit == 'banana.png':

                self.score += 10
            else:
                self.score += 5
            reward = 10
            self._place_food()
            self._place_food_posion()

        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.score


    def is_collision(self, pt=None):

        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y <80 or self.head==self.food2:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False

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
        self.body_horizontal = pygame.image.load(
            f'Graphics/Snake_color/{snake_color}/body_horizontal.png').convert_alpha()
        self.body_tr = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(f'Graphics/Snake_color/{snake_color}/body_bl.png').convert_alpha()

    def _update_ui(self):
        self.display.fill(BLACK)
        self.draw_grass()

        self.levels(self.score)

        for pt in self.snake:
            block_rect = pygame.Rect(pt.x, pt.y, 40, 40)

            logo=pygame.image.load(f'Graphics/Snake_color/green/body_horizontal.png').convert_alpha()
            logo = pygame.transform.scale(logo, (40, 55))



            self.display.blit(logo, block_rect)

            # pygame.draw.rect(self.display, pygame.image.load(f'Graphics/Snake_color/black/body_bl.png').convert_alpha(), pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            # pygame.draw.rect(self.display, pygame.image.load(f'Graphics/Snake_color/black/body_bl.png').convert_alpha(), pygame.Rect(pt.x+4, pt.y+4, 12, 12))





















        fruit_rect = pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE)
        self.display.blit(self.fruit_pic, fruit_rect)
        poisin_rect = pygame.Rect(self.food2.x, self.food2.y, BLOCK_SIZE, BLOCK_SIZE)
        self.display.blit(self.posion, poisin_rect)

        # pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        fruit_score = pygame.image.load('Graphics/Fruits/fruits.png').convert_alpha()
        score_surface = font.render(str(self.score), True, (200, 200, 200))
        score_x = int(2.3 * 40)
        score_y = int(40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        fruit_score_rect = fruit_score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(fruit_score_rect.left, fruit_score_rect.top,
                              fruit_score_rect.width + score_rect.width + 6,
                              fruit_score_rect.height)
        self.display.blit(score_surface, score_rect)
        self.display.blit(fruit_score, fruit_score_rect)

        # text = font.render("Score: " + str(self.score), True, WHITE)
        # self.display.blit(text, [0, 0])
        pygame.display.flip()


    def _move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)


    def levels(self,value):


        if True:
            if value <= 50:
               self.show_level_once('1')

            elif 50 < value <= 100:
                self.show_level_once('2')

            elif 100 < value <= 150:
                self.show_level_once('3')

            elif 150 < value <= 200:
                self.show_level_once('4')

            elif 200 < value <= 250:
                self.show_level_once('5')

            elif 250 < value <= 300:
                self.show_level_once('6')

            elif 300 < value <= 350:
                self.show_level_once('7')

            elif 350 < value <= 400:
                self.show_level_once('8')

            elif 400 < value <= 450:
                self.show_level_once('9')

            elif 450 < value < 500:
                self.show_level_once('10')






    def show_level_once(self,value):

        # global level_name
        # if value!=level_name and value!='1':
        #     self.level_up_sound.set_volume(0.2)
        #     self.level_up_sound.play()
        level_img = pygame.image.load(f'Graphics/levels/level_{value}.jpg').convert_alpha()
        level_img = pygame.transform.scale(level_img, (50, 65))
        level_rect = pygame.Rect(9*BLOCK_SIZE, BLOCK_SIZE*0.1, BLOCK_SIZE, BLOCK_SIZE)
        self.display.blit(level_img, level_rect)
        level_name = value

