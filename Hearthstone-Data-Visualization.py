import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
#%matplotlib inline

matchups = df = pd.read_csv('Semester Project Dataset_Deck Matchups.csv')

## Function to create visualization of Class Matchups
def class_matchup(player_arch):
    matchups = df = pd.read_csv('Semester Project Dataset_Deck Matchups.csv')
    percents = np.array(matchups.loc[(df.player_archetype==player_arch), 'win_rate'])
    enemy_arch = np.array(matchups.loc[(df.player_archetype==player_arch), 'opponent_archetype'])
    a = np.arange(1, len(percents)+1)
    plt.figure(figsize=(20,7))
    ax = plt.bar(a, percents)
    plt.title(player_arch+' Win Percentages by Matchup')
    for x in np.arange(1,len(percents)+1):
        if "Druid" in enemy_arch[x-1]:
            ax[x-1].set_color('darkorange')
        if "Hunter" in enemy_arch[x-1]:
            ax[x-1].set_color('darkgreen')
        if "Mage" in enemy_arch[x-1]:
            ax[x-1].set_color('dodgerblue')
        if "Paladin" in enemy_arch[x-1]:
            ax[x-1].set_color('gold')
        if "Priest" in enemy_arch[x-1]:
            ax[x-1].set_color('grey')
        if "Rogue" in enemy_arch[x-1]:
            ax[x-1].set_color('black')
        if "Shaman" in enemy_arch[x-1]:
            ax[x-1].set_color('mediumblue')
        if "Warlock" in enemy_arch[x-1]:
            ax[x-1].set_color('darkmagenta')
        if "Warrior" in enemy_arch[x-1]:
            ax[x-1].set_color('sienna')
        if player_arch == enemy_arch[x-1]:
            ax[x-1].set_color('hotpink')

    plt.axhline(y=50,color = "black")
    plt.xticks(np.arange(1,len(percents)+1), enemy_arch, ha='right',rotation=30)
    plt.show()

## Function to create visualization of individual deck stats
def deck_stats(player_arch):
    deckstats = df = pd.read_csv('Deck Stats.csv')
    held_percent = np.array(deckstats.loc[(df.player_archetype==player_arch), 'held_percentage'])
    drawn_wr = np.array(deckstats.loc[(df.player_archetype==player_arch), 'drawn_wr'])
    played_wr = np.array(deckstats.loc[(df.player_archetype==player_arch), 'played_wr'])
    played_wr = played_wr*100
    turns_held = np.array(deckstats.loc[(df.player_archetype==player_arch), 'turns_held'])
    turn_played = np.array(deckstats.loc[(df.player_archetype==player_arch), 'turn_played'])
    card_names = np.array(deckstats.loc[(df.player_archetype==player_arch), 'card_name'])
    a = np.arange(1, len(held_percent)+1)
    
    plt.figure(figsize=(10,10))

    plt.subplot(3, 2, 1)
    ax = plt.barh(a, held_percent)
    plt.title(player_arch+' Kept in Hand Percentage')
    plt.yticks(np.arange(1,len(held_percent)+1), card_names, ha='right')
    for x in np.arange(0,len(held_percent)):
        if int(held_percent[x])>=60:
            ax[x].set_color('green')
        if int(held_percent[x])<60 and int(held_percent[x])>=50:
            ax[x].set_color('yellow')
        if int(held_percent[x])<50 and int(held_percent[x])>=40:
            ax[x].set_color('orange')
        if int(held_percent[x])<40:
            ax[x].set_color('red')
        
    
    plt.subplot(3, 2, 2)
    ax_drawn = plt.barh(a, drawn_wr, tick_label="")
    plt.title(player_arch+' Drawn Win Rate')
    for x in np.arange(0,len(drawn_wr)):
        if int(drawn_wr[x])>=60:
            ax_drawn[x].set_color('green')
        if int(drawn_wr[x])<60 and int(drawn_wr[x])>=50:
            ax_drawn[x].set_color('yellow')
        if int(drawn_wr[x])<50 and int(drawn_wr[x])>=40:
            ax_drawn[x].set_color('orange')
        if int(drawn_wr[x])<40:
            ax_drawn[x].set_color('red')
            
    # played_wr plot
    plt.subplot(3, 2, 3)
    ax_played = plt.barh(a, played_wr)
    plt.title(player_arch+' Played Win Rate')
    plt.yticks(np.arange(1,len(played_wr)+1), card_names, ha='right')
    for x in np.arange(0,len(drawn_wr)):
        if int(played_wr[x])>=60:
            ax_played[x].set_color('green')
        if int(played_wr[x])<60 and int(played_wr[x])>=50:
            ax_played[x].set_color('yellow')
        if int(played_wr[x])<50 and int(played_wr[x])>=40:
            ax_played[x].set_color('orange')
        if int(played_wr[x])<40:
            ax_played[x].set_color('red')
            
            
    # turns_held plot
    plt.subplot(3,2,5)
    ax_played = plt.bar(a, turns_held)
    plt.title(player_arch+' Average Turns Held In Hand');
    plt.xticks(np.arange(1,len(played_wr)+1), card_names, ha='right', rotation = 45)
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
                    wspace=0.3)
    
    
    # turn_played plot
    plt.subplot(3,2,6)
    ax_played = plt.bar(a, turn_played)
    plt.title(player_arch+' Average Turn Card is Played');
    plt.xticks(np.arange(1,len(played_wr)+1), card_names, ha='right', rotation = 45)
    plt.axhline(y=np.mean(turn_played),color = "black")
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.4,
                    wspace=0.3)
    
    plt.show()



def main():
    player_decks = np.array(matchups.player_archetype.unique())
    print()
    print('Welcome to "Decks of Hearthstone"!')
    print()
    print("How can we help you break the Meta today?")
    print()
    print("Would you like to compare deck win-rates or analyze a specific deck?")
    print()
    x = True
    while x:
        main_menu = str(input("Enter 'win-rates' or 'specific deck' or 'quit' to quit: "))
        print()
        print()
        if main_menu == 'quit' or "Quit":
            x = False
            print("Thanks for analyzing Hearthstone with us! Good luck on the ladder and come again soon!")
        if main_menu == 'win-rates' or main_menu == "Win-Rates":
            x = False
            print("Which deck would you like to see win-rates for?")
            print()
            for i in range(len(player_decks)):
                print("  "+player_decks[i])
            y = True
            while y:
                deck_matchup = str(input("Enter the deck you would like to view or enter 'back' to go back: "))
                print()
                if deck_matchup in player_decks:
                    player_arch = deck_matchup
                    class_matchup(player_arch)
                    print()
                if deck_matchup == 'back' or deck_matchup == "Back":
                    x = True
                    y = False
        if main_menu == "Specific Deck" or main_menu == "specific deck":
            x = False
            print("Which deck do you want to see the card details for?")
            print()
            for i in range(len(player_decks)):
                print("  "+player_decks[i])
            y = True
            while y:
                specific_deck = str(input("Enter the deck you would like to view or enter 'back' to go back: "))
                print()
                if specific_deck in player_decks:
                    player_arch = specific_deck
                    deck_stats(player_arch)
                    print()
                if specific_deck == 'back' or specific_deck == "Back":
                    x = True
                    y = False
    
            
                
            

if __name__ == "__main__":
    main()