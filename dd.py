import nltk
import tkinter as tk
from textblob import TextBlob
from newspaper import Article


def summarize():
    url = utext.get('1.0', 'end').strip()
    myArticle = Article(url, language = 'en')
    #download link
    myArticle.download()
    myArticle.parse()
    myArticle.nlp()

    title.config(state= 'normal')
    Authors.config(state= 'normal')
    publication_date.config(state= 'normal')
    summary.config(state= 'normal')
    sentiment.config(state= 'normal')
     
    title.delete('1.0', 'end')
    title.insert('1.0', myArticle.title) 

    Authors.delete('1.0', 'end')
    Authors.insert('1.0', myArticle.authors) 

    publication_date.delete('1.0', 'end')
    publication_date.insert('1.0', myArticle.publish_date) 

    summary.delete('1.0', 'end')
    summary.insert('1.0', myArticle.summary) 

     

    # sentiment analysis
    analysis = TextBlob(myArticle.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'polarity : {analysis.polarity}, Sentiment :{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
    title.config(state= 'disabled')
    Authors.config(state= 'disabled')
    publication_date.config(state= 'disabled')
    summary.config(state= 'disabled')
    sentiment.config(state= 'disabled')


#GUI DRAWING

root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height = 1, width = 140)
title.config(state='disabled', bg='#dddddd')
title.pack()


alabel = tk.Label(root, text='Authors')
alabel.pack()

Authors = tk.Text(root, height = 1, width = 140)
Authors.config(state='disabled', bg='#dddddd')
Authors.pack()

blabel = tk.Label(root, text='Publication date')
blabel.pack()

publication_date = tk.Text(root, height = 1, width = 140)
publication_date.config(state='disabled', bg='#dddddd')
publication_date.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height = 20, width = 140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

snlabel = tk.Label(root, text='Sentiment analysis')
snlabel.pack()

sentiment = tk.Text(root, height = 1, width = 140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()


ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height = 1, width = 140)
utext.pack()

btn = tk.Button(root, text = 'Summarize', command= summarize)
btn.pack()





root.mainloop()














