from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import HTMLParser


def scrapCodeToFile(text_file,alog_page):
	#alog_page="http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/"
	page=""
	try :
		page = urllib2.urlopen(alog_page)
	except Exception:
   		 return
	
	soup=BeautifulSoup(page);

	#print soup.prettify()

	entry_header=soup.findAll('h1',{'class':'entry-title'})

	if len(entry_header) == 0:
		return
	entry_header=entry_header[0].contents

	if len(entry_header) == 0:
		return

	entry_header=entry_header[0].encode('utf-8')

	# entry_header=entry_header[0].contents[0].encode('utf-8')

	entry_content=soup.findAll('pre',{'class':re.compile(r".*\bcpp\b.*")})
	
	if len(entry_content) !=0 :
		text_file.write("%s \n\n" % entry_header) 

	for i in range(len(entry_content)):
		entry_content[i]=entry_content[i].contents
		text_file.write("%s \n\n\n\n" % entry_content[i][0].encode('utf-8'))
