# Working with Python Lists
from pyscript import document


# List of East Asian countries
countries = [
    "China",
    "Japan",
    "South Korea",
    "North Korea",
    "Mongolia",
    "Taiwan"
]

# List of nicknames matching each country
nicknames = [
    "The Middle Kingdom",
    "The Land of the Rising Sun",
    "The Land of the Morning Calm",
    "The Hermit Kingdom",
    "The Land of the Eternal Blue Sky",
    "The Beautiful Island"
]

def show_nn(e):
    # Get the selected country
    country = document.getElementById("country").value

    # Check if a country was selected
    if country in countries:

        # Find the position of the country
        index = countries.index(country)

        # Get the matching nickname
        nickname = nicknames[index]

        # Display the nickname
        document.getElementById("result").innerHTML = nickname

    else:

        # Display a message if no country was selected
        document.getElementById("result").innerHTML = "Please choose a country."