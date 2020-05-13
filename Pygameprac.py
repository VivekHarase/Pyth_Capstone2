# This is Hero Hit, a basic game
# Make the Superhero fly to the prize and win the game
# Be careful to avoid hitting the asteroids!

import pygame  
import random

pygame.init()

# Sets screen width and a height.

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Loading of player and enemy images

player = pygame.image.load("superhero.png")
enemy = pygame.image.load("meteorite.png")
enemy_2 = pygame.image.load("asteroid.png")
enemy_3 = pygame.image.load("comet.png")
prizeImg = pygame.image.load("gold.png")
background = pygame.image.load("background.jpg")

# Get the width and height of the images to determine boundary detection, keeping images visible within the game screen

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height ()
enemy_width = enemy.get_width()
enemy_2height = enemy.get_height()
enemy_2width = enemy.get_width()
enemy_3height = enemy.get_height()
enemy_3width = enemy.get_width()
prizeImg_height = prizeImg.get_height()
prize_width = prizeImg.get_width()


# Store the positions of the player variables

playerXPosition = 370
playerYPosition = 480
vel = 5

# Starts off the enemy on the screen and at a random y position.

enemyXPosition = screen_width
enemyYPosition = random.randint(0, 736)
enemy_2XPosition = screen_width
enemy_2YPosition = random.randint(100, 150)
enemy_3XPosition = screen_width
enemy_3YPosition = random.randint(100, 350)

#Stores position of the prize variable

prizeX = 400
prizeY = 20

#Start off the Game loop where conditional statements control gameplay

while 1:

# Drawing of the player, prize and enemy on the game screen

    screen.fill(0)
    screen.blit(background, (0, 0))
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_2, (enemy_2XPosition, enemy_2YPosition))
    screen.blit(enemy_3, (enemy_3XPosition, enemy_3YPosition))
    screen.blit(prizeImg, (prizeX, prizeY))
    pygame.display.flip()  

    # Nested loops to control the game events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls to move the player on the screen 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerXPosition -= vel

    if keys[pygame.K_RIGHT]:
        playerXPosition += vel

    if keys[pygame.K_UP]:
        playerYPosition -= vel

    if keys[pygame.K_DOWN]:
        playerYPosition += vel

    if playerXPosition <= 0:
        playerXPosition = 0
    elif playerXPosition >= 736:
        playerXPosition = 736
    if playerYPosition <= 0:
        playerYPosition = 0
    elif playerYPosition >= 536:
        playerYPosition = 536


    # Bounding box for the player for collision detection

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies for collision detection

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemyBox_2 = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemy_2YPosition
    enemyBox.left = enemy_2XPosition

    enemyBox_3 = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemy_3YPosition
    enemyBox.left = enemy_3XPosition
    
    # Bounding box for the prize for collision detection
    
    prizeBox = pygame.Rect(enemy.get_rect())
    prizeBox.top = prizeY
    prizeBox.left = prizeX


        # Test collision of the boxes:
        # Quits game and exits window if player collides with enemies and loses or gets prize and wins

    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit
        exit(0)

    elif playerBox.colliderect(enemyBox_2):
        print("You lose!")
        pygame.quit
        exit(0)
        
    elif playerBox.colliderect(enemyBox_3):
        print("You lose!")
        pygame.quit
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit
        exit(0)

    # Make enemy approach the player.

    enemyXPosition -= 1
    enemy_2XPosition -= 1
    enemy_3XPosition -= 1



