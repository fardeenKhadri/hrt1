#urlshortner
import pyshorteners

url = input('Enter the URL: ')

def shorten(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shorten(url)
