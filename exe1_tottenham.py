"""You are the Manager of Manchester United FC, and your objective is to defeat Tottenham Hotspur. 
To achieve this, you must consider the power level of your players and choose the appropriate line-up 
against your opponent. Select 11 players from your team.

....

How it works: The system will randomly generate 11 Tottenham Hotspur players, comprising 1 goalkeeper, 
4 defenders, 3 midfielders, and 3 strikers.

As the Manager of Manchester United, you must select 11 players following the same system: 4-3-3."""

import os
import random

#data

tot_goalkeapers = {"Hugo Lloris": 85,"Guglielmo Vicario": 79, "Fraser Forster": 79,
                  "Brandon Austin": 79}
tot_defenders = {"Eric Dier": 80, "Cristian Romero": 80, "Davinson Sánchez": 74, 
                 "Japhet Tanganga": 70, "Matt Doherty": 70, "Djed Spence": 70, 
                 "Sergio Reguilón": 74, "Ben Davies": 76, "Joe Rodon": 70, 
                 "Mislav Orsic": 71}
tot_midfielders = {"Oliver Skipp": 70, "Pierre-Emile Højbjerg": 70, "Yves Bissouma": 72, 
                   "James Maddison": 74, "Giovani Lo Celso": 78, "Ryan Sessegnon": 80, 
                   "Dejan Kulusevski": 60, "Pape Sarr": 65, "Rodrigo Bentancur": 65}
tot_forwards = {"Son Heung-Min": 78, "Richarlison": 82, "Bryan Gil": 80, "Timo Werner": 82, 
                "Brennan Johnson": 70, "Manor Solomon": 70, "Alejo Véliz": 75, 
                "Dane Scarlett": 75}

man_goalkeapers = {"André Onana": 80, "Tom Heaton": 75, "Altay Bayindir": 69}
man_defenders = {"Victor Lindelöf": 80, "Harry Maguire": 82, "Lisandro Martínez": 82, "Tyrell Malacia": 67, 
                 "Raphaël Varane": 80, "Diogo Dalot": 89, "Luke Shaw": 89, "Aaron Wan-Bissaka": 70}
man_midfielders = {"Sofyan Amrabat": 76, "Scott McTominay": 80, "Bruno Fernandes": 88, 
                   "Christian Eriksen": 67, "Mason Mount": 77, "Kobbie Mainoo": 65, "Daniel Gore": 60}
man_forwards = {"Anthony Martial": 50, "Marcus Rashford": 76, "Antony": 75, "Rasmus Højlund": 80, 
                "Alejandro Garnacho": 85, "Facundo Pellistri": 75}

list_tot = [tot_goalkeapers, tot_defenders, tot_defenders, tot_defenders, tot_defenders, 
            tot_midfielders, tot_midfielders, tot_midfielders, tot_forwards, tot_forwards,
            tot_forwards]
list_man = [man_goalkeapers, man_defenders, man_defenders, man_defenders, man_defenders, 
            man_midfielders, man_midfielders, man_midfielders, man_forwards, man_forwards,
            man_forwards]
tot_players = []
man_players = []

def select_tot():
    list_select = []
    for tot in list_tot:
        num_random = random.randrange(0,len(tot)-1)
        list_select.append(num_random)
                 
    list_player_tot = []
    for x in range(0,10):
        players = list(list_tot[x].keys())
        index = list_select[x]
        list_player_tot.append(players[index])
    
    return list_player_tot

def print_players(list_players, team):
    list_positions = ['Portero:\n------------', '\nDefensa:\n------------', '---', '---', '---', 
                      '\nMediocampo:\n------------', '---', '---', '\nDelantero:\n------------', '---', '---']
    for x in range(0,10):
        print(list_positions[x])
        name = list_players[x]
        if team == 'tot':  
            points = list_tot[x]
        elif team == 'man':
            points = list_man[x]
        print(f"{name} - {points[name]}")
        
def select_players(list_player_tot):
    list_player_man = []
    for x in  range(0,10):
        name = list_player_tot[x]
        points_man = 0
        man_player = None
        if x == 0:
            points_tot = tot_goalkeapers[name]
            for man in man_goalkeapers.items():
                if (man[1] >= points_tot or man[1] >= points_man) and man[0] not in list_player_man:
                    man_player = man[0]
                    points_man = man[1]
            list_player_man.append(man_player)
        elif x in [1, 2, 3, 4]:
            points_tot = tot_defenders[name]
            for man in man_defenders.items():
                if (man[1] >= points_tot or man[1] >= points_man) and man[0] not in list_player_man:
                    man_player = man[0]
                    points_man = man[1]
            list_player_man.append(man_player)
        elif x in [5, 6, 7]:
            points_tot = tot_midfielders[name]
            for man in man_midfielders.items():
                if (man[1] >= points_tot or man[1] >= points_man) and man[0] not in list_player_man:
                    man_player = man[0]
                    points_man = man[1]
            list_player_man.append(man_player)
        elif x in [8, 9, 10]:
            points_tot = tot_forwards[name]
            for man in man_forwards.items():
                if (man[1] >= points_tot or man[1] >= points_man) and man[0] not in list_player_man:
                    man_player = man[0]
                    points_man = man[1]
            list_player_man.append(man_player)
         
    return list_player_man
                
    
    
list_player_tot = select_tot()
print_players(list_player_tot, team='tot')
list_player_man = select_players(list_player_tot)
print('-----------------------------')
print('MANCHESTER')
print_players(list_player_man, 'man')


