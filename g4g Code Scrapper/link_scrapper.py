from bs4 import BeautifulSoup
import urllib2
import urllib
from code_scrapper import *

g4g="http://www.geeksforgeeks.org/fundamentals-of-algorithms/"

page=urllib2.urlopen(g4g);
soup=BeautifulSoup(page);

entry_content=soup.findAll('div',{'class':'entry-content'})

algo_links=entry_content[0].find_all('ul')

links_to_be_opened = []

#Saves all thr links of algorithms' pages in array
for i in range(1,len(algo_links)):
	li=algo_links[i].find_all('li')
	for j in range(len(li)):
		li[j]=li[j].contents[0].get('href')
		links_to_be_opened.append(li[j])

text_file=open("g4g.txt","a")

for i in range(len(links_to_be_opened)):
	scrapCodeToFile(text_file,links_to_be_opened[i])
	print "Saving Code from link number : " + str(i+1) + "/" + str(len(links_to_be_opened))
text_file.close()