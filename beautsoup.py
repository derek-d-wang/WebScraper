import bs4 as bs
import urllib.request
import pandas as pd

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface').read()

soup = bs.BeautifulSoup(source, 'lxml')

# pt 1
#print(soup)
#print(soup.title)          # prints everything enclosed in <title> brackets
#print(soup.title.string)   # prints

#print(soup.p)               # prints first paragraph
#print(soup.find_all('p'))   # finds all the paragraph tags to print

#for paragraph in soup.find_all('p'):
#    print(paragraph.text)       # string throws none if there are child tags, text just prints the plaintext

#print(soup.get_text())      # prints all plaintext

#for url in soup.find_all('a'):  # 'a' tag is for links/urls
#    print(url.get('href'))

# pt 2
nav = soup.nav

#for url in nav.find_all('a'):
#    print(url.get('href'))

#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)

#for div in soup.find_all('div', class_ = 'body'):
#    print(div.text)         # Prints all text between <div> tags


# pt 3
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface',header = 0)
for df in dfs:
    print(df)           # using pandas, search for and print all the dataframes on the site

