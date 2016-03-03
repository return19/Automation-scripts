from bs4 import BeautifulSoup
import urllib2
import urllib
import random
import math
import os

quote_fancy_url="https://quotefancy.com/inspirational-entrepreneurship-quotes"
quote_fancy_url_base="https://quotefancy.com"

page=urllib2.urlopen(quote_fancy_url);
soup=BeautifulSoup(page);

#print soup.prettify()

all_wallpapers=soup.findAll('div',{'class':'wallpaper scrollable'})

#print all_wallpapers;

res=[]
# retrieving links of wallpapers
for i in range(len(all_wallpapers)) :
	ans = all_wallpapers[i].find_all('img')
	if ans[0].get('src') :
		res.append(ans[0].get('src'))
	else :
		res.append(ans[0].get('data-original'))

#randomly selecting image url from res
number_of_wallpapers = len(res)
selected_index= int(math.floor((number_of_wallpapers-1)*random.random()))
#downloading selected wallpaper
urllib.urlretrieve(quote_fancy_url_base + res[selected_index], "/home/abhinandan/latest_wall.jpg")
# Changing desktop wallpaper
os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/abhinandan/latest_wall.jpg")