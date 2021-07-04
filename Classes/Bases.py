random_number=random.randint(0, 9)
snake_color_list=['blue','black','grey','green','light-blue','orange','red','yellow','purple','brown','brown']
primary_board_color=[(175, 215, 70),(200, 188, 177),(67, 31, 29),(250, 183, 61),(45, 6, 37),(244, 215, 94),(195, 49, 36),(211, 220, 200),(192, 4, 123),(120, 63, 4)]
secondary_board_color=[(167, 209, 61),(228, 218, 207),(144, 88, 75),(253, 220, 165),(33, 65, 12),(153, 41, 21),(110, 5, 22),(175, 202, 84),(255, 6, 89),(120, 63, 4)]
pn = 0
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
score = 0
level_name = 'level 1'
snake_color = snake_color_list[0]
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption('United - Snake Game')
clock = pygame.time.Clock()
fruit_score = pygame.image.load('Graphics/Fruits/fruits.png').convert_alpha()
game_font = pygame.font.Font('Font/Astral Groove.ttf', 20)
rules_font = pygame.font.Font('Font/Astral Groove.ttf', 10)
point_font = pygame.font.Font('Font/Space Rave.ttf', 30)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
SCREEN_UPDATE2 = pygame.USEREVENT+1
pygame.time.set_timer(SCREEN_UPDATE2, 4000)
main_game = MAIN()
stop_reassgin_background_music=False
play_intro=True
playlist = list()
playlist.append('Sound/Play_ground3.mp3')
playlist.append('Sound/Play_ground.mp3')
playlist.append('Sound/Play_ground2.mp3')