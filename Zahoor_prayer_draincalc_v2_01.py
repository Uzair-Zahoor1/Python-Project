"""
Prayer drain calculator
Student:  Uzair Zahoor
File:Zahoor_prayer_draincalc_v2_01.py
Course:  CIS 156, CGCC
"""
from colorama import Fore # imports colorama which allows me to color my printed text

if __name__ == '__main__':
    # creates a dictionary with our curses and prayer point drain every second for each curse
    print('Curses and their drain rates per second:')
    curses = dict(t90_damage=5, t99_damage=6.67, soulsplit=5, protect_item=0.16, deflection=2.5)
    for curse, prayer_per_sec in curses.items(): # looping through our dictionary items, prints them out for us to see
        print(Fore.YELLOW + f'{curse}: {prayer_per_sec}')
    hour = 3600 # creates a value for 1 hour
    comma = ',' # allows me to concatenate a comma to other strings within print statements
    print() # newline
    print(Fore.RED + '---Prayer point usage---')
    print(Fore.GREEN + 'Enter number of hours:')
    try:
        num_hours = float(input()) # allows you to choose how many hours you want to calculate
    except ValueError: # exception handler for an input that isn't an integer
        print('Invalid number entered.')
    total_hrs = num_hours * hour # puts what you inputted into hours
    for curse, prayer_per_sec in curses.items(): # loops through the dictionary to show prayer points total
        total_time = total_hrs * float(prayer_per_sec)
        if num_hours > 1: # allows my print statements to be plural if the inputted number is more than one
            print(Fore.MAGENTA + 'For', curse + comma, 'after', num_hours, 'hours you will use', float(total_time), 'prayer points.')
        else:
            print(Fore.CYAN + 'For', curse + comma, 'after', num_hours, 'hour you will use', float(total_time), 'prayer points.')