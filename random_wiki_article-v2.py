import requests, wikipedia, random, webbrowser, json, sys
from os import path

def getPage():
    # Defines the variables to be used
    wikipage = wikipedia.random(1)
    wikiload = wikipedia.page(wikipage)

    # Asks for the user input if they would like to read about a Wikipedia page
    userinput = input("Would you like to read about {}? (Y/N/Z) ".format(wikipage))

    # The If statement that checks if they responded with 'Y' or 'N'
    if(userinput == "Y" or userinput == "y"):
        # Prints the summary of the Wikipedia page
        print("\nSummary:\n------------\n" + wikipedia.summary(wikipage))
        # Asks if the user would like to open it in their browser
        wikiopen = input("\nOpen Wiki page in browser? (Y/N) ")
        if(wikiopen == "Y" or wikiopen == "y"):
            webbrowser.open(wikiload.url,new=2)
        else:
            pass
    elif(userinput == "z" or userinput == "Z"):
        exit()
    else:
        pass
    # Defines the variable "favorites" as JSON data
    favorites = {
        'Favorites': [ {
            'Title': wikipedia.page(wikipage).title,
            'Summary': wikipedia.summary(wikipage),
            'URL': wikiload.url,
            }
        ]
    }
    if path.exists('favorites.json'):
        with open('favorites.json') as favraw:
            favorites = json.load(favraw)
    else:
        favorites = []

    newfav = {"Title": wikipedia.page(wikipage).title, "Summary": wikipedia.summary(wikipage), "URL": wikiload.url}
    fav_answer = input("Would you like to add {} as a favorite? (Y/N) ".format(wikipage))
    if ("Y" in fav_answer or "y" in fav_answer):
        favorites.append(newfav)
        with open('favorites.json','w') as favraw:
            json.dump(favorites, favraw, indent=4, ensure_ascii=False)
        print("Page saved! Please check your favorites.json file, or the one that was just made, to see your favorites!")
        getPage()
    else:
        getPage()
getPage()