from operator import or_
import pygame, sys
from button import Button
import time
from pygame.locals import *
from pygame import mixer
import random

#Initialization
pygame.init()
mixer.init()

#Determine the fonts used in the program
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

#Sound effects
buttonSound = pygame.mixer.Sound("assets/button.wav")
punchSound = pygame.mixer.Sound("assets/punch.wav")
fartSound = pygame.mixer.Sound("assets/fart.wav")
bulletSound = pygame.mixer.Sound("assets/gunshot.wav")

#Declaring variables
white = 255,255,255
clock = pygame.time.Clock()
result1 = pygame.image.load("assets/red_gun.png")
result2 = pygame.image.load("assets/red_gun (2).png")
result3 = get_font(70).render(("TIE"),True, white)

#Player 1 attributes
player1 = []
player1.append(pygame.image.load('assets/jack1.png')) #0
player1.append(pygame.image.load('assets/player1_idle.png')) #1
player1.append(pygame.image.load('assets/player1_rock.png')) #2
player1.append(pygame.image.load('assets/player1_paper.png')) #3
player1.append(pygame.image.load('assets/player1_scissor.png')) #4 
player1.append(pygame.image.load('assets/player1_roulette.png')) #5
player1.append(pygame.image.load('assets/jack1_dead.png')) #6
player1.append(pygame.image.load('assets/player1_ghost.png')) #7
player1.append("JACK") #8

#Player 2 attributes
player2 = []
player2.append(pygame.image.load('assets/jack2.png')) #0
player2.append(pygame.image.load('assets/player2_idle.png')) #1
player2.append(pygame.image.load('assets/player2_rock.png')) #2
player2.append(pygame.image.load('assets/player2_paper.png')) #3
player2.append(pygame.image.load('assets/player2_scissor.png')) #4 
player2.append(pygame.image.load('assets/player2_roulette.png')) #5 
player2.append(pygame.image.load('assets/jack2_dead.png')) #6
player2.append(pygame.image.load("assets/player2_ghost.png")) #7
player2.append("JACK") #8

#Player 1 (Jack) idle animations frames
jack1_idle_animations = []
jack1_idle_animations.append(pygame.image.load("animations/jack1_idle_2.png"))
jack1_idle_animations.append(pygame.image.load("animations/jack1_idle_3.png"))

#Player 1 (Sir McTrump) idle animations frames
mctrump1_idle_animations = []
mctrump1_idle_animations.append(pygame.image.load("animations/mctrump1_idle_2.png"))
mctrump1_idle_animations.append(pygame.image.load("animations/mctrump1_idle_3.png"))

#Player 2 (Jack) idle animations frames
jack2_idle_animations = []
jack2_idle_animations.append(pygame.image.load("animations/jack2_idle_2.png"))
jack2_idle_animations.append(pygame.image.load("animations/jack2_idle_3.png"))

#Player 2 (Sir McTrump) idle animations frames
mctrump2_idle_animations = []
mctrump2_idle_animations.append(pygame.image.load("animations/mctrump2_idle_2.png"))
mctrump2_idle_animations.append(pygame.image.load("animations/mctrump2_idle_3.png"))

#Player 1 (Sir Mctrump) fart animations frames
mctrump1_fart_animations = []
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_1.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_2.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_3.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_4.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_5.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_6.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_8.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_6.png"))
mctrump1_fart_animations.append(pygame.image.load("animations/mctrump1_roulette_8.png"))

#Player 1 (Sir Mctrump) roulette animations frames
mctrump1_roulette_animations = []
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_1.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_2.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_3.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_4.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_5.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_6.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_7.png"))
mctrump1_roulette_animations.append(pygame.image.load("animations/mctrump1_roulette_6.png"))
mctrump1_roulette_animations.append(pygame.image.load("assets/mctrump1_dead.png"))

#Player 1 (Jack) fart animations frames
jack1_fart_animations = []
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_1.png")) #0
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_2.png")) #1
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_3.png")) #2
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_4.png")) #3
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_5.png")) #4
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_6.png")) #5
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_8.png")) #6
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_6.png")) #7
jack1_fart_animations.append(pygame.image.load("animations/jack1_roulette_8.png")) #8

#Player 1 (Jack) roulette animations frames
jack1_roulette_animations = []
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_1.png")) #0
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_2.png")) #1
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_3.png")) #2
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_4.png")) #3
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_5.png")) #4
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_6.png")) #5
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_7.png")) #6
jack1_roulette_animations.append(pygame.image.load("animations/jack1_roulette_6.png")) #7
jack1_roulette_animations.append(pygame.image.load("assets/jack1_dead.png")) #8

#Player 2 (Jack) fart animations frames
player2_fart_animations = []
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_1.png")) #0
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_2.png")) #1
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_3.png")) #2
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_4.png")) #3
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_5.png")) #4
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_6.png")) #5
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_8.png")) #6 
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_6.png")) #7
player2_fart_animations.append(pygame.image.load("animations/jack2_roulette_8.png")) #8

#Player 2 (Jack) roulette animations frames
player2_roulette_animations = []
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_1.png")) #0
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_2.png")) #1
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_3.png")) #2
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_4.png")) #3
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_5.png")) #4
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_6.png")) #5
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_7.png")) #6 
player2_roulette_animations.append(pygame.image.load("animations/jack2_roulette_6.png")) #7
player2_roulette_animations.append(pygame.image.load("assets/jack2_dead.png")) #8

#Left Click
Left = 1

#Create window
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("BREAKING POINT")

#Update animations
def updateAnimation(state, type, player1_current, player2_current, playerIdle, bullet_shot):
        
    #If the current state of the character is idle
    if state == "idle":
        
        #Declare images
        background = pygame.image.load("assets/Fight Page.png")
        screen.blit(background, (0, 0))

        if player1[8] == "JACK":
            animations_1 = jack1_idle_animations

        elif player1[8] == "SIR MCTRUMP":
            animations_1 = mctrump1_idle_animations

        #Spawning players
        if playerIdle == 1:
            screen.blit(animations_1[type], (90,200))
            screen.blit(player2[0], (570,195))
            screen.blit(player2[1], (570,195))
        
        elif playerIdle == 2:
            screen.blit(jack2_idle_animations[type], (570,195))
            screen.blit(player1[0], (90,200))
            screen.blit(player1[1], (90,200))
    
    #If the current state of the character is roulette(blank)
    elif state == "fart":

        #Declare images
        background = pygame.image.load("assets/Fight Page (roulette).png")
        current_image = 0

        while True:
            
            print(current_image)

            screen.blit(background, (0, 0))

            #Calls the function to display the chance of fatal bullet
            updateChance(bullet_shot)

            if player1[8] == "JACK":
                animations = jack1_fart_animations

            elif player1[8] == "SIR MCTRUMP":
                animations = mctrump1_fart_animations

            if player1_current == 5:
                screen.blit(animations[int(current_image)], (90, 200))
                screen.blit(player2[0], (570, 195))
                screen.blit(player2[player2_current], (570, 195))
            
            else:
                screen.blit(player2_fart_animations[int(current_image)], (570, 195))
                screen.blit(player1[0], (90, 200))
                screen.blit(player1[player1_current], (90, 200))

            #Frames timing
            if current_image < 1:
                print("Above is running")
                current_image += 0.010

            elif current_image >= 5 and current_image < 6.8:
                print("Middle is running")
                current_image += 0.0055

            elif current_image >= 7 and current_image < 8:
                print("Middle Below is running")
                current_image += 0.04
            
            elif current_image >= 8 and current_image < 8.9:
                current_image += 0.01
            
            elif current_image > 8.9:
                break

            else:
                print("Below is running")
                current_image += 0.19

            #Check events
            for event in pygame.event.get():

                #If the user close the program, it will exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
    
    #If the current state of the character is roulette(dead)
    elif state == "roulette":

        #Declare images
        background = pygame.image.load("assets/Fight Page (roulette).png")
        current_image = 0

        while True:

            print(current_image)
            
            screen.blit(background, (0, 0))

            #Calls the function to display the chance of fatal bullet
            updateChance(bullet_shot)

            if player1[8] == "JACK":
                animations = jack1_roulette_animations

            elif player1[8] == "SIR MCTRUMP":
                animations = mctrump1_roulette_animations

            if player1_current == 5:
                screen.blit(animations[int(current_image)], (90, 200))
                screen.blit(player2[0], (570, 195))
                screen.blit(player2[player2_current], (570, 195))
            
            else:
                screen.blit(player2_roulette_animations[int(current_image)], (570, 195))
                screen.blit(player1[0], (90, 200))
                screen.blit(player1[player1_current], (90, 200))

            #Frames timings
            if current_image < 1:
                print("Above is running")
                current_image += 0.010

            elif current_image >= 5 and current_image < 6:
                print("Middle is running")
                current_image += 0.007
            
            elif current_image > 8:
                break

            else:
                print("Below is running")
                current_image += 0.19

            #Check events
            for event in pygame.event.get():

                #If the user close the program, it will exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

#Display Chance of Fatal Bullet
def updateChance(bullet_shot):
    
    chance = int(7 - bullet_shot)

    #Color varies depending on the chance
    if chance == 6:
        color = "#34eb43"
        
    elif chance == 5:
        color = "#b4eb34"

    elif chance == 4:
        color = "#ebdc34"
    
    elif chance == 3:
        color = "#eb7734"

    elif chance == 2:
        color = "#eb7734"
    
    else:
        color = "#eb3434"
    
    #Display the chance
    displayChance = get_font(50).render(("1 IN " +str(chance) +" CHANCE"),True, color)
    screen.blit(displayChance, (390, 280))

def rouletteTutorials(player_roulette, bullet_shot, fatal_bullet):

    #Declare images 
    background = pygame.image.load("assets/tutorial(9).png")
    roulette_mode = True

    while roulette_mode == True:

        #Page background
        screen.blit(background, (0, 0))
        
        if player_roulette == 1:
            player1_current = 5
            player2_current = 1
        else:
            player1_current = 1
            player2_current = 5

        #If the current shot is fatal
        if bullet_shot == fatal_bullet:
            bulletSound.play()
            updateAnimation("roulette", 3, player1_current, player2_current, 0, bullet_shot)
            player_alive = False
            print("Player " +str(player_roulette) +" has died")
            print("Game Over")

        #If the current shot is blank
        else:
            fartSound.play()
            updateAnimation("fart", 3, player1_current, player2_current, 0, bullet_shot)
            player_alive = True
            print("Player " +str(player_roulette) +" has survived")
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

        break
    
    return player_alive

#Roulette program
def roulette(player_roulette, bullet_shot, fatal_bullet):

    #Declare images 
    background = pygame.image.load("assets/Fight Page.png")
    roulette_mode = True

    while roulette_mode == True:

        #Page background
        screen.blit(background, (0, 0))
        
        if player_roulette == 1:
            player1_current = 5
            player2_current = 1
        else:
            player1_current = 1
            player2_current = 5

        updateScene(player1_current, player2_current)
        
        #If the current shot is fatal
        if bullet_shot == fatal_bullet:
            bulletSound.play()
            updateAnimation("roulette", 3, player1_current, player2_current, 0, bullet_shot)
            player_alive = False
            print("Player " +str(player_roulette) +" has died")
            print("Game Over")

        #If the current shot is blank
        else:
            fartSound.play()
            updateAnimation("fart", 3, player1_current, player2_current, 0, bullet_shot)
            player_alive = True
            print("Player " +str(player_roulette) +" has survived")
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

        break
    
    return player_alive

#Update player's state on the display's screen
def updateScene(player1_current, player2_current):
    
    #Declare images
    background = pygame.image.load("assets/Fight Page.png")

    #Page background
    screen.blit(background, (0, 0))

    #Spawning players
    if (player1_current > 4 or player2_current > 4):
        if player1_current > 4:
            screen.blit(player2[0], (570,195))
   
        elif player2_current > 4:
            screen.blit(player1[0], (90,200))
        
    else:
        screen.blit(player1[0], (90,200))
        screen.blit(player2[0], (570,195))
              
    screen.blit(player1[player1_current], (90,200))
    screen.blit(player2[player2_current], (570,195))

#Start timer
def updateTimer(result, player1_current, player2_current, duration):
    
    time_start = pygame.time.get_ticks()
    elapsed_time = 0

    while not elapsed_time >= duration:
        current_time = pygame.time.get_ticks()
        elapsed_time = int((current_time - time_start)/1000)

        updateScene(player1_current, player2_current)

        if result == 1:
            screen.blit(result1, (430, 260))
            pygame.display.update()
        
        elif result == 2:
            screen.blit(result2, (430, 260))
            pygame.display.update()
        
        elif result == 3:
            screen.blit(result3, (430, 260))
            pygame.display.update()

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#Display buttons when it is player’s turn
def updateButton(update):

    Single_Mouse_Pos = pygame.mouse.get_pos()

    Rock_Button = Button(image=None, pos=(150, 220), 
                            text_input="ROCK", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    Paper_Button = Button(image=None, pos=(240, 220), 
                        text_input="PAPER", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    Scissor_Button = Button(image=None, pos=(340, 220), 
                        text_input="SCISSOR", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    
    for button in [Rock_Button, Paper_Button, Scissor_Button]:
        button.changeColor(Single_Mouse_Pos)
        button.update(screen)
    
    if update == True:
        pygame.display.update()

#Run the main game flow 
def singleFight():

    Rock_Button = Button(image=None, pos=(150, 200), 
                            text_input="ROCK", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    Paper_Button = Button(image=None, pos=(240, 200), 
                        text_input="PAPER", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    Scissor_Button = Button(image=None, pos=(340, 200), 
                        text_input="SCISSOR", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
    Menu_Button = Button(image=None, pos=(482, 50), 
                            text_input="MENU", font=get_font(50), base_color="White", hovering_color="Red")

    #Declare variables
    player_alive = True
    bullet_shot = 1
    fatal_bullet = random.randint(1,6)
    player_roulette = 0
    game_pause = False
    action = False
    first_time = pygame.time.get_ticks()
    mixer.music.load("assets/main music.wav")

    pygame.mixer.music.play(-1)

    while game_pause == False:

        pygame.mixer.music.set_volume(0.7)
        
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - first_time)/1000

        if elapsed_time >= 4:
            first_time = pygame.time.get_ticks()

        player1_current = 1
        player2_current = 1
        
        #Mouse position
        Single_Mouse_Pos = pygame.mouse.get_pos()

        #Idle animations
        if action == False:

            if elapsed_time >= 0.5 and elapsed_time <= 0.8:
                updateAnimation("idle", 0, player1_current, player2_current, 2, bullet_shot)

            elif elapsed_time >= 1.5 and elapsed_time <= 1.8:
                updateAnimation("idle", 0, player1_current, player2_current, 1, bullet_shot)

            elif elapsed_time >= 2.0 and elapsed_time <= 2.7:
                updateAnimation("idle", 1, player1_current, player2_current, 2, bullet_shot)

            elif elapsed_time >= 3.0 and elapsed_time <= 3.7:
                updateAnimation("idle", 1, player1_current, player2_current, 1, bullet_shot)

            else:
                updateScene(player1_current, player2_current)

            for button in [Menu_Button, Rock_Button, Paper_Button, Scissor_Button]:
                button.changeColor(Single_Mouse_Pos)
                button.update(screen)

            pygame.display.update()

            #Check events
            for event in pygame.event.get():

                #If the user close the program, it will exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left and action == False:
                    
                    #If the player choose "ROCK"
                    if Rock_Button.checkForInput(Single_Mouse_Pos):
                        player1_current = 2
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True

                    #If the player choose "PAPER"
                    if Paper_Button.checkForInput(Single_Mouse_Pos):
                        player1_current = 3
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True
                    
                    #If the player choose "SCISSOR"
                    if Scissor_Button.checkForInput(Single_Mouse_Pos):
                        player1_current = 4
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True
                    
                    #If the player choose "MENU"
                    if Menu_Button.checkForInput(Single_Mouse_Pos):
                        buttonSound.play()
                        main_menu()
            
            #This code will run after the player has choosen between the options
            if action == True:
                pygame.mixer.music.set_volume(0.2)

                result = checkResult(player1_current, player2_current)
            
                if result == 1:
                    player_roulette = 2
                    print("THE WINNER IS " +str(result))

                elif result == 2:
                    player_roulette = 1
                    print("THE WINNER IS " +str(result))
                    
                else:
                    print("DRAW") 

                updateTimer(result, player1_current, player2_current, 2)

                if result == 1 or result == 2:
                    player_alive = roulette(player_roulette, bullet_shot, fatal_bullet)
                    bullet_shot += 1
            
                if player_alive == False:
                    print("Runs")
                    results(player_roulette)

            action = False
            
#Display the result after the fight has ended showing the winner with the scores obtained from the fight.
def results(player_dead):

    ascend = 150

    #Backgrounds
    background = pygame.image.load("assets/Fight Page.png")
    player_ghost = []
    player_ghost.append(pygame.image.load("assets/player1_ghost.png"))
    player_ghost.append(pygame.image.load("assets/player2_ghost.png"))

    #Character buttons
    resultsMenu = Button(image=None, pos=(482, 43), 
                        text_input="MENU", font=get_font(50), base_color="White", hovering_color="Gold")

    #Page loop
    while True:

        #Mouse position
        Results_Mouse_Pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        if player_dead == 1:
            player1_current = 6
            player2_current = 1
            updateScene(player1_current, player2_current)

            screen.blit(player1[7], (100,ascend))
        
        else:
            player1_current = 1
            player2_current = 6
            updateScene(player1_current, player2_current)

            screen.blit(player2[7], (660,ascend))

        ascend -= 0.8

        if ascend < 30 and player_dead == 1:
            background = pygame.image.load("assets/lose.png")
            screen.blit(background, (0,0))
            resultsMenu.changeColor(Results_Mouse_Pos)
            resultsMenu.update(screen)
        
        elif ascend < 30 and not (player_dead == 1):
            background = pygame.image.load("assets/winner.png")
            screen.blit(background, (0,0))
            resultsMenu.changeColor(Results_Mouse_Pos)
            resultsMenu.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:

                #If the "MENU" button is clicked, this code will run
                if resultsMenu.checkForInput(Results_Mouse_Pos):
                    buttonSound.play()
                    main_menu()

        pygame.display.update()

#Will randomly choose moves for the computer during the fight 
def opponentRandomMove():
        randomMove = random.randint(2,4)
        
        #If the program's move is "ROCK"
        if randomMove == 2:
            punchSound.play()
            player2_current = 2
        
        #If the program's move is "PAPER"
        elif randomMove == 3: 
            punchSound.play()
            player2_current = 3
        
        #If the program's move is "SCISSOR"
        elif randomMove == 4: 
            punchSound.play()
            player2_current = 4

        return player2_current

#Check whether player 1 has lost or win in the main program
def checkResult(player1_current, player2_current):

        if player1_current == player2_current:
            result = 3

        elif player1_current == 2 and player2_current == 4:
            result = 1

        elif player1_current == 3 and player2_current == 2:
            result = 1
        
        elif player1_current == 4 and player2_current == 3:
            result = 1
        
        else:
            result = 2
        
        return result

#Display each character for the users to choose and view their stats  
def characterStats():

    background = pygame.image.load("assets/Character Page.png")

    while True:

        #Mouse position
        Character_Mouse_Pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        #Character buttons
        Character_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(50), base_color="White", hovering_color="Gold")
        
        Character_c1 = Button(image=None, pos=(255, 200), 
                            text_input="JACK", font=get_font(35), base_color="White", hovering_color="Gold")
        
        Character_c2 = Button(image=None, pos=(690, 200), 
                            text_input="SIR MCTRUMP", font=get_font(30), base_color="White", hovering_color="Gold")
    
        for button in [Character_Menu, Character_c1, Character_c2]:
            button.changeColor(Character_Mouse_Pos)
            button.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:
                if Character_Menu.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Character_c1.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(1)

                if Character_c2.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(2)

        pygame.display.update()

#Display the general information for each character.
def stats(userOption):

    #Page loop
    while True:
        
        #Mouse position
        Mouse_Pos = pygame.mouse.get_pos()

        #Button instance
        Back_Button = Button(image=None, pos=(482, 43), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Gold")
        
        if userOption == 1:
            background = pygame.image.load("assets/jackStats.png")
            screen.blit(background, (0, 0))
        
        elif userOption == 2:
            background = pygame.image.load("assets/mctrumpStats.png")
            screen.blit(background, (0, 0))
        
        Back_Button.changeColor(Mouse_Pos)
        Back_Button.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:

                #If the "BACK" button is clicked, this code will run
                if Back_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    characterStats()

        pygame.display.update()

#Display a few options of characters for the users to choose.
def characterOption():

    #Page background
    background = pygame.image.load("assets/Character Page.png")

    #Page loop
    while True:

        #Mouse position
        Character_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        #Character buttons
        Character_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(50), base_color="White", hovering_color="Gold")
        
        Character_c1 = Button(image=None, pos=(255, 200), 
                            text_input="JACK", font=get_font(35), base_color="White", hovering_color="Gold")
        
        Character_c2 = Button(image=None, pos=(690, 200), 
                            text_input="SIR MCTRUMP", font=get_font(30), base_color="White", hovering_color="Gold")
    
        for button in [Character_Menu, Character_c1, Character_c2]:
            button.changeColor(Character_Mouse_Pos)
            button.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run     
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:
                if Character_Menu.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Character_c1.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    player1[0] = pygame.image.load("assets/jack1.png")
                    player1[6] = pygame.image.load("assets/jack1_dead.png")
                    player1[8] = ("JACK")
                    singleFight()

                if Character_c2.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    player1[0] = pygame.image.load("assets/mctrump1.png")
                    player1[6] = pygame.image.load("assets/mctrump1_dead.png")
                    player1[8] = ("SIR MCTRUMP")
                    singleFight()

        pygame.display.update()

#Display the game's credits.
def credits():

    background = pygame.image.load("assets/Credits.png")
    
    #Page loop
    while True:

        #Mouse position
        Credits_Mouse_Pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        Credits_Menu = Button(image=None, pos=(482, 50), 
                            text_input="MENU", font=get_font(50), base_color="Black", hovering_color="red")

        Credits_Menu.changeColor(Credits_Mouse_Pos)
        Credits_Menu.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:
                if Credits_Menu.checkForInput(Credits_Mouse_Pos):
                    buttonSound.play()
                    main_menu()

        pygame.display.update()

#Update player's state on the display's screen
def updateTutorialScene(page, player1_current, player2_current):
    
    result = checkResult(player1_current, player2_current)

    if page == 0:
        player1_current = 1
        player2_current = 1
        #Declare images
        background = pygame.image.load("assets/tutorial(0).png")
    
    elif page == 1:
        player1_current = 1
        player2_current = 1
        #Declare images
        background = pygame.image.load("assets/tutorial(1).png")
    
    elif page == 2:
        player1_current = 1
        player2_current = 1
        #Declare images
        background = pygame.image.load("assets/tutorial(2).png")
    
    elif page == 3:
        #Declare images
        background = pygame.image.load("assets/tutorial(tie).png")
    
    elif page == 4:
        #Declare images
        background = pygame.image.load("assets/tutorial(lose).png")
    
    elif page == 5:
        #Declare images
        background = pygame.image.load("assets/tutorial(win).png")
    
    elif page == 6:
        #Declare images
        background = pygame.image.load("assets/tutorial(6).png")
    
    elif page == 7:
        #Declare images
        background = pygame.image.load("assets/tutorial(7).png")
    
    elif page == 8:
        #Declare images
        background = pygame.image.load("assets/tutorial(8).png")
    
    elif page == 9:
        #Declare images
        background = pygame.image.load("assets/tutorial(9).png")
    
    elif page == 10:
        #Declare images
        background = pygame.image.load("assets/tutorial(9).png")
    
    elif page == 11:
        #Declare images
        background = pygame.image.load("assets/tutorial(10).png")
    
    elif page == 12:
        #Declare images
        background = pygame.image.load("assets/tutorial(end).png")
    
    
    if result == 1 and (page == 6 or page == 7 or page == 8):
        player1_current = 1
        player2_current = 5

    elif result == 2 and (page == 6 or page == 7 or page == 8):
        player1_current = 5
        player2_current = 1
    
    else:
        player1_current = 1
        player2_current = 1

    #Page background
    screen.blit(background, (0, 0))

    if page == 5:
        screen.blit(result1, (430, 260))

    elif page == 4:
        screen.blit(result2, (430, 260))
    
    elif page == 3:
        screen.blit(result3, (430, 260))

    #Spawning players
    if (player1_current > 4 or player2_current > 4):
        if player1_current > 4:
            screen.blit(player2[0], (570,195))
   
        elif player2_current > 4:
            screen.blit(player1[0], (90,200))
        
    else:
        screen.blit(player1[0], (90,200))
        screen.blit(player2[0], (570,195))
              
    screen.blit(player1[player1_current], (90,200))
    screen.blit(player2[player2_current], (570,195))

#Display the tutorials of the game as the guides for the players.
def tutorials():

    page = 0
    action = False
    player1_current = 1
    player2_current = 1
    player_roulette = 0

    #Page loop
    while True:

        print(page)
        
        #Mouse position
        Tutorials_Mouse_Pos = pygame.mouse.get_pos()

        #Buttons instance
        Rock_Button = Button(image=None, pos=(150, 200), 
                            text_input="ROCK", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
        Paper_Button = Button(image=None, pos=(240, 200), 
                            text_input="PAPER", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
        Scissor_Button = Button(image=None, pos=(340, 200), 
                            text_input="SCISSOR", font=get_font(40), base_color="#E1E4E4", hovering_color="Red")
        Next_Button = Button(image=pygame.image.load("assets/next1.png"), pos=(910, 95), 
                                text_input="", font=get_font(30), base_color="White", hovering_color="Red")
        Back_Button = Button(image=pygame.image.load("assets/back1.png"), pos=(50, 95), 
                                text_input="", font=get_font(30), base_color="White", hovering_color="Red")
        Tutorial_Menu = Button(image=None, pos=(480, 300), 
                            text_input="MENU", font=get_font(50), base_color="#dce0df", hovering_color="red")

        if action == False:
            
            updateTutorialScene(page, player1_current, player2_current)

            if page == 0 or page == 1 or page == 4 or page == 5 or page == 6 or page == 7 or page == 8 or page == 10 or page == 11:
                Next_Button.update(screen)  

            if page == 1 or page == 2 or page == 3 or page == 6 or page == 7 or page == 8 or page == 11 or page == 12:
                Back_Button.update(screen)
            
            if page == 1 or page == 2:
                for button in [Rock_Button, Paper_Button, Scissor_Button]:
                    button.changeColor(Tutorials_Mouse_Pos)
                    button.update(screen)
            
            if page == 7 or page == 8:
                updateChance(1)
            
            if page == 9:
                rouletteTutorials(player_roulette, 1, 2)
                page += 1
            
            if page == 12:
                Tutorial_Menu.changeColor(Tutorials_Mouse_Pos)
                Tutorial_Menu.update(screen)
        
            pygame.display.update()

        if action == True:
            result = checkResult(player1_current, player2_current)
            
            if result == 1:
                player_roulette = 2
                page = 5
        
            elif result == 2:
                player_roulette = 1
                page = 4
            
            elif result == 3:
                page = 3

            action = False

            pygame.display.update()
            
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:

                #If the player choose "NEXT"
                if Next_Button.checkForInput(Tutorials_Mouse_Pos) and page != 2 and page != 12:

                    if page == 4:
                        page += 2

                    else:
                        page += 1
                        buttonSound.play()

                #If the player choose "BACK"
                if Back_Button.checkForInput(Tutorials_Mouse_Pos) and page != 0 and page != 4 and page != 5 and page != 10:
                    page -= 1
                    buttonSound.play()   

                #If the player choose "MENU"
                if Tutorial_Menu.checkForInput(Tutorials_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                    
                if page == 2:
                    
                    #If the player choose "ROCK"
                    if Rock_Button.checkForInput(Tutorials_Mouse_Pos):
                        player1_current = 2
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True

                    #If the player choose "PAPER"
                    if Paper_Button.checkForInput(Tutorials_Mouse_Pos):
                        player1_current = 3
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True
                    
                    #If the player choose "SCISSOR"
                    if Scissor_Button.checkForInput(Tutorials_Mouse_Pos):
                        player1_current = 4
                        buttonSound.play()
                        player2_current = opponentRandomMove()
                        action = True   

#Display the tutorials of the game as the guides for the players.
def tutorial():

    page = 1

    #Page loop
    while True:
        
        #If the current page is page 1
        if page == 1:
            background = pygame.image.load("assets/tutorials.png")
        
        #If the current page is page 2
        elif page == 2:
            background = pygame.image.load("assets/tutorials (2).png")

        #Mouse position
        Tutorials_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        #Buttons instance
        Tutorials_Menu = Button(image=None, pos=(482, 50), 
                            text_input="MENU", font=get_font(50), base_color="Black", hovering_color="red")
        Tutorials_Next = Button(image=pygame.image.load("assets/next.png"), pos=(830, 300), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        Tutorials_Back = Button(image=pygame.image.load("assets/back.png"), pos=(100, 300), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="cadetblue1")

        Tutorials_Menu.changeColor(Tutorials_Mouse_Pos)
        Tutorials_Menu.update(screen)

        if page == 1:
            Tutorials_Next.changeColor(Tutorials_Mouse_Pos)
            Tutorials_Next.update(screen)

        if page == 2:
            Tutorials_Back.changeColor(Tutorials_Mouse_Pos)
            Tutorials_Back.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:
                if Tutorials_Menu.checkForInput(Tutorials_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Tutorials_Next.checkForInput(Tutorials_Mouse_Pos) and page == 1:
                    buttonSound.play()
                    page = 2

                if Tutorials_Back.checkForInput(Tutorials_Mouse_Pos) and page == 2:
                    buttonSound.play()
                    page = 1

        pygame.display.update()

#Display the main menu of the game.
def main_menu():

    background = pygame.image.load("assets/background.png")
    background = pygame.image.load("assets/background (2).png")
    first_time = pygame.time.get_ticks()
    mixer.music.load("assets/light_bulb.wav")

    pygame.mixer.music.play(-1)

    while True:

        
        clock.tick(60)
        
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - first_time)/1000
        print(elapsed_time)

        if elapsed_time > 5.14:
            first_time = pygame.time.get_ticks()

        #Page background
        screen.blit(background, (0, 0))

        if elapsed_time >= 0 and elapsed_time <= 1:
            background = pygame.image.load("assets/background.png")

        elif elapsed_time >= 1.5 and elapsed_time <= 1.55:
            background = pygame.image.load("assets/background (2).png")

        elif elapsed_time >= 1.05 and elapsed_time <= 1.6:
            background = pygame.image.load("assets/background.png")

        elif elapsed_time >= 1.7 and elapsed_time <= 1.9:
            background = pygame.image.load("assets/background (2).png")

        elif elapsed_time >= 2.0 and elapsed_time <= 2.1:
            background = pygame.image.load("assets/background.png")
        
        elif elapsed_time >= 2.2 and elapsed_time <= 2.4:
            background = pygame.image.load("assets/background (2).png")
            
        elif elapsed_time >= 2.4 and elapsed_time <= 2.6:
            background = pygame.image.load("assets/background.png")

        elif elapsed_time >= 2.8 and elapsed_time <= 3.2:
            background = pygame.image.load("assets/background (2).png")
        
        elif elapsed_time >= 3.3 and elapsed_time <= 3.9:
            background = pygame.image.load("assets/background.png")

        #Mouse position
        Mouse_Pos = pygame.mouse.get_pos()

        Play_Button = Button(image=None, pos=(675, 280), 
                            text_input="PLAY", font=get_font(70), base_color="#dce0df", hovering_color="Gold")
        Character_Button = Button(image=None, pos=(580, 360), 
                            text_input="CHARACTERS", font=get_font(50), base_color="#dce0df", hovering_color="Gold")
        Tutorials_Button = Button(image=None, pos=(760, 360), 
                            text_input="TUTORIALS", font=get_font(50), base_color="#dce0df", hovering_color="Gold")
        Credits_Button = Button(image=None, pos=(675, 430), 
                            text_input="CREDITS", font=get_font(50), base_color="#dce0df", hovering_color="Gold")
        Exit_Button = Button(image=None, pos=(675, 550), 
                            text_input="QUIT", font=get_font(50), base_color="#dce0df", hovering_color="Red")

        for button in [Play_Button, Character_Button, Tutorials_Button, Credits_Button, Exit_Button]:
            button.changeColor(Mouse_Pos)
            button.update(screen)
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:

                #If the "PLAY" button is clicked, this code will run
                if Play_Button.checkForInput(Mouse_Pos):
                    pygame.mixer.music.pause()
                    buttonSound.play()
                    characterOption()

                #If the "CHARACTER" button is clicked, this code will run
                if Character_Button.checkForInput(Mouse_Pos):
                    pygame.mixer.music.pause()
                    buttonSound.play()
                    characterStats()

                #If the "TUTORIALS" button is clicked, this code will run
                if Tutorials_Button.checkForInput(Mouse_Pos):
                    pygame.mixer.music.pause()
                    buttonSound.play()
                    tutorials()
                
                #If the "CREDITS" button is clicked, this code will run
                if Credits_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    credits()

                #If the "EXIT" button is clicked, this code will run
                if Exit_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    time.sleep(0.3)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#Execute the function main_menu() to start the program.
main_menu()


#Add background music in game