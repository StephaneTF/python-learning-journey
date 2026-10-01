# ------------------------- Boredless Tourist ------------------------
# Recommend attractions to travelers based on their destination      |
# and interests.                                                     |
# --------------------------------------------------------------------
# Setting up global variables
destinations = [
    "Paris, France", "Shanghai, China", 
    "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"
]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


# ---------------------------------------
# Travelling To Faraway Lands           |
# ---------------------------------------
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Test the function
print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    # Use get_destination_index() to retrieve
    # the index of the traveler's destination
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Test the function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# -------------------------------------
# Visiting Interesting Places         |
# -------------------------------------

# Create an empty list of attractions for each destination
attractions = []
for destination in destinations:
    attractions.append([])

# Test list of attractions
print(attractions)

def add_attraction(destination, attraction):
    # Find the index of the destination
    destination_index = get_destination_index(destination)
    # Add the attraction to that destination
    attractions[destination_index].append(attraction)


# Add different attractions / interesting places to go
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])

add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])

add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])

add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])

add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])

add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])

add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])

add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])

add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])

add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# ------------------------------------
# Find the best places to go         |
# ------------------------------------
def find_attractions(destination, interests):
    # Get the destination index
    destination_index = get_destination_index(destination)

    # Get all attractions for that destination
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []

    # Check each attraction against the traveler's interests
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                # Stop checking this attraction after a match
                # to prevent duplicate recommendations
                break
    return attractions_with_interest

# Test find_attractions()
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

# ----------------------------------------------
# See the parts of a city you want to see      |
# ----------------------------------------------

def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0]
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attractions(
        traveler_destination,
        traveler_interests
    )

    # Create the recommendation message
    interests_string = (
        "Hi " + traveler_name +
        ", we think you'll like these places around " +
        traveler_destination + ": "
    )

    # Add attraction names to the message
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ", "
    return interests_string

# Test get_attractions_for_traveler()
smills_france = get_attractions_for_traveler(
["Dereck Smill", "Paris, France", ["monument"]]
)
print(smills_france)