#shows reviews, 1 to 5, so we need to loop n/5 times, n total number of reviews
#URL_BaseVPE:           https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS
#URL_Next_5_reviews_SP: https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS

#URL_BaseLNB: https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS
#URL_Next_5_reviews__LNB:: https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-or5-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS

#REVIEWS SP ITEM


#REVIEWS LNB ITEM 
#5 star review: <span class="_1jcHBWVU _1-HtLqs3 uq1qMUbD"></span>
#4 star review: <span class="_1jcHBWVU _2vB__cbb uq1qMUbD"></span>

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def reviewCounter(soup, url):
    
    if not soup:
        print('[parse] no soup:', url)
        return
    num_reviews = soup.find('span', class_='_82HNRypW').text
    space_ubication = num_reviews.search(" ")
    num_reviews[0:space_ubication]
    print('num_reviews ALL:', int(num_reviews))
    return num_reviews

ua = UserAgent() #I do not get this. CHECK

query="banana%20loaf"
number_result=5
#google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)


google_url = "https://www.tripadvisor.es/Attraction_Review-g186525-d2042818-Reviews-or5-Viajar_Por_Escocia_Tours_en_Espanol-Edinburgh_Scotland.html#REVIEWS"
google_url = "https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS"

response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "lxml")

number_reviews = reviewCounter(soup, google_url)

#first loop to cover all the reviews https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS
url_reviews = "https://www.tripadvisor.co.uk/AttractionProductReview-g186525-d19148502-or5-Loch_Ness_Glencoe_The_Highlands_from_Edinburgh-Edinburgh_Scotland.html#REVIEWS"
string_to_search = "-or"
reviews_integer = int(number_reviews)/(5)
list = range(2, )
url_to_call = []
for l in list:
    new_url_review.replace(string_to_search, string_to_search + (n*5))
    url_to_call.append(new_url_review)
    
len(url_to_call)
print(url_to_call)
    
#All the information per review
# result_div = soup.find_all('div', {"class": "location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw"})
# result_div = soup.find_all('div', {"class": "_1T1U92WJ"})
# 
# print("total divs ",len(result_div))
# 
# 
# review_value = []
# writer = []
# title = []
# description = []
# for r in result_div:
#     try:
# #         print(r)
# #         #review value
# #         rv_aux = r.find('div', {'class': 'location-review-review-list-parts-RatingLine__bubbles--GcJvM'})
# #         rv_aux = review_value.append(rv_aux.find('span')).get_text()
# #         print(rv_aux)
# #         rv_aux = rv_aux[:2]
# #         review_value.append(rv_aux)
# #         
# #         #shows revewer + date of review
# #         writer.append(r.find('a', attrs={'class': 'ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC'}).get_text())
# #         #review title
# #         title.append(r.find('a', attrs={'class': 'location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT'}).get_text())
# #         #review.
# #         description.append(r.find('q', attrs={'class': 'location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'}).get_text())
#         
#         #stars value; html generated does not show the result of the review
#         review_value.append(r.find('div', {'class': '_2cyNVhH_'}))
#         #shows revewer + date of review
#         writer.append(r.find('a', attrs={'class': '_1e-v2VZJ _3I1Aup9d'}).get_text())
#         #review title
#         title.append(r.find('a', attrs={'class': '_1xr4qUQI'}).get_text())
#         #review text
#         description.append(r.find('div', attrs={'class': 'cPQsENeY'}).get_text())
#         #
#     except:
#         continue
#  
# for rv in review_value:
#     print(rv.find('span'))
#  
# for wr in writer:
#     print(wr)
#  
# for t in title:
#     print(t)
# 
# #check if review fishines with 3 dots. In that case remove last sentence until previous dot
# for d in description:
#     print(d)
#      
    
# for w in writer:
#     print(w)
#     print(title[n])
#     print(description[n])
#     ++n

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
