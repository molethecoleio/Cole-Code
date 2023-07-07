import pygame, random
from threading import Timer

# made by Cole K.
pygame.init()
text_font = pygame.font.SysFont("Arial", 40)
WIDTH, HEIGHT = (700, 700)
CLOCK = pygame.time.Clock()
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
screen.fill(background_colour)
pygame.display.set_caption('SUPER AWSOME COOL CALCULATOR!!!!!! - by cole k')


def draw_text(text, font, font_color, x, y):
    img = font.render(text, True, font_color)
    screen.blit(img, (x, y))


# params 1 = window is displayed on, 2-4 = color of the rectangle, 5-6= x and y of shape, 7-8 = height and width
pygame.draw.rect(screen, (54, 69, 79), (150, 150, 400, 500))  # back of calculator
pygame.draw.rect(screen, (178, 190, 181), (200, 200, 300, 75))  # screen for drawing

b7 = pygame.draw.rect(screen, (115, 147, 179), (203, 300, 50, 50))
draw_text(str(7), text_font, (0, 0, 0), 215, 300)
b8 = pygame.draw.rect(screen, (115, 147, 179), (283, 300, 50, 50))
draw_text(str(8), text_font, (0, 0, 0), 295, 300)
b9 = pygame.draw.rect(screen, (115, 147, 179), (363, 300, 50, 50))
draw_text(str(9), text_font, (0, 0, 0), 375, 300)
bdivide = pygame.draw.rect(screen, (115, 147, 179), (443, 300, 50, 50))
draw_text(str("/"), text_font, (0, 0, 0), 460, 300)

b4 = pygame.draw.rect(screen, (115, 147, 179), (203, 380, 50, 50))
draw_text(str(4), text_font, (0, 0, 0), 215, 380)
b5 = pygame.draw.rect(screen, (115, 147, 179), (283, 380, 50, 50))
draw_text(str(5), text_font, (0, 0, 0), 295, 380)
b6 = pygame.draw.rect(screen, (115, 147, 179), (363, 380, 50, 50))
draw_text(str(6), text_font, (0, 0, 0), 375, 380)
bmulti = pygame.draw.rect(screen, (115, 147, 179), (443, 380, 50, 50))
draw_text(str("x"), text_font, (0, 0, 0), 460, 380)

b1 = pygame.draw.rect(screen, (115, 147, 179), (203, 460, 50, 50))
draw_text(str(1), text_font, (0, 0, 0), 215, 460)
b2 = pygame.draw.rect(screen, (115, 147, 179), (283, 460, 50, 50))
draw_text(str(2), text_font, (0, 0, 0), 295, 460)
b3 = pygame.draw.rect(screen, (115, 147, 179), (363, 460, 50, 50))
draw_text(str(3), text_font, (0, 0, 0), 375, 460)
bminus = pygame.draw.rect(screen, (115, 147, 179), (443, 460, 50, 50))
draw_text("-", text_font, (0, 0, 0), 460, 460)

b0 = pygame.draw.rect(screen, (115, 147, 179), (203, 540, 50, 50))
draw_text(str(0), text_font, (0, 0, 0), 215, 540)
bdec = pygame.draw.rect(screen, (115, 147, 179), (283, 540, 50, 50))
draw_text(str("."), text_font, (0, 0, 0), 300, 540)
badd = pygame.draw.rect(screen, (115, 147, 179), (363, 540, 50, 50))
draw_text(str("+"), text_font, (0, 0, 0), 375, 540)
bequals = pygame.draw.rect(screen, (115, 147, 179), (443, 540, 50, 50))
draw_text(str("="), text_font, (0, 0, 0), 460, 540)

#go back button
bdivide = pygame.draw.rect(screen, (115, 147, 179), (550, 300, 50, 50))
draw_text(str("^"), text_font, (0, 0, 0), 565, 300)
draw_text(str("|"), text_font, (0, 0, 0), 568, 300)

#confm co back
bdivide = pygame.draw.rect(screen, (115, 147, 179), (610, 300, 50, 50))
draw_text(str("<"), text_font, (0, 0, 0), 615, 300)
draw_text(str("---"), text_font, (0, 0, 0), 625, 297)



