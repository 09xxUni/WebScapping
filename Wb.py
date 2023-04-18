from bs4 import BeautifulSoup

import requests
for page in range(0,240,10):

    url=f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&start={page}"

    
    data=requests.get(url)

    soup=BeautifulSoup(data.content,"html.parser")

    rdata = soup.find_all('li',class_="border-color--default__09f24__NPAKY")

    yelpdata_list=[]

    for d in rdata:

        restaurant = d.find('a',class_="css-19v1rkv")
        rating=d.find('span',class_="css-chan6m")

        if restaurant==None :
            continue

        else:
            restaurant=restaurant.text
        if rating==None:
            continue
        else:
            rating=rating.text
        yelpdata_list.append([restaurant,rating])

        
        
    for data in yelpdata_list:
        print(data)
