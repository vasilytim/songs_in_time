
import random
from math import modf
from datetime import timedelta
import module

my_favorirte_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

def start_project():
    print(module.calculate_total_playing_time(my_favorirte_songs_dict))
  

if __name__ == '__main__':
  start_project()

