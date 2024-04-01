import random
from math import modf
from datetime import timedelta

def calculate_total_playing_time(songs):
  total = timedelta()
  for song in random.sample(sorted(songs), 3):
    modf(songs[song])
    seconds, minutes = modf(songs[song])
    converted_time = timedelta(minutes=int(minutes), seconds=int(seconds*100))
  
    total+=converted_time
  
  return total


