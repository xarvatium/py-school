import requests
import wikipedia
import random
import webbrowser
import json



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
            getPage()
    elif(userinput == "z" or userinput == "Z"):
        exit()
    else:
        exit()
getPage()