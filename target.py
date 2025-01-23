import pygame
import sys
import math
import random

pygame.init()
x_val = 1000
y_val = 500
screen = pygame.display.set_mode((x_val,y_val))
font = pygame.font.Font(None, 30)
font_large = pygame.font.Font(None, 100)
score = 0
miss_or_hit = ''
game_state = "playing"

circle_pos = (x_val/2, y_val/2)

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1]- circle_pos[1])**2)<= 50:
        return True
    return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_state == "playing":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left click
                    if check_circle_collision():
                        score += 1
                        circle_pos = (random.randint(0,x_val),random.randint(0,y_val))
                        miss_or_hit = 'HIT'
                    else:
                        score -= 1
                        circle_pos = (random.randint(0,x_val),random.randint(0,y_val))
                        miss_or_hit = 'MISS'
            if score == 10:
                game_state = "win"
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
    if game_state == "playing":
        score_sur = font.render(f'Score: {score}', True, "black") #this is a surface, must be displayed
        word_sur = font.render(f'{miss_or_hit}',True, "black")

        screen.fill('lightpink') #everything underneath is shown on top 
        pygame.draw.circle(screen, "red", circle_pos, 50)
        screen.blit(score_sur, (50, 50))  # Keep score at the top-left corner
        screen.blit(word_sur, (50, 80))  # Move hit/miss text slightly below the score
    else:
        win_text = font_large.render('YOU WIN!!', True, "black")
        win_text2 = font.render('click anywhere to exit', True, "black")
        screen.fill('lightpink')
        screen.blit(win_text, (x_val / 2 - win_text.get_width() / 2, y_val / 2 - win_text.get_height() / 2))
        screen.blit(win_text2, (x_val / 2 - win_text2.get_width() / 2, (y_val / 2 - win_text2.get_height() / 2)+50))

   
    pygame.display.update()
    