#https://www.pingshiuanchua.com/blog/post/collecting-analysing-google-home-reviews-with-python
#https://www.pingshiuanchua.com/blog/category/python/web-scraping/

import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
#from test.support.testresult import result

query = "trade war"
query = urllib.parse.quote_plus(query) # Format into URL encoding
number_result = 20

ua = UserAgent()

google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")

if(soup):
    print(soup.tittle)
    result_div = soup.find_all('div', attrs = {'class': 'KJDcUb'})
    print(len(result_div))
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        print("inside loop")
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href = True)
            title = r.find('div', attrs={'class':'PpBGzd YcUVQe'}).get_text()
            description = r.find('div', attrs={'class':'MUxGbd yDYNvb'}).get_text()
        
            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '': 
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
                # Next loop if one element is not present
        except:
            continue
        