import pygame, random

pygame.init()

input("what is your  name? ")

space = pygame.image.load("space.jpg")
space = pygame.transform.scale(space, (800, 600))

font = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 100)
speed2 = 0
screen = pygame.display.set_mode((800, 600))

bomb = pygame.image.load("bomb.png")
bombs = []
bomb = pygame.transform.scale(bomb, (40, 40))
for _ in range(3):
    bomb_x = random.randint(0, 750)
    bomb_y = 0
    bomb_speed = 0.3
    bombs.append([bomb_x, bomb_y, bomb_speed])

pygame.display.set_caption("basket & star")
icon = pygame.image.load("basket_green.png")
pygame.display.set_icon(icon)

score = 0
game_over = font2.render(" -game over- ", True, ("#69FF76"))
level = font2.render("level up!", True, ("#69FF76"))
basket_img = pygame.image.load("basket_green.png") 
basket_img = pygame.transform.scale(basket_img, (100, 100))
basket_x = 600
basket_y = 300
speed = 1.1

star_img = pygame.image.load("star.png")
star_img = pygame.transform.scale(star_img, (40, 40))


stars = []
for _ in range(3):
    star_x = random.randint(0, 750)
    star_y = 0
    star_speed = 0.3
    stars.append([star_x, star_y, star_speed])
    
if score == 10:
    pygame.time.wait(10) 
    screen.blit(level, (200, 300))
    score=35

running = True
while running:
      
    basket_rect = basket_img.get_rect(topleft=(basket_x, basket_y))
    for i in bombs:

        if i[1] > 800:
            i[1] = 0
            i[0] = random.randint(0, 780)

        if score == 10:
           
            i[2] =+ 1
        
        i[1] += i[2]
        bomb_rect = bomb.get_rect(topleft=(i[0],i[1]))
        if bomb_rect.colliderect(basket_rect):
            score -= 1
            i[1] = 0
            i[0] = random.randint(0, 780)

    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= speed
    if keys[pygame.K_RIGHT]:
        basket_x += speed

    if basket_x < 0:
        basket_x = 0
    if basket_x > 750:
        basket_x = 750
    if basket_y < 0:
        basket_y = 0
    if basket_y > 560:
        basket_y = 560

        for i in stars:
            star_rect = star_img.get_rect(topleft=(i[0],i[1]))

    for i in stars:
        if score == 10:
           
            i[2] =+ 1
        
        i[1] += i[2]
        star_rect = star_img.get_rect(topleft=(i[0],i[1]))
        if star_rect.colliderect(basket_rect):
            score += 1
            i[1] = 0
            i[0] = random.randint(0, 780)

        if i[1] > 800:
            score -= 1
            i[1] = 0
            i[0] = random.randint(0, 780)
        
    score_txt = font.render(f"score:{score}", True, ("#69FF76"))

    screen.fill((55, 93, 15))
    screen.blit(space, (0, 0))
    screen.blit(basket_img, (basket_x, basket_y))


    for i in stars:
        if score == -10:
            
            screen.blit(game_over, (200, 300))
            pygame.time.wait(5) 
            if score == -10:
                running = False
        screen.blit(star_img, (i[0], i[1]))
    screen.blit(score_txt, (10, 10))

    for _ in stars:
        if score == 30:
            screen.blit(level, (200, 300))
            pygame.time.wait(5) 

    for i in bombs:
        screen.blit(bomb, (i[0], i[1]))
    
    pygame.display.update()
