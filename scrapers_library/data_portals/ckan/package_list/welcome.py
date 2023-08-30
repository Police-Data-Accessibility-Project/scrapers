'''W. Alec Akin
Police Data Accessibility Project
PDAP CKAN Python Project
main.py
April 13, 2022
https://pdap.io
Based on information from https://www.pythonsherpa.com/tutorials/2/
Intended for use with https://data.wprdc.org/dataset/officer-training
and other CKAN-based Open Data Portals
welcome.py - fancy welcome banner'''

#Import libraries
#This makes things colorful
from colorama import Fore, Back, Style, init

#Define function which does all the work/presents welcome banner
def welcomeBanner():
    init(autoreset=True)
    print(Fore.BLUE + r"""
    
   

  _____  _____          _____  
 |  __ \|  __ \   /\   |  __ \ 
 | |__) | |  | | /  \  | |__) |
 |  ___/| |  | |/ /\ \ |  ___/ 
 | |    | |__| / ____ \| |     
 |_|    |_____/_/    \_\_|     
  _______     _____            
 |__   __|   / ____|           
    | |_   _| |     __ _ _ __  
    | | | | | |    / _` | '_ \ 
    | | |_| | |___| (_| | | | |     - Get's data from an Open Data Portal URL
    |_|\__,_|\_____\__,_|_| |_|         provided by user, and downloads selected
                                            packages. - Rainmana (Alec)
                               

 
    
    """)