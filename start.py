import os
import time
import pygame

DEBUG = True
BUTTON_DEBOUNCE_TIME = 0.2 # 0.2 Sekunden Entprellzeit für den Button

# Color Scheme
pink = (255,67,238)
yellow = (238,255,67)
blue = (67,238,255)
magenta = (255,67,144)
violette = (178,67,255)

background_color = blue

global screen
global players
global players_team_1
global players_team_2
global current_player_team_1
global current_player_team_2
global debug_font
game_status = "welcome"
screen_width = 1024
screen_height = 768

x_team_1 = 200
x_team_2 = 700
y_start = 300
y_dist = 70


def main():
    print("start")
    global players
    global players_team_1
    global players_team_2
    global current_player_team_1
    global current_player_team_2

    players = [Player(1, [], (x_team_1, y_start + 0 * y_dist)),
               Player(2, [], (x_team_1, y_start + 1 * y_dist)),
               Player(3, [], (x_team_1, y_start + 2 * y_dist)),
               Player(4, [], (x_team_1, y_start + 3 * y_dist)),
               Player(5, [], (x_team_1, y_start + 4 * y_dist)),
               Player(6, [], (x_team_2, y_start + 0 * y_dist)),
               Player(7, [], (x_team_2, y_start + 1 * y_dist)),
               Player(8, [], (x_team_2, y_start + 2 * y_dist)),
               Player(9, [], (x_team_2, y_start + 3 * y_dist)),
               Player(0, [], (x_team_2, y_start + 4 * y_dist))]

    players_team_1 = [players[0],
                      players[1],
                      players[2],
                      players[3],
                      players[4]]

    current_player_team_1 = 0

    players_team_2 = [players[5],
                      players[6],
                      players[7],
                      players[8],
                      players[9]]

    current_player_team_2 = 0
    Game()


def Game():
    global screen
    global players
    global players_team_1
    global players_team_2
    global current_player_team_1
    global current_player_team_2
    global screen_width
    global screen_height
    global debug_font
    global game_status

    pygame.init()
    pygame.font.init()

    debug_font = pygame.font.SysFont('Arial', 20)
    timer_Font = pygame.font.SysFont('Arial', 50)

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    done = False


    # load graphics
    print('loading graphics')
    beer = pygame.image.load(os.path.join('images', 'beer-mug_1f37a.png'))


    while not done:

        # Evemts
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif game_status == "welcome":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_status = "start"

            elif game_status == "going":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_status = "stopping"
                    elif event.key == pygame.K_0 and players[0].status == "start":
                        players[0].status = "done"
                        players[0].stop_time = time.time()
                    elif event.key == pygame.K_1 and players[1].status == "start":
                        players[1].status = "done"
                        players[1].stop_time = time.time()
                    elif event.key == pygame.K_2 and players[2].status == "start":
                        players[2].status = "done"
                        players[2].stop_time = time.time()
                    elif event.key == pygame.K_3 and players[3].status == "start":
                        players[3].status = "done"
                        players[3].stop_time = time.time()
                    elif event.key == pygame.K_4 and players[4].status == "start":
                        players[4].status = "done"
                        players[4].stop_time = time.time()
                    elif event.key == pygame.K_5 and players[5].status == "start":
                        players[5].status = "done"
                        players[5].stop_time = time.time()
                    elif event.key == pygame.K_6 and players[6].status == "start":
                        players[6].status = "done"
                        players[6].stop_time = time.time()
                    elif event.key == pygame.K_7 and players[7].status == "start":
                        players[7].status = "done"
                        players[7].stop_time = time.time()
                    elif event.key == pygame.K_8 and players[8].status == "start":
                        players[8].status = "done"
                        players[8].stop_time = time.time()
                    elif event.key == pygame.K_9 and players[9].status == "start":
                        players[9].status = "done"
                        players[9].stop_time = time.time()


        screen.fill(background_color)


        if game_status == "welcome":
            screen.blit(beer, (0,0))

        for player in players:
            player.show_player()

        if game_status == "start":
            game_start_time = time.time()
            game_status = "going"
            players_team_1[current_player_team_1].status = "start"
            players_team_1[current_player_team_1].start_time = time.time()
            players_team_2[current_player_team_2].status = "start"
            players_team_2[current_player_team_2].start_time = time.time()

        if game_status == "going":
            current_time = time.time()
            screen_time = timer_Font.render("{:03.3f}".format(current_time - game_start_time), True, (0, 0, 0))
            screen.blit(screen_time, (screen_width / 2, screen_height * 0.1))

            if current_player_team_1 < len(players_team_1):
                if players_team_1[current_player_team_1].status == "done":
                    current_player_team_1 += 1
                    if current_player_team_1 < len(players_team_1):
                        players_team_1[current_player_team_1].status = "start"
                        players_team_1[current_player_team_1].start_time = time.time()
            else:
                print("Team 1 ist fertig")
                # Todo: Team 1 ist fertig, was passiert jetzt?

            if current_player_team_2 < len(players_team_2):
                if players_team_2[current_player_team_2].status == "done":
                    current_player_team_2 += 1
                    if current_player_team_2 < len(players_team_2):
                        players_team_2[current_player_team_2].status = "start"
                        players_team_2[current_player_team_2].start_time = time.time()
            else:
                print("Team 2 ist fertig")
                # Todo: Team 2 ist dertig, was passiert jetzt?

                current_player_team_2 += 1

        if game_status == "stopping":
            game_end_time = time.time()
            game_status = "stop"

        if game_status == "stop":
            screen_time = timer_Font.render("{:03.3f}".format(game_end_time - game_start_time), True, (0, 0, 0))
            screen.blit(screen_time, (screen_width / 2, screen_height * 0.1))

        for player in players:
            player.status


        # Game Status
        if DEBUG:
            screen_game_status = debug_font.render("Game Status: " + game_status, True, (0,0,0))
            screen.blit(screen_game_status, (0,0))

        pygame.display.flip()
        clock.tick(100)


class Player():
    def __init__(self, button_pin, LED_list, x_y_pos):
        print('player created')
        self.status = "stop"
        self.LED_status = "stop"
        self.button_pin = button_pin
        self.LED_list = LED_list
        self.LED_color = violette
        self.last_button_press_time = -1

        self.x_pos, self.y_pos = x_y_pos
        self.x_y_pos = x_y_pos

        self.start_time = 0
        self.stop_time = 0

        self.smiley_yawning = pygame.image.load(os.path.join('images', 'smiley_yawning.png'))
        self.drooling_face = pygame.image.load(os.path.join('images', 'drooling_face.png'))

    def show_player(self):
        if self.status == "stop":
            self.LED_color = violette
        if self.status == "start":
            self.LED_color = magenta
        if self.status == "done":
            self.LED_color = (200, 200, 200)
        if DEBUG:
            if self.status == "start" and game_status != "stop":
                self.stop_time = time.time()
            screen_player_status = debug_font.render(self.status +
                                                     "({:3.3f}s)".format(self.stop_time- self.start_time)
                                                     , True, (0, 0, 0))
            screen.blit(screen_player_status, (self.x_pos + 30, self.y_pos - 10))

        #pygame.draw.circle(screen, self.LED_color, self.x_y_pos, 20)

        screen.blit(pygame.transform.scale(self.drooling_face, (60, 60)), self.x_y_pos)



if __name__ == "__main__":
    main()