#print history button for testing purpuses
bhistory = pygame.draw.rect(screen, (115, 147, 179), (550, 550, 125, 100))
draw_text(str("Print"), text_font, (0, 0, 0), 565, 550)
draw_text(str("History"), text_font, (0, 0, 0), 565, 590)

pygame.draw.rect(screen, (115, 147, 179), (150, 100, 150, 50))
draw_text(str("CLEAR"), text_font, (0, 0, 0), 170, 100)

timer = 5
counter = 0
running = True
currentNum = ""
answer = ""
aHistory = []
pHistory = []
while running:
    for event in pygame.event.get():
        mX = pygame.mouse.get_pos()[0]
        mY = pygame.mouse.get_pos()[1]
        
        if event.type == pygame.QUIT:
            running = False
        if timer >= 5:
            if pygame.mouse.get_pressed()[0]:
                timer = 0
                if mX >=150 and mX <= 300 and mY >= 100 and mY <= 150: # clear button
                    if currentNum != "" and answer != "":
                        pHistory.append(currentNum)
                        aHistory.append(answer)
                    currentNum = ""
                    answer = ""
                    pygame.draw.rect(screen, (178, 190, 181), (200, 200, 300, 75)) #shhhh no one will know XD
                    print("cleared")
                elif  mX >= 215 and mX <= 265:
                    if mY >= 300 and mY <= 350:
                        currentNum = currentNum + "7"
                    elif mY >= 380 and mY <= 430:
                        currentNum = currentNum + "4"
                    elif mY >= 460 and mY <= 510:
                        currentNum = currentNum + "1"
                    elif mY >= 540 and mY <= 590:
                        currentNum = currentNum + "0"
                elif mX >= 300 and mX <= 350:
                    if mY >= 300 and mY <= 350:
                        currentNum = currentNum + "8"
                    elif mY >= 380 and mY <= 430:
                        currentNum = currentNum + "5"
                    elif mY >= 460 and mY <= 510:
                        currentNum = currentNum + "2"
                    elif mY >= 540 and mY <= 590:
                        currentNum = currentNum + "."
                elif mX >= 375 and mX <= 425:
                    if mY >= 300 and mY <= 350:
                        currentNum = currentNum + "9"
                    elif mY >= 380 and mY <= 430:
                        currentNum = currentNum + "6"
                    elif mY >= 460 and mY <= 510:
                        currentNum = currentNum + "3"
                    elif mY >= 540 and mY <= 590:
                        currentNum = currentNum + "+"
                elif mX >= 460 and mX <= 510:
                    if mY >= 300 and mY <= 350:
                        currentNum = currentNum + "/"
                    elif mY >= 380 and mY <= 430:
                        currentNum = currentNum + "*"
                    elif mY >= 460 and mY <= 510:
                        currentNum = currentNum + "-"
                    elif mY >= 540 and mY <= 590:
                        answer = str(eval(currentNum))
                        currentNum = currentNum + "="
                        pygame.draw.rect(screen, (178, 190, 181), (200, 200, 300, 75)) #shhhh no one will know XD
                elif mX >= 550 and mX <= 600: # up arrow
                    if mY >= 300 and mY <= 350:
                        pygame.draw.rect(screen, (178, 190, 181), (200, 200, 300, 75)) #shhhh no one will know XD
                        counter += 1
                        currentNum = pHistory[len(pHistory)-counter]
                        answer = aHistory[len(aHistory)-counter]
                        
                elif mX >= 600 and mX <= 700: # up arrow
                    if mY >= 300 and mY <= 350:
                        pygame.draw.rect(screen, (178, 190, 181), (200, 200, 300, 75)) #shhhh no one will know XD
                        currentNum = aHistory[len(aHistory)-counter]
                        counter = 0
                        answer = ""
                        
                elif mX >= 550 and mX <= 675:
                    if mY >= 550 and mY <= 650:
                        for i in range(len(pHistory)):
                            print(pHistory[i] + aHistory[i])
    if timer <= 5:
        timer += 1
                    
    CLOCK.tick(FPS)
    draw_text(str(currentNum), text_font, (0, 0, 0), 220, 220)
    draw_text(str(answer), text_font, (0, 0, 0), 450, 220)
    pygame.display.flip()

pygame.quit()