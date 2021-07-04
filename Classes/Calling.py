
from Classes.Bases import *
from Classes.Main import *

def sound_background(flag,page):
    global  stop_reassgin_background_music
    if flag != stop_reassgin_background_music and page=='main_minue':
        pygame.mixer.music.load('Sound/StartWindow.wav')
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(0.2)
        stop_reassgin_background_music=flag
    elif flag != stop_reassgin_background_music and page=='play_ground':
        stop_reassgin_background_music = flag
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.queue(playlist[1])
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.mixer.music.play()
    elif flag != stop_reassgin_background_music and page == 'win_ground':
        stop_reassgin_background_music = flag
        pygame.mixer.music.load('Sound/Win_ground.mp3')
        pygame.mixer.music.play()
    elif flag != stop_reassgin_background_music and page == 'game_over':
        stop_reassgin_background_music = flag
        pygame.mixer.music.load('Sound/game_over.mp3')
        pygame.mixer.music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.USEREVENT:  # A track has ended
            if len(playlist) > 0 and main_game.play:
                temp=playlist.pop(0)
                pygame.mixer.music.queue(temp)
                playlist.append(temp)
        if event.type == SCREEN_UPDATE2:
            main_game.fruit.draw_fruit_po()
            main_game.fruit.randomize_po()
            main_game.fruit.randomize_po2()
            main_game.fruit.randomize_po3()
            main_game.fruit.randomize_po4()
            main_game.fruit.randomize_po5()
            main_game.fruit.randomize_po6()
            main_game.fruit.randomize_po7()
            main_game.fruit.randomize_po8()
            main_game.fruit.randomize_po9()
            main_game.fruit.randomize_po10()
        if main_game.play==True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
        else:
            mousePosition = pygame.mouse.get_pos()
            if main_game.main_minue_dialog == 1 :
                if 313 <= mousePosition[0] <= 509 and 563 <= mousePosition[1] <= 654:
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                elif 371<=mousePosition[0]<=445 and 462<=mousePosition[1]<=509 :
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
            elif main_game.main_minue_dialog == 4 :
                if 71 <= mousePosition[0] <= 130 and 682 <= mousePosition[1] <= 731:
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
            elif main_game.main_minue_dialog == 3:
                if 71 <= mousePosition[0] <= 130 and 682 <= mousePosition[1] <= 731:
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                elif 313 <= mousePosition[0] <= 509 and 563 <= mousePosition[1] <= 654:
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)


            if event.type == MOUSEBUTTONDOWN:

                if event.button == 1 and main_game.main_minue_dialog == 1:
                    if 313<=mousePosition[0]<=509 and 563<=mousePosition[1]<=654:
                        main_game.main_minue_dialog = 0
                        main_game.play=True
                    elif 371<=mousePosition[0]<=445 and 462<=mousePosition[1]<=509 and main_game.main_minue_dialog == 1:
                        main_game.main_minue_dialog = 4

                elif event.button == 1 and main_game.main_minue_dialog == 4:
                    if 71 <= mousePosition[0] <= 130 and 682 <= mousePosition[1] <= 731:
                        main_game.main_minue_dialog = 1
                elif event.button == 1 and main_game.main_minue_dialog == 3:

                    if 71 <= mousePosition[0] <= 130 and 682 <= mousePosition[1] <= 731:
                        main_game.main_minue_dialog = 1
                    elif 313<=mousePosition[0]<=509 and 563<=mousePosition[1]<=654:
                        main_game.main_minue_dialog = 0
                        main_game.play=True




    screen.fill((240,240,240))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
