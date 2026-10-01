#------------------------------ Instructions Scrabble--------------------------------
# In this prcatice, I processed some data from a group of friends playing scrabble. |
# I used dictionaries to organize players, words, and points.                       |
#------------------------------------------------------------------------------------

# Initiale variables 
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Build Point Dictionary
letters += {letter.lower() for letter in letters}
points *= 2
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
# test
print(letter_to_points)

# Score a Word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
# test
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Dictionary that maps players to a list of the words they played.
player_to_words = {
                    "player1":["BLUE", "TENNIS", "EXIT"], 
                    "wordNerd":["EARTH", "EYES", "MACHINE"], 
                    "Lexi Con":["ERASER", "BELLY", "HUSKY"], 
                    "Prof Reader":["ZAP", "COMA", "PERIOD"]
                  }
player_to_points = {}

# Score a Game: Function to check the point of each player.
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# test
update_point_totals()
print(player_to_points)

# Function that take player and word, and add that word to the list of words they've played.
def play_word(player, word):
  player_to_words[player].append(word)

# test
play_word("player1", "CODE")
print(player_to_words)