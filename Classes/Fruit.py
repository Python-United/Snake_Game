from Classes.Bases import *
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




