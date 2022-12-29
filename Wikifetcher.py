from tkinter import *
from bs4 import BeautifulSoup
import requests

root = Tk()
root.title("Wikipedia Random Article")

frame = Frame(root, bg="lightgrey")
frame.pack(padx=10, pady=10)

title_label = Label(frame, text="Wikipedia Random Article", font =('Helvetica',18,'bold'), bg="lightgrey")
title_label.pack()

url_label = Label(frame, text="")
url_label.pack()

def fetch_article():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find('h1').text
    content = soup.find('div', {'class': 'mw-parser-output'})
    url_label['text'] = url
    title_label['text'] = title
    article_box.delete('1.0', END)
    article_box.insert('1.0', content.text)

article_frame = Frame(frame, width=600, height=350, bg="lightgrey")
article_frame.pack()

scrollbar = Scrollbar(article_frame)
scrollbar.pack(side=RIGHT, fill=Y)

article_box = Text(article_frame, width=60, height=15, wrap=WORD, font=('Arial', 12))
article_box.pack()

article_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=article_box.yview)

fetch_button = Button(frame, text="Fetch Random Article", bg='steelblue', fg='white', command=fetch_article)
fetch_button.pack(pady = 10)

copy_button = Button(frame, text="Copy Article URL", bg='steelblue', fg='white', command=lambda: root.clipboard_append(url_label["text"]))
copy_button.pack(pady = 10)

open_button = Button(frame, text="Open in Browser", bg='steelblue', fg='white', command=lambda: webbrowser.open_new(url_label["text"]))
open_button.pack(pady = 10)

clear_button = Button(frame, text="Clear Article", bg='steelblue', fg='white', command=lambda: article_box.delete('1.0', END))
clear_button.pack(pady = 10)

save_button = Button(frame, text="Save Article", bg='steelblue', fg='white', command=lambda: save_article())
save_button.pack(pady = 10)

def save_article():
    file_name = title_label["text"]+".txt"
    f = open(file_name, "w", encoding="utf-8")
    f.write(article_box.get('1.0', END))
    f.close()

root.geometry("800x600")

frame.pack(padx=20, pady=20)

nav_frame = Frame(root, bg='darkblue', width=800, height=20)
nav_frame.pack(side=TOP, fill=X)

fetch_button = Button(nav_frame, text="Fetch Article", bg='darkblue', fg='white', command=fetch_article)
fetch_button.pack(side=LEFT)

copy_button = Button(nav_frame, text="Copy URL", bg='darkblue', fg='white', command=lambda: root.clipboard_append(url_label["text"]))
copy_button.pack(side=LEFT)

open_button = Button(nav_frame, text="Open in Browser", bg='darkblue', fg='white', command=lambda: webbrowser.open_new(url_label["text"]))
open_button.pack(side=LEFT)

clear_button = Button(nav_frame, text="Clear Article", bg='darkblue', fg='white', command=lambda: article_box.delete('1.0', END))
clear_button.pack(side=LEFT)

save_button = Button(nav_frame, text="Save Article", bg='darkblue', fg='white', command=lambda: save_article())
save_button.pack(side=LEFT)

fetch_button.config(relief=RIDGE, bd=2)
copy_button.config(relief=RIDGE, bd=2)
open_button.config(relief=RIDGE, bd=2)
clear_button.config(relief=RIDGE, bd=2)
save_button.config(relief=RIDGE, bd=2)

title_label['font'] = ('Helvetica', 22, 'bold')
title_label['fg'] = 'darkblue'

root.mainloop()
