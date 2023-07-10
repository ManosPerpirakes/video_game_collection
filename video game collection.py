from random import randint
import pygame
pygame.init()

def f1():
    global closeall

    class Enemy():
        def __init__(self, speed, collision):
            self.rect = pygame.rect.Rect(1500, randint(0, 700), 50, 50)
            self.speed = speed
            self.collision = collision
            enemies.append(self)

    try_again = True
    closeapp = False
    while try_again:
        w = pygame.display.set_mode((1500, 750))
        player = pygame.rect.Rect(100, 375, 50, 50)
        enemies = []
        for i in range(5):
            new_enemy = Enemy(randint(5, 10), False)
        close = False
        go_up = False
        go_down = False
        lives = 5
        counter = 0
        score = 0
        clock = pygame.time.Clock()
        font1 = pygame.font.Font(None, 30)
        text1 = font1.render("1-quit", True, (0, 255, 0))
        while True:
            counter += 1
            if counter == 60:
                score += 1
                counter = 0
            w.fill((255, 255, 255))
            pygame.draw.rect(w, (0, 0, 255), player)
            for enemy in enemies:
                pygame.draw.rect(w, (255, 0, 0), enemy.rect)
                enemy.rect.x -= enemy.speed
                if enemy.rect.colliderect(player):
                    if enemy.collision == False:
                        enemy.collision = True
                        lives -= 1
                if enemy.rect.x <= 0:
                    enemy.rect.x = 1500
                    enemy.rect.y = randint(0, 700)
                    enemy.collision = False
                    enemy.speed = randint(10, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closeapp = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        go_up = True
                    if event.key == pygame.K_DOWN:
                        go_down = True
                    if event.key == pygame.K_1:
                        close = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        go_up = False
                    if event.key == pygame.K_DOWN:
                        go_down = False
            if go_up and player.y >= 10:
                player.y -= 10
            if go_down and player.y <= 690:
                player.y += 10
            if lives == 0:
                close = True
            if closeapp:
                close = True
            if close == True:
                break
            w.blit(text1, (1000, 50))
            text2 = font1.render('lives: ' + str(lives), True, (0, 255, 0))
            w.blit(text2, (1000, 80))
            text3 = font1.render("score: " + str(score), True, (0, 255, 0))
            w.blit(text3, (1000, 110))
            pygame.display.update()
            clock.tick(60)
        close = False
        font1 = pygame.font.Font(None, 50)
        text1 = font1.render("game over", True, (0, 255, 0))
        text2 = font1.render("score: " + str(score), True, (0, 255, 0))
        text3 = font1.render("1-try again", True, (0, 255, 0))
        text4 = font1.render("2-exit", True, (0, 255, 0))
        try_again = True
        while True:
            w.fill((255, 255, 255))
            w.blit(text1, (750, 100))
            w.blit(text2, (750, 150))
            w.blit(text3, (750, 200))
            w.blit(text4, (750, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closeapp = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        close = True
                    if event.key == pygame.K_2:
                        close = True
                        try_again = False
            if closeapp:
                close = True
                try_again = False
            if close == True:
                break
            pygame.display.update()
            clock.tick(60)

def f2():
    global closeall
    close = False
    counter5 = True
    while counter5:
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 325, 10, 100)
        r2 = pygame.Rect(1390, 0, 10, 750)
        r3 = pygame.Rect(740, 365, 20, 20)
        r1_move_up = False
        r1_move_down = False
        r3_x_add = 2
        r3_y_add = randint(3, 7)
        font1 = pygame.font.Font(None, 100)
        font2 = pygame.font.Font(None, 50)
        text2 = font2.render("1-quit", True, (255, 0, 0))
        clock = pygame.time.Clock()
        counter1 = 5
        counter2 = 50
        counter3 = False
        counter4 = False
        score = 0
        while True:
            w.fill((255, 255, 255))
            text3 = font2.render('lives: ' + str(counter1), True, (255, 0, 0))
            w.blit(text2, (50, 50))
            w.blit(text3, (50, 100))
            pygame.draw.rect(w, (0, 255, 0), r1)
            pygame.draw.rect(w, (0, 255, 0), r2)
            pygame.draw.rect(w, (0, 0, 255), r3)
            if r3.colliderect(r1):
                r3_x_add = randint(7, 12)
                r3_y_add = randint(5, 10)
                counter4 = True
            if r3.colliderect(r2):
                r3_x_add = -(randint(7, 12))
                r3_y_add = randint(5, 10)
                if counter4:
                    score += 1
                    counter4 = False
            if r3.x <= 0 and counter2 <= 0:
                counter1 -= 1
                counter2 = 50
                r3.x = 740 
                r3.y = 365
                r3_x_add = randint(7, 12)
            counter2 -= 1
            if counter1 <= 0:
                break
            if close:
                counter1 = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        r1_move_up = True
                    if event.key == pygame.K_DOWN:
                        r1_move_down = True
                    if event.key == pygame.K_1:
                        counter1 = 0
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        r1_move_up = False
                    if event.key == pygame.K_DOWN:
                        r1_move_down = False
            if r1_move_up and r1.y > 0:
                r1.y -= 6   
            if r1_move_down and r1.y < 650:
                r1.y += 6               
            if r3.y >= 720:
                r3_y_add = -(abs(r3_y_add))
            if r3.y <= 0:
                r3_y_add = abs(r3_y_add)
            r3.x += r3_x_add
            r3.y += r3_y_add  
            pygame.display.update()
            clock.tick(60)
        while True:
            w.fill((255, 255, 255))
            text1 = font1.render("Score: " + str(score) + " (1-try again, 2-exit)", True, (0, 0, 255))      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter3 = True
                    if event.key == pygame.K_2:
                        counter3 = True
                        counter5 = False
            if close:
                counter3 = True
                counter5 = False
            if counter3:
                break
            w.blit(text1, (100, 300))
            pygame.display.update()
            clock.tick(60)

def f3():
    global closeall
    counter2 = True
    close = False
    while counter2:
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 300, 10, 150)
        r2 = pygame.Rect(1390, 300, 10, 150)
        r3 = pygame.Rect(740, 365, 20, 20)
        r1_move_up = False
        r1_move_down = False
        r2_move_up = False
        r2_move_down = False
        r3_x_add = 2
        r3_y_add = randint(3, 7)
        font1 = pygame.font.Font(None, 100)
        clock = pygame.time.Clock()
        counter1 = 0
        closewin = False
        while True:
            w.fill((255, 255, 255))
            pygame.draw.rect(w, (0, 255, 0), r1)
            pygame.draw.rect(w, (0, 255, 0), r2)
            pygame.draw.rect(w, (0, 0, 255), r3)
            if r3.colliderect(r1):
                r3_x_add = randint(7, 12)
                r3_y_add = randint(5, 10)
            if r3.colliderect(r2):
                r3_x_add = -(randint(7, 12))
                r3_y_add = randint(5, 10)
            if r3.x >= 1470:
                counter1 += 1
                break
            if r3.x <= 0:
                counter1 += 2
                closewin = True
            if closewin:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        r1_move_up = True
                    if event.key == pygame.K_s:
                        r1_move_down = True
                    if event.key == pygame.K_UP:
                        r2_move_up = True
                    if event.key == pygame.K_DOWN:
                        r2_move_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        r1_move_up = False
                    if event.key == pygame.K_s:
                        r1_move_down = False
                    if event.key == pygame.K_UP:
                        r2_move_up = False
                    if event.key == pygame.K_DOWN:
                        r2_move_down = False
            if close:
                closewin = True
                counter1 += 2
            if r1_move_up and r1.y > 0:
                r1.y -= 8   
            if r1_move_down and r1.y < 600:
                r1.y += 8
            if r2_move_up and r2.y > 0:
                r2.y -= 8 
            if r2_move_down and r2.y < 600:
                r2.y += 8              
            if r3.y >= 720:
                r3_y_add = -(abs(r3_y_add))
            if r3.y <= 0:
                r3_y_add = abs(r3_y_add)
            r3.x += r3_x_add
            r3.y += r3_y_add  
            pygame.display.update()
            clock.tick(60)
        while counter1 != 0:
            w.fill((255, 255, 255))
            if counter1 == 1:
                text1 = font1.render("Left player wins! (1-try again, 2-exit)", True, (0, 0, 255))
            elif counter1 == 2:
                text1 = font1.render("Right player wins! (1-try again, 2-exit)", True, (0, 0, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter1 = 0
                    if event.key == pygame.K_2:
                        counter1 = 0
                        counter2 = False
            if close:
                counter1 = 0
                counter2 = False
            w.blit(text1, (100, 300))
            pygame.display.update()
            clock.tick(60)

def f4():
    global closeall
    close = False
    counter7 = True
    while counter7:
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 600, 30, 30)
        r2 = pygame.Rect(0, 630, 1500, 120)
        r3 = pygame.Rect(300, 550, 950, 4)
        r4 = pygame.Rect(600, 495, 55, 55)
        r5 = pygame.Rect(900, 495, 55, 55)
        r6 = pygame.Rect(1100, 470, 100, 4)
        r7 = pygame.Rect(350, 554, 55, 76)
        r8 = pygame.Rect(300, 390, 950, 4)
        r9 = pygame.Rect(900, 70, 50, 4)
        r10 = pygame.Rect(1050, 335, 55, 55)
        r11 = pygame.Rect(750, 335, 55, 55)
        r12 = pygame.Rect(450, 335, 55, 55)
        r13 = pygame.Rect(300, 310, 100, 4)
        r14 = pygame.Rect(300, 230, 950, 4)
        r15 = pygame.Rect(500, 175, 55, 55)
        r16 = pygame.Rect(700, 175, 55, 55)
        r17 = pygame.Rect(875, 150, 100, 4)
        r18 = pygame.Rect(1150, 554, 55, 76)
        r3_2 = pygame.Rect(300, 554, 950, 4)
        r6_2 = pygame.Rect(1100, 474, 100, 4)
        r8_2 = pygame.Rect(300, 394, 950, 4)
        r9_2 = pygame.Rect(900, 74, 50, 4)
        r13_2 = pygame.Rect(300, 314, 100, 4)
        r14_2 = pygame.Rect(300, 234, 950, 4)
        r17_2 = pygame.Rect(875, 154, 100, 4)
        font1 = pygame.font.Font(None, 70)
        font2 = pygame.font.Font(None, 30)
        font3 = pygame.font.Font(None, 20)
        text1 = font2.render("Avoid the red rectangles!", True, (255, 0, 0))
        text2 = font3.render('Finish line!', True, (255, 150, 0))
        text3 = font2.render('(1-quit)', True, (255, 0, 0))
        r1_move_right = False
        r1_move_left = False
        clock = pygame.time.Clock()
        counter1 = 1
        counter2 = False
        counter3 = False
        counter4 = -1
        counter5 = False
        while True:
            w.fill((255, 255, 255))
            w.blit(text1, (50, 50))
            w.blit(text2, (890, 40))
            w.blit(text3, (50, 70))
            pygame.draw.rect(w, (0, 0, 255), r1)
            pygame.draw.rect(w, (0, 255, 0), r2)
            pygame.draw.rect(w, (0, 255, 0), r3)
            pygame.draw.rect(w, (255, 0, 0), r4)
            pygame.draw.rect(w, (255, 0, 0), r5)
            pygame.draw.rect(w, (0, 255, 0), r6)
            pygame.draw.rect(w, (255, 0, 0), r7)
            pygame.draw.rect(w, (0, 255, 0), r8) 
            pygame.draw.rect(w, (255, 150, 0), r9)
            pygame.draw.rect(w, (255, 0, 0), r10)
            pygame.draw.rect(w, (255, 0, 0), r11)
            pygame.draw.rect(w, (255, 0, 0), r12)
            pygame.draw.rect(w, (0, 255, 0), r13)
            pygame.draw.rect(w, (0, 255, 0), r14)
            pygame.draw.rect(w, (255, 0, 0), r15) 
            pygame.draw.rect(w, (255, 0, 0), r16)
            pygame.draw.rect(w, (0, 255, 0), r17)
            pygame.draw.rect(w, (255, 0, 0), r18)  
            pygame.draw.rect(w, (0, 255, 0), r3_2)
            pygame.draw.rect(w, (0, 255, 0), r6_2)
            pygame.draw.rect(w, (0, 255, 0), r8_2)
            pygame.draw.rect(w, (255, 150, 0), r9_2)
            pygame.draw.rect(w, (0, 255, 0), r13_2)
            pygame.draw.rect(w, (0, 255, 0), r14_2)
            pygame.draw.rect(w, (0, 255, 0), r17_2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter3 = True
                        counter7 = False
                    if event.key == pygame.K_UP and counter1 == 1 and counter4 == -1:
                        counter4 = 1
                        counter1 = 0
                    if event.key == pygame.K_RIGHT:
                        r1_move_right = True
                    if event.key == pygame.K_LEFT:
                        r1_move_left = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        r1_move_right = False
                    if event.key == pygame.K_LEFT:
                        r1_move_left = False
            if close:
                counter3 = True
                counter7 = False
            if counter4 >= 0 and counter4 <= 15:
                counter4 += 1
                r1.y -= 10
            if counter4 > 15:
                counter4 = -1
            if r1_move_right:
                r1.x += 5
            if r1_move_left:
                r1.x -= 5
            if r1.colliderect(r9):
                counter2 = True
                counter3 = True
            if counter3:
                break
            if r1.colliderect(r4) or r1.colliderect(r5) or r1.colliderect(r7) or r1.colliderect(r10) or r1.colliderect(r11) or r1.colliderect(r12) or r1.colliderect(r15) or r1.colliderect(r16) or r1.colliderect(r18):
                counter3 = True
                counter5 = True
            pygame.display.update()
            clock.tick(60)
            if r1.colliderect(r3_2) or r1.colliderect(r6_2) or r1.colliderect(r8_2) or r1.colliderect(r9_2) or r1.colliderect(r13_2) or r1.colliderect(r14_2) or r1.colliderect(r17_2):
                r1.y += 3
            if r1.colliderect(r2) or r1.colliderect(r3) or r1.colliderect(r4) or r1.colliderect(r5) or r1.colliderect(r6) or r1.colliderect(r7) or r1.colliderect(r8) or r1.colliderect(r9) or r1.colliderect(r10) or r1.colliderect(r11) or r1.colliderect(r12) or r1.colliderect(r13) or r1.colliderect(r14) or r1.colliderect(r15) or r1.colliderect(r16) or r1.colliderect(r17):
                counter1 = 1
                continue
            else:
                counter1 = 0
            r1.y += 3
        while True:
            if counter7:
                counter3 = False
            w.fill((255, 255, 255))     
            if counter2:
                text4 = font1.render("You win! (1-try again, 2-exit)", True, (255, 0, 0))      
            else:
                text4 = font1.render('Game over (1-try again, 2-exit)', True, (255, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter3 = True
                    if event.key == pygame.K_2:
                        counter3 = True
                        counter7 = False
            if close:
                counter3 = True
            if counter3:
                break
            w.blit(text4, (100, 300))
            pygame.display.update()
            clock.tick(60)

def f5():
    global closeall
    close_app = False
    close = False
    while close_app == False:
        win = False
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 600, 30, 30)
        r2 = pygame.Rect(0, 630, 6500, 225)
        r3 = pygame.Rect(300, 550, 100, 8)
        r4 = pygame.Rect(430, 450, 60, 8)
        r5 = pygame.Rect(560, 400, 200, 8)
        r6 = pygame.Rect(650, 250, 50, 50)
        r7 = pygame.Rect(800, 260, 400, 8)
        r8 = pygame.Rect(660, 480, 30, 150)
        r9 = pygame.Rect(850, 550, 200, 8)
        r10 = pygame.Rect(950, 500, 50, 50)
        r11 = pygame.Rect(1150, 450, 200, 8)
        r12 = pygame.Rect(1350, 350, 50, 50)
        r13 = pygame.Rect(1400, 430, 50, 200)
        r14 = pygame.Rect(1550, 300, 50, 50)
        r15 = pygame.Rect(1700, 350, 400, 8)
        r16 = pygame.Rect(1575, 450, 50, 50)
        r17 = pygame.Rect(1975, 430, 50, 200)
        r18 = pygame.Rect(1700, 400, 50, 50)
        r19 = pygame.Rect(2200, 350, 200, 8)
        r20 = pygame.Rect(2350, 150, 50, 200)
        r21 = pygame.Rect(2300, 580, 50, 50)
        r22 = pygame.Rect(2800, 500, 50, 50)
        r23 = pygame.Rect(2900, 400, 400, 8)
        r24 = pygame.Rect(3300, 430, 50, 200)
        r25 = pygame.Rect(3450, 430, 50, 50)
        r26 = pygame.Rect(3450, 580, 200, 50)
        r27 = pygame.Rect(3850, 530, 500, 8)
        r28 = pygame.Rect(4300, 546, 50, 84)
        r29 = pygame.Rect(4100, 480, 50, 50)
        r3_2 = pygame.Rect(300, 558, 100, 8)
        r4_2 = pygame.Rect(430, 458, 60, 8)
        r5_2 = pygame.Rect(560, 408, 200, 8)
        r7_2 = pygame.Rect(800, 268, 400, 8)
        r9_2 = pygame.Rect(850, 558, 200, 8)
        r11_2 = pygame.Rect(1150, 458, 200, 8)
        r15_2 = pygame.Rect(1700, 358, 400, 8)
        r19_2 = pygame.Rect(2200, 358, 200, 8)
        r23_2 = pygame.Rect(2900, 408, 400, 8)
        r27_2 = pygame.Rect(3850, 538, 500, 8)
        clock = pygame.time.Clock()
        break_game_loop = False
        r1_move_right = False
        r1_move_left = False 
        collide = False
        has_landed = True
        counter1 = -1   
        display_manual = True
        buttons_pressed = False
        yellow = False
        objects1 = [r2, r3, r4, r5, r7, r9, r11, r15, r19, r23, r27]
        objects2 = [r3_2, r4_2, r5_2, r7_2, r9_2, r11_2, r15_2, r19_2, r23_2, r27_2]
        objectsall = [r2, r3, r3_2, r4, r4_2, r5, r5_2, r6, r7, r7_2, r8, r9, r9_2, r10, r11, r11_2, r12, r13, r14, r15, r15_2, r16, r17, r18, r19, r19_2, r20, r21, r22, r23, r23_2, r24, r25, r26, r27, r27_2, r28, r29]
        objectsgreen = [r2, r3, r3_2, r4, r4_2, r5, r5_2, r7, r7_2, r9, r9_2, r11, r11_2, r15, r15_2, r19, r19_2, r23, r23_2, r27, r27_2]
        objectsred = [r8, r10, r13, r16, r17, r18, r20, r21, r24, r26, r28, r29]
        objectsyellow = [r6, r12, r14, r22, r25]
        font1 = pygame.font.Font(None, 30)
        text1 = font1.render("2-manual (progress will be deleted)", True, (255, 0, 0))
        text12 = font1.render("Finish line", True, (255, 0, 0))
        see_manual = False
        godown = False
        text1_x = 50
        text1_y = 150
        text12_x = 4500
        text12_y = 150
        while True:
            w.fill((255, 255, 255))
            pygame.draw.rect(w, (0, 0, 255), r1)
            for i in objectsgreen:
                pygame.draw.rect(w, (0, 255, 0), i)
            for i in objectsyellow:
                pygame.draw.rect(w, (255, 255, 0), i)
            for i in objectsred:
                pygame.draw.rect(w, (255, 0, 0), i)
            w.blit(text1, (text1_x, text1_y))
            w.blit(text12, (text12_x, text12_y))
            if break_game_loop:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and has_landed and counter1 == -1:
                        counter1 = 1
                        has_landed = False
                        buttons_pressed = True
                    if event.key == pygame.K_SPACE and has_landed and counter1 == -1:
                        counter1 = 1
                        has_landed = False
                        buttons_pressed = True
                    if event.key == pygame.K_1:
                        break_game_loop = True
                    if event.key == pygame.K_2:
                        break_game_loop = True
                        see_manual = True
                    if event.key == pygame.K_RIGHT:
                        r1_move_right = True
                        buttons_pressed = True
                    if event.key == pygame.K_LEFT:
                        r1_move_left = True
                        buttons_pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        r1_move_right = False
                    if event.key == pygame.K_LEFT:
                        r1_move_left = False
            if buttons_pressed:
                display_manual = False
            if close:
                break_game_loop = True
            for i in objectsred:
                if r1.colliderect(i):
                    break_game_loop = True
            if r2.x <= -4500:
                win = True
                break_game_loop = True
            if counter1 >= 0 and counter1 <= 15:
                counter1 += 1
                for i in objectsall:
                    i.y += 10
                text1_y += 10
                text12_y += 10
            for i in objectsyellow:
                if r1.colliderect(i):
                    for i in objectsall:
                        i.y += 150
                    text1_y += 150
                    text12_y += 150
            if counter1 > 15:
                counter1 = -1
            if r1_move_right:
                for i in objectsall:
                    i.x -= 5
                text1_x -= 5
                text12_x -= 5
            if r1_move_left and r2.x < 0:
                for i in objectsall:
                    i.x += 5
                text1_x += 5
                text12_x += 5
            for i in objects1:
                if r1.colliderect(i):
                    collide = True
            for i in objects2:
                if r1.colliderect(i):
                    godown = True
            if collide == False or godown:
                for i in objectsall:
                    i.y -= 3
                text1_y -= 3
                text12_y -= 3
            if collide:
                has_landed = True
            else:
                has_landed = False
            collide = False
            godown = False
            for i in objects2:
                if r1.colliderect(i):
                    has_landed = False
            pygame.display.update()
            clock.tick(60)
        if see_manual:
            w = pygame.display.set_mode((1500, 750))
            close_manual = False
            try_again = True
            text2 = font1.render("Controls:", True, (255, 0, 0))
            text3 = font1.render("1-exit", True, (255, 0, 0))
            text4 = font1.render("arrows-move", True, (255, 0, 0))
            text5 = font1.render("space-jump", True, (255, 0, 0))
            text6 = font1.render("Tips:", True, (255, 0, 0))
            text7 = font1.render("Avoid the red rectangles", True, (255, 0, 0))
            text8 = font1.render("Yellow rectangles will make you go higher", True, (255, 0, 0))
            text9 = font1.render("Green rectangles are platforms", True, (255, 0, 0))
            text10 = font1.render("Enjoy!", True, (255, 0, 0))
            texts = [text2, text3, text4, text5, text6, text7, text8, text9, text10]
            text_y = 50
            while close_manual == False:
                w.fill((255, 255, 255))
                for i in texts:
                    w.blit(i, (50, text_y))
                    text_y += 70
                text_y = 50 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        close = True
                        closeall = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            close_manual = True
                if close:
                    close_manual = True
                pygame.display.update()
                clock.tick(60)
        elif see_manual == False:
            w = pygame.display.set_mode((1500, 750))
            close_end_screen = False
            try_again = False
            if win == False:
                text11 = font1.render('Game over (1-try again, 2-exit)', True, (255, 0, 0)) 
            if win == True:
                text11 = font1.render('You win! (1-try again, 2-exit)', True, (255, 0, 0)) 
            while close_end_screen == False:
                w.fill((255, 255, 255))
                w.blit(text11, (50, 50))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        close = True
                        closeall = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            try_again = True
                            close_end_screen = True
                        if event.key == pygame.K_2:
                            close_end_screen = True
                if close:
                    close_end_screen = True
                pygame.display.update()
                clock.tick(60)
        if try_again == False:
            close_app = True

def f6():
    global closeall
    close = False
    counter8 = True
    while counter8:
        xs1 = 1500
        score = 0
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 600, 30, 30)
        r2 = pygame.Rect(0, 630, 1500, 120)
        s1 = pygame.Rect(xs1, 580, 50, 50)
        font1 = pygame.font.Font(None, 50)
        font2 = pygame.font.Font(None, 100)
        text1 = font1.render("1-quit", True, (255, 0, 0))
        counter1 = True
        counter2 = 5
        counter3 = -1
        counter4 = False
        counter5 = 20
        counter6 = True
        counter7 = 10
        clock = pygame.time.Clock()
        while counter2 > 0:
            if close:
                counter2 = 0
            r1.y += 6
            w.fill((255, 255, 255))
            text2 = font1.render('lives: ' + str(counter2), True, (255, 0, 0))
            w.blit(text2, (50, 100))
            w.blit(text1, (50, 50))
            pygame.draw.rect(w, (0, 0, 255), r1)
            pygame.draw.rect(w, (0, 255, 0), r2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and counter1 and counter3 == -1:
                        counter3 = 0
                        counter1 = False
                    if event.key == pygame.K_1:
                        counter2 = 0
                if event.type == pygame.MOUSEBUTTONDOWN and counter1 and counter3 == -1 and event.button == 1:
                    counter3 = 0
                    counter1 = False
            if counter3 >= 0 and counter3 <= 15:
                counter3 += 1
                r1.y -= 12
            if counter3 > 15:
                counter3 = -1
            if r1.colliderect(r2):
                r1.y -= 6
                counter1 = True
            pygame.draw.rect(w, (255, 0, 0), s1)
            if counter4:
                counter7 = randint(10, 25)
                counter4 = False
            s1.x -= counter7
            if s1.x <= -50:
                s1.x = xs1
                if counter6:
                    score += 1
                counter4 = True
                counter6 = True
            if r1.colliderect(s1) and counter5 <= 0:
                counter5 = 20
                counter2 -= 1
                counter6 = False
            counter5 -= 1
            if counter2 <= 0:
                text2 = font2.render('Score: ' + str(score) + ' (1-try again, 2-exit)', True, (255, 0, 0))
            pygame.display.update()
            clock.tick(60)
        while counter2 <= 0:
            if close:
                counter2 = 1
                counter8 = False
            w.fill((255, 255, 255))
            w.blit(text2, (100, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter2 = 1
                    if event.key == pygame.K_2:
                        counter8 = False
                        counter2 = 1
            pygame.display.update()
            clock.tick(60)

def f7():
    global closeall
    close = False
    counter11 = True
    while counter11:
        xs1 = 1500
        ys1_1 = 580
        ys1_2 = 120
        ylist = [ys1_1, ys1_2] 
        score = 0
        w = pygame.display.set_mode((1500, 750))
        r1 = pygame.Rect(100, 600, 30, 30)
        r2 = pygame.Rect(0, 630, 1500, 120)
        r3 = pygame.Rect(0, 0, 1500, 120)
        s1 = pygame.Rect(xs1, ys1_1, 50, 50)
        font1 = pygame.font.Font(None, 30)
        font2 = pygame.font.Font(None, 100)
        text1 = font1.render("1-quit", True, (255, 0, 0))
        counter1 = True
        counter2 = 5
        counter3 = -1
        counter4 = False
        counter5 = 20
        counter6 = True
        counter7 = 10
        counter8 = randint(0, 1)
        counter9 = randint(0, 1)
        counter10 = 0
        clock = pygame.time.Clock()
        while counter2 > 0:
            if counter9 == 0:
                s1.y = ys1_1
                r1c = (0, 0, 255)
                s1c = (255, 0, 0)
            elif counter9 == 1:
                r1c = (255, 0, 0)
                s1c = (0, 0, 255)
                s1.y = ylist[counter8]  
            if r1.y >= 450:
                r1.y += 6
            elif r1.y <= 270:
                r1.y -= 6      
            w.fill((255, 255, 255))
            text2 = font1.render('lives: ' + str(counter2), True, (255, 0, 0))
            w.blit(text2, (1200, 250))
            w.blit(text1, (1200, 280))
            pygame.draw.rect(w, r1c, r1)
            pygame.draw.rect(w, (0, 255, 0), r2)
            pygame.draw.rect(w, (0, 255, 0), r3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and counter1 and counter3 == -1 and counter9 == 0:
                        counter3 = 0
                        counter1 = False
                    if event.key == pygame.K_SPACE and counter1 and counter3 == -1 and counter9 == 1:
                        if r1.y >= 450:
                            r1.y = 120
                        elif r1.y <= 270:
                            r1.y = 600
                    if event.key == pygame.K_1:
                        counter2 = 0
                if event.type == pygame.MOUSEBUTTONDOWN and counter1 and counter3 == -1 and counter9 == 0 and event.button == 1:
                    counter3 = 0
                    counter1 = False
                if event.type == pygame.MOUSEBUTTONDOWN and counter1 and counter3 == -1 and counter9 == 1 and event.button == 1:
                    if r1.y >= 450:
                        r1.y = 120
                    elif r1.y <= 270:
                        r1.y = 600
            if close:
                counter2 = 0
            if counter3 >= 0 and counter3 <= 15:
                counter3 += 1
                if r1.y >= 450:
                    r1.y -= 12
            if counter3 > 15:
                counter3 = -1
            if r1.colliderect(r2) or r1.colliderect(r3):
                if r1.y >= 450:
                    r1.y -= 6
                elif r1.y <= 270:
                    r1.y += 6
                counter1 = True
            pygame.draw.rect(w, s1c, s1)
            if counter4:
                if counter9 == 0 or counter10 == 10:
                    counter7 = randint(10, 25)
                elif counter9 == 1 and counter10 != 10:
                    counter7 = randint(40, 60)
                counter4 = False
            s1.x -= counter7
            if counter10 >= 10:
                counter9 = randint(0, 1)
                if counter9 == 0:
                    if r1.y <= 270: 
                        r1.y = 600
                counter10 = 0
            if s1.x <= -50:
                counter8 = randint(0, 1)
                s1.x = xs1
                counter10 += 1
                if counter6:
                    score += 1
                counter4 = True
                counter6 = True
            if r1.colliderect(s1) and counter5 <= 0:
                counter5 = 20
                counter2 -= 1
                counter6 = False
            counter5 -= 1
            if counter2 <= 0:
                text2 = font2.render('Score: ' + str(score) + ' (1-try again, 2-exit)', True, (255, 0, 0))
            pygame.display.update()
            clock.tick(60)
        while counter2 <= 0:
            w.fill((255, 255, 255))
            w.blit(text2, (100, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    closeall = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        counter2 = 1
                    if event.key == pygame.K_2:
                        counter11 = False
                        counter2 = 1 
            if close:
                counter11 = False
                counter2 = 1    
            pygame.display.update()
            clock.tick(60)

closeall = False
while closeall == False:
    w = pygame.display.set_mode((1500, 750))
    controls = []
    xclick = None
    yclick = None
    y = 50
    pygame.display.set_caption('video game collection')
    rectangles = []
    for i in range(7):
        controls.append(False)
        rectangles.append(pygame.rect.Rect(50, y, 1400, 70))
        y += 70
    font = pygame.font.Font(None, 70)
    text1 = font.render('evasion', True, (0, 0, 0))
    text2 = font.render('paddle game I', True, (0, 0, 0))
    text3 = font.render('paddle game II', True, (0, 0, 0))
    text4 = font.render('platformer video game I', True, (0, 0, 0))
    text5 = font.render('platformer video game II', True, (0, 0, 0))
    text6 = font.render('jump', True, (0, 0, 0))
    text7 = font.render('jump II', True,(0, 0, 0))
    texts = [text1, text2, text3, text4, text5, text6, text7]
    functions = [f1, f2, f3, f4, f5, f6, f7]
    clock = pygame.time.Clock()
    while True:
        w.fill((255, 255, 255))
        y = 50
        for i in texts:
            w.blit(i, (50, y))
            y += 70
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closeall = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                xclick, yclick = event.pos
        try:
            for i in range(7):
                if rectangles[i].collidepoint(xclick, yclick):
                    functions[i]()
        except:
            pass
        xclick = None
        yclick = None
        if closeall:
            break
        pygame.display.update()
        clock.tick(60)