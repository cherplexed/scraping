# shows reviews, 1 to 5, so we need to loop n/5 times, n total number of reviews. TA use a combination for the totals reviews between TA and viator
# URL_BaseVPE:           https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
# URL_Next_5_reviews_SP: https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS

# URL_BaseLNB: https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS
# URL_Next_5_reviews__LNB:: https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-or5-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS

# REVIEWS SP ITEM

# REVIEWS LNB ITEM 
# 5 star review: <span class="_1jcHBWVU _1-HtLqs3 uq1qMUbD"></span>
# 4 star review: <span class="_1jcHBWVU _2vB__cbb uq1qMUbD"></span>

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import numpy as np


def reviewCounter(soup, url):
    
    if not soup:
        print('[parse] no soup:', url)
        return
    num_reviews = soup.find('span', class_='_82HNRypW').text
    space_ubication = num_reviews.find(" reviews")
    num_reviews = num_reviews[0:space_ubication]
    return num_reviews


ua = UserAgent()  # I do not get this. CHECK

query = "banana%20loaf"
number_result = 5
# google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)

google_url = "https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS"
google_url = "https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html"

response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "lxml")

number_reviews = reviewCounter(soup, google_url)

# first loop to cover all the reviews https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS
url_reviews = "https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-or-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS"
string_to_search = "-or"
number_reviews = int(number_reviews)
# we force the value to scrap the reviews as the number showed in TA is the addition between TA and viator.
number_reviews = 10
reviews_integer = int((number_reviews) / (5))
print(reviews_integer)
list = range(0, (reviews_integer))
url_to_call = []
for l in list:
    if l == 0:
        url_to_call.append("https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS")
    else:
        url_to_call.append(url_reviews.replace(string_to_search, string_to_search + str(l * 5)))

# we generate one soap per page

    review_value = []
    date = []
    writer = []
    title = []
    description = []
for url in url_to_call:
    response = requests.get(url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "lxml")

    # All the information per review
    result_div = soup.find_all('div', {"class": "location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw"})
    result_div = soup.find_all('div', {"class": "_1T1U92WJ"})
    for r in result_div:
        try:
            # stars value; html generated does not show the result of the review. we compare the class value to know the numeric review value
            value_to_compare = (r.find('div', {'class': '_2cyNVhH_'}))
            new_value = str(value_to_compare.find('span'))
            if (new_value.find("2vB__cbb") != -1):
                review_value.append(5)
            elif(new_value.find("1-HtLqs3") != -1):
                review_value.append(4)
            else:
                review_value.append(3)
            #datereview
            aux = r.find('div', attrs={'class': '_3mCNwHy0'}).get_text()
            aux = aux[int(aux.find("review"))+7:]
            date.append(aux)
            # shows revewer + date of review
            writer.append(r.find('a', attrs={'class': '_1e-v2VZJ _3I1Aup9d'}).get_text())
            # review title
            title.append(r.find('a', attrs={'class': '_1xr4qUQI'}).get_text())
            # review text
            # check if review fishines with 3 dots. In that case remove last sentence until previous dot
            review_description = r.find('div', attrs={'class': 'cPQsENeY'}).get_text()
            review_description[:]
            review_description = 
            description.append()
            # add all values in one array
            np.Array([review_value[-1], date[-1],writer[-1], title[-1], description[-1]])
        except:
            continue

for rv in review_value:
    print(rv)
     
for d in date:
    print(d)
   
for wr in writer:
     print(wr)
   
for t in title:
     print(t)

for d in description:
     print(d)
 
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

# SPANISH TAGS WORKING
# for r in result_div:
#     try:
 #         print(r)
 #         #review value
 #         rv_aux = r.find('div', {'class': 'location-review-review-list-parts-RatingLine__bubbles--GcJvM'})
 #         rv_aux = review_value.append(rv_aux.find('span')).get_text()
 #         print(rv_aux)
 #         rv_aux = rv_aux[:2]
 #         review_value.append(rv_aux)
 #         
 #         #shows revewer + date of review
 #         writer.append(r.find('a', attrs={'class': 'ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC'}).get_text())
 #         #review title
 #         title.append(r.find('a', attrs={'class': 'location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT'}).get_text())
 #         #review.
 #         description.append(r.find('q', attrs={'class': 'location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'}).get_text())
