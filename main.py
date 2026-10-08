from pyscript import document

# Nicknames of East Asian countries
nicknames = {
    "China": "The Middle Kingdom",
    "Japan": "The Land of the Rising Sun",
    "South Korea": "The Land of the Morning Calm",
    "North Korea": "The Hermit Kingdom",
    "Mongolia": "The Land of the Eternal Blue Sky",
    "Taiwan": "The Beautiful Island"
}


def show_nn(event):
    # Getting the selected country
    country = document.getElementById("country").value

    # Finding the nickname
    if country in nicknames:
        nickname = nicknames[country]
    else:
        nickname = "Please choose a country."

    # Displaying the nickname
    document.getElementById("result").innerHTML = nickname