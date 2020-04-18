#https://www.pingshiuanchua.com/blog/post/collecting-analysing-google-home-reviews-with-python
#https://www.pingshiuanchua.com/blog/category/python/web-scraping/
#https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
#http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/

#base url to take number of reviews, n
#shows reviews, 1 to 5, so we need to loop n/5 times, n total number of reviews
#URL_BaseSP:           https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
#URL_Next_5_reviewsSP: https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
#URL_BaseEN: https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
#URL_Next_5_reviewsSP: https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import google

ua = UserAgent() #I do not get this. CHECK

query="banana%20loaf"
number_result=5
#google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)


google_url = "https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS"

response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "lxml")

#All the information per review
result_div = soup.find_all('div', {"class": "location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw"})
print("total divs ",len(result_div))

writer = []
title = []
description = []
for r in result_div:
    try:
        #shows revier + date of review
        writer.append(r.find('a', attrs={'class': 'ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC'}).get_text())
        #review title
        title.append(r.find('a', attrs={'class': 'location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT'}).get_text())
        #review.
        description.append(r.find('q', attrs={'class': 'location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'}).get_text())
        #
    except:
        continue
n=0
for w in writer:
    print(w)
    print(title[n])
    print(description[n])
    ++n

# import re   
# 
# 
# to_remove = []
# clean_links = []
# for i, l in enumerate(links):
#     clean = re.search('\/url\?q\=(.*)\&sa',l)
#     if clean is None:
#         to_remove.append(i)
#         continue
#     clean_links.append(clean.group(1))
#     
# for x in to_remove:
#     del titles[x]
#     del descriptions[x]
#     
