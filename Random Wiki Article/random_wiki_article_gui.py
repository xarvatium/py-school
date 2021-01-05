import tkinter as tk
import wikipedia
import webbrowser
import json
from os import path

window = tk.Tk()
window.title("Random Wikipedia Article Generator")
window.geometry("350x400")
window.configure(bg="gray")
disclaim = tk.Label(text = "Disclaimer: This is still in development so expect bugs", fg="red", bg="gray")
disclaim.grid(column=0,row=19)
def getPage():
    global wikipage
    wikipage = wikipedia.random(1)
    article = wikipedia.summary(wikipage)
    text_area = tk.Text(master=window,height=15,width=40)
    text_area.grid(column=0,row=5)
    text_area.insert(tk.END,article)
def openWeb():
    global wikiload
    wikiload = wikipedia.page(wikipage)
    webbrowser.open(wikiload.url, new=2)

def saveFav():
    favorites = {
        'Favorites': [{
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
    favorites.append(newfav)
    with open('favorites.json', 'w') as favraw:
        json.dump(favorites, favraw, indent=4, ensure_ascii=False)


button1 = tk.Button(text="Generate a Wiki Article",bg="gray",command=getPage)
button1.grid(column=0,row=1)
button2 = tk.Button(text = "Save to Favorites",bg="gray",command=saveFav)
button2.grid(column=0,row=2)
button3 = tk.Button(text = "Open in Web Browser",bg="gray",command=openWeb)
button3.grid(column=0,row=3)
label = tk.Label(text="I know some of the dimensions are weird\n but it's difficult to get exact measurements")
label.grid(column=0,row=4)
label.configure(bg="gray")

window.mainloop()

