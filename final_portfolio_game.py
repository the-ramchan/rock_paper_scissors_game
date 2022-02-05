"""""
DEVELOPED BY LAL RAMCHANDANI
02.05.2021
NUCAMP BOOTCAMP PROJECT
"""""


############## IMPORT LIBRARIRES ##############
import pandas as pd
import numpy as np
import random

############## INITIALIZAE ALL VARIABLES AND DATAFRAMES, BUILD LOGIC ##############
user = ''
menu_select = 0
d = {'user': ['-'], 'comp': ['-'], 'user_pt': [0], 'comp_pt': [0]}
score_df = pd.DataFrame(data=d)
battle_df = pd.DataFrame(data=d)

# CREATE A DATA FRAME TO HOUSE CHOICES AND POINTS
df1 = pd.DataFrame(['rock', 'paper', 'scissors'], columns=['user'])
df2 = pd.DataFrame(['rock', 'paper', 'scissors'], columns=['comp'])
df = pd.merge(df1, df2, how='cross')

cond = [(df['user'] == 'rock') & (df['comp'] == 'rock'),
        (df['user'] == 'rock') & (df['comp'] == 'paper'),
        (df['user'] == 'rock') & (df['comp'] == 'scissors'),
        (df['user'] == 'paper') & (df['comp'] == 'rock'),
        (df['user'] == 'paper') & (df['comp'] == 'paper'),
        (df['user'] == 'paper') & (df['comp'] == 'scissors'),
        (df['user'] == 'scissors') & (df['comp'] == 'rock'),
        (df['user'] == 'scissors') & (df['comp'] == 'paper'),
        (df['user'] == 'scissors') & (df['comp'] == 'scissors')]

choices_user = [0, 0, 1, 1, 0, 0, 0, 1, 0]
choices_comp = [0, 1, 0, 0, 0, 1, 1, 0, 0]

df['user_pt'] = np.select(cond, choices_user, default='check')
df['comp_pt'] = np.select(cond, choices_comp, default='check')

############## FUNCTIONS TO BE CALLED ON LATER ##############

# MENU FUNCTION


def show_menu():
    global menu_select
    print("")
    print("= ROCK .. PAPER .. SCISSORS =")
    print("------------------------------")
    print("|1.       Start New Game     |")
    print("|2.       Show Points        |")
    print("|3.       Next Round         |")
    print("|4.       Exit               |")
    print("------------------------------")
    menu_select = input('\n Please make a selection: ')

# REGISTER FUNCTION


def register():
    global user, d, score_df, battle_df
    d = {'user': ['-'], 'comp': ['-'], 'user_pt': [0], 'comp_pt': [0]}
    score_df = pd.DataFrame(data=d)
    battle_df = pd.DataFrame(data=d)
    user = input('WELCOME! Please enter your name for the game: ')
    return user

# BATTLE FUNCTION


def battle():
    global battle_df
    user_choice = input(
        'ROCK, PAPER, OR SCISSORS - Make your selection: ').lower()
    a = pd.DataFrame([user_choice], columns=['user'])
    comp_choice = random.choice(['rock', 'paper', 'scissors'])
    b = pd.DataFrame([comp_choice], columns=['comp'])
    battle_df = pd.concat([a, b], axis=1)
    battle_df = pd.merge(battle_df, df[['user', 'comp', 'user_pt', 'comp_pt']], on=[
                         'user', 'comp'], how='left')
    return battle_df

# WINNER SELECT FOR FUNCTIONS


def winner_select(battle_df):
    print('')
    print('')
    print('')
    print(battle_df)
    if battle_df['user_pt'].sum() > battle_df['comp_pt'].sum():
        print('-----------------------')
        print('')
        print(str(user) + ' is winning!')
        print('')
    elif battle_df['user_pt'].sum() < battle_df['comp_pt'].sum():
        print('-----------------------')
        print('')
        print('Computer is winning!')
        print('')
    else:
        print('-----------------------')
        print('')
        print('It tied so far!')
        print('')

# POINT TRACKER


def pt_tracker(battle_df):
    global score_df
    score_df = pd.concat([score_df, battle_df])
    return score_df

# OVERALL WINNER SELECT


def overall_winner(score_df):
    print(score_df)
    score_df['user_pt'] = score_df['user_pt'].astype(int)
    score_df['comp_pt'] = score_df['comp_pt'].astype(int)
    if score_df['user_pt'].sum() > score_df['comp_pt'].sum():
        print('-----------------------')
        print(str(user) + ' is winning!')
    elif score_df['user_pt'].sum() < score_df['comp_pt'].sum():
        print('-----------------------')
        print('Computer is winning!')
    else:
        print('-----------------------')
        print('It tied so far!')


############## EXECUTION CODE ##############
while True:
    show_menu()

    if menu_select == '1':
        register()
        battle()
        winner_select(battle_df)
        pt_tracker(battle_df)

    elif menu_select == '2':
        overall_winner(score_df)

    elif menu_select == '3':
        battle()
        winner_select(battle_df)
        pt_tracker(battle_df)

    elif menu_select == '4':
        print('Thanks for Playing!')
        print('Results Below: ')
        overall_winner(score_df)
        break

    else:
        print('\n Not A Valid Selection, please try again')
        show_menu()
