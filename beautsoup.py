import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface').read()

soup = bs.BeautifulSoup(source, 'lxml')

print(soup)
#print(soup.title)          # prints everything enclosed in <title> brackets
#print(soup.title.string)   # prints

print(soup.p)               # prints first paragraph
#print(soup.find_all('p'))   # finds all the paragraph tags to print

for paragraph in soup.find_all('p'):
    print(paragraph.text)       # string throws none if there are child tags, text just prints the plaintext

print(soup.get_text())      # prints all plaintext

for url in soup.find_all('a'):  # 'a' tag is for links/urls
    print(url.get('href'))
