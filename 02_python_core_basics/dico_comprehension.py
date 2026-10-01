# -------------------------------------------------------------------------------------
# Practice: Create dictionary, add item, update a dictionary, and dict comprehension. |
# -------------------------------------------------------------------------------------

# Initial variables
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# dico comprehension
plays = {song:playcount for song, playcount in zip(songs, playcounts)}
# test
print(plays)

# dico manipulation.
plays["Purple Haze"] = 1
plays["Respect"] = 94
library = {"The Best Songs": plays, "Sunday Feelings": {}}
# test
print(library)