# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:48:55 2020

@author: Kaleb Dickerson
"""
import time
import numpy as np
import sys
from random import randint

def delay_print(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
def How2Win(you):
    if you == 0:
        return 1
    elif you == 1:
        return 2
    elif you == 2:
        return 0
    else:
        return 1
def How2Lose(you):
    if you == 0:
        return 2
    elif you == 1:
        return 0
    elif you == 2:
        return 1
    else:
        return 1
def FindWinner(you,comp):
    
    global Won 
    if you == -1:
        delay_print('You input your play incorrectly! ')
        print()
        return "Lost"
    if you == comp:
        return "Drew"
    elif you == 1 and comp == 0:
        return "Won"
    elif you == 1 and comp == 2:
        return "Lost"
    elif you == 0 and comp == 1:
        return "Lost"
    elif you == 0 and comp == 2:
        return "Won"
    elif you == 2 and comp == 0:
        return "Lost"
    elif you == 2 and comp == 1:
        return "Won"
def Easy():
    delay_print('Play your hand: ')
    Play = input().upper()
    Play2Val = {'ROCK':0,'PAPER':1,'SCISSORS':2}
    Comp2Play = {0:'Rock',1:'Paper',2:'Scissors'}
    Your_Streak = 0
    Comp_Streak = 0
    RandLoss = randint(0,4)
    while (Your_Streak != 3) and (Comp_Streak != 3) and (Play != "QUIT"):
        try:
            PlayVal = Play2Val[Play]
        except:
            PlayVal = -1
            Your_Streak = 0
        if RandLoss == 0 or RandLoss == 1:
            RandLoss = randint(0,4)
            CompPlay = How2Lose(PlayVal)
        else:
            RandVic = randint(0,4)
            CompPlay = randint(0,4)
        delay_print('Your opponent played '+str(Comp2Play[CompPlay]))
        print()
        Result = FindWinner(PlayVal,CompPlay)
        
        if Result == "Won":
            Your_Streak += 1
            Comp_Streak = 0
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        elif Result == "Lost":
            Your_Streak = 0
            Comp_Streak += 1
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        else:
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
        delay_print('Play your hand: ')
        Play = input().upper()
    
    if Your_Streak == 3:
        delay_print('Congratulations! You defeated me on easy... sooo impressive.')
    elif Comp_Streak == 3:
        delay_print('HAHAHA... You have been defeated! And in the easiest mode! That\'s just sad!')
    else:
        delay_print('Game Over')
def Normal():
    delay_print('Play your hand: ')
    Play = input().upper()
    Play2Val = {'ROCK':0,'PAPER':1,'SCISSORS':2}
    Comp2Play = {0:'Rock',1:'Paper',2:'Scissors'}
    Your_Streak = 0
    Comp_Streak = 0
    while (Your_Streak != 3) and (Comp_Streak != 3) and (Play != "QUIT"):
        try:
            PlayVal = Play2Val[Play]
        except:
            PlayVal = -1
        CompPlay = randint(0,2)
        delay_print('Your opponent played '+str(Comp2Play[CompPlay]))
        print()
        Result = FindWinner(PlayVal,CompPlay)
        
        if Result == "Won":
            Your_Streak += 1
            Comp_Streak = 0
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        elif Result == "Lost":
            Your_Streak = 0
            Comp_Streak += 1
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        else:
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
        delay_print('Play your hand: ')
        Play = input().upper()
    
    if Your_Streak == 3:
        delay_print('Congratulations! You won! Are you ready to play me on impossible mode?')
    elif Comp_Streak == 3:
        delay_print('HAHAHA... You have been defeated! Maybe an easier level would be more suitable for you.')
    else:
        delay_print('Game Over')
def Impossible():
    delay_print('Play your hand: ')
    Play = input().upper()
    Play2Val = {'ROCK':0,'PAPER':1,'SCISSORS':2}
    Comp2Play = {0:'Rock',1:'Paper',2:'Scissors'}
    Your_Streak = 0
    Comp_Streak = 0
    RandVic = randint(0,3)
    while (Your_Streak != 3) and (Comp_Streak != 3) and (Play != "QUIT"):
        try:
            PlayVal = Play2Val[Play]
        except:
            PlayVal = -1
            Your_Streak = 0
        if Your_Streak == 2 or RandVic == 0:
            RandVic = randint(0,3)
            CompPlay = How2Win(PlayVal)
        else:
            RandVic = randint(0,3)
            CompPlay = randint(0,3)
        delay_print('Your opponent played '+str(Comp2Play[CompPlay]))
        print()
        Result = FindWinner(PlayVal,CompPlay)
        
        if Result == "Won":
            Your_Streak += 1
            Comp_Streak = 0
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        elif Result == "Lost":
            Your_Streak = 0
            Comp_Streak += 1
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
            if Your_Streak == 3 or Comp_Streak == 3:
                break
        else:
            delay_print('You ' + Result + '\t\t Your Streak: ' + str(Your_Streak) + '     Opponent\'s streak: ' + str(Comp_Streak))
            print()
        delay_print('Play your hand: ')
        Play = input().upper()
    
    if Your_Streak == 3:
        delay_print('Congratulations! You won! What I program here is irrelevent because you literally cannot win!')
    elif Comp_Streak == 3:
        delay_print('HAHAHA... You have been defeated! But dont feel too bad, I am a god at this game')
    else:
        delay_print('Game Over')
delay_print('Welcome to the House of Doom... Do you have what it takes to defeat me at Rock Paper Scissors? First to 3 victories in a row wins!')
print('\n')

Play_again = "YES"
while Play_again == "YES":
    delay_print('Select Game-mode (Easy, Normal, or Impossible): ')
    Select = input().upper()
    if Select == 'NORMAL':
        delay_print('What are you, a coward?')
        print()
        Normal()
    elif Select == 'IMPOSSIBLE':
        delay_print('A foolish decision indeed...')
        print()
        Impossible()
    elif Select == 'EASY':
        delay_print('Pathetic... You disgust me.')
        print()
        Easy()
    elif Select == 'QUIT':
        break
    else:
        delay_print('Your dumbass couldn\'t even select the gamemode properly... Try again.')
        print()
        delay_print('Select Game-mode (Normal or Impossible): ')
        Select = input().upper()
    print()
    delay_print('Would you like to play again?')
    Play_again = input().upper()
delay_print('Game Over')





