import pygame
import sys

pygame.init()  # starting pygame

# screensize, making the screen surface
screen = pygame.display.set_mode((900, 520))
clock = pygame.time.Clock()  # clock objet, determines the framerate of the game

# loading image to variable, has to be in same folder if done this way
wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1_bg = pygame.image.load('Cloud1.png')
cloud2_bg = pygame.image.load('Cloud2.png')
crosshair = pygame.image.load('crosshair.png')

land_position_y = 375
land_speed = 1

water_position_y = 440
water_speed = 1.5

while True:
    for event in pygame.event.get():  # pygame searching for events (searches for all player input)
        if event.type == pygame.QUIT:  # check for closing button of the window
            pygame.quit()  # closes just the pygame module
            sys.exit()  # closes the program completely
        if event.type == pygame.MOUSEMOTION: #checking if the mouse is moving
            crosshair_rect = crosshair.get_rect(center = event.pos) #drawing a rectangle around the surface and placing it's center on the position of the mouse

    # -------------Background placements-----------------
    screen.blit(wood_bg, (0, 0))

    # -------------land movement + placement-----------------
    land_position_y -= land_speed

    if land_position_y <= 335 or land_position_y >= 405:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    # -------------Water movement + placement-----------------
    water_position_y -= water_speed

    if water_position_y <= 420 or water_position_y >= 450:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))
    
    # -------------Crosshair Placement-----------------
    screen.blit(crosshair,crosshair_rect)

    # -------------Cloud Placement-----------------
    screen.blit(cloud1_bg, (50, 50))
    screen.blit(cloud2_bg, (200, 40))
    screen.blit(cloud1_bg, (500, 30))
    screen.blit(cloud2_bg, (700, 40))
    screen.blit(cloud1_bg, (400, 50))

    # -------------Necesary Parameters-----------------
    # update the screen, refreshing, displaying it in the variable screen
    pygame.display.update()
    clock.tick(120)  # 120 fps
