#https://www.pingshiuanchua.com/blog/post/collecting-analysing-google-home-reviews-with-python
#https://www.pingshiuanchua.com/blog/category/python/web-scraping/
#https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
#http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()

query="banana loaf"
number_result=5

google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")

result_div = soup.find('div', attrs = {'class': 'gc'}).get_text()
print(len(result_div))

links = []
titles = []
descriptions = []
for r in result_div:
    try:
        link = r.find('a', href = True)
        title = r.find('h3', attrs={'class': 'r'}).get_text()
        description = r.find('span', attrs={'class': 'st'}).get_text()
        
        if link != '' and title != '' and description != '':
            links.append(link['href'])
            titles.append(title)
            descriptions.append(description)
    except:
        continue

import re   

to_remove = []
clean_links = []
for i, l in enumerate(links):
    clean = re.search('\/url\?q\=(.*)\&sa',l)
    if clean is None:
        to_remove.append(i)
        continue
    clean_links.append(clean.group(1))
    
for x in to_remove:
    del titles[x]
    del descriptions[x]
    