from bs4 import BeautifulSoup
import requests as rq

url = "https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=jsonp&lang=en&jsonp=?"

result = rq.get(url)
doc = BeautifulSoup(result.text, "html.parser")

fullText = doc.get_text()

quoteStart = fullText.index(":") + 1
quoteEnd = fullText.index("\"", quoteStart + 1) + 1

authorStart = fullText.index(":", quoteEnd + 1) + 2
authorEnd = fullText.index("\"", authorStart + 1)

quote = fullText[quoteStart:quoteEnd]
if fullText[authorStart] == "\"":
    author = "Anonymous"
else: 
    author = fullText[authorStart:authorEnd]

def removeSlash(quote):
    while "\\" in quote:
        ind = quote.index("\\")
        quote = quote[0:ind] + quote[ind+1:-1]

def formatQuote(quote, author):
    return quote + " - " + author

removeSlash(quote)

print(formatQuote(quote, author))
print(author)