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

tot_goalkeapers = {"Hugo Lloris": 85," Guglielmo Vicario": 79, "Fraser Forster": 79,
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
tot_players =[]

pre_players= f"""\
        {players[1]}
    
    *****************
     ***************
      *************
       ***********
        *********
         *******
          *****
           ***
            *\
"""

def select_tot():
    for tot in list_tot:
        print(len(tot))

select_tot



