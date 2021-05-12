### Scrape a movive details like name, positon, year of releasing, rating, movielink ###

import requests
from bs4 import BeautifulSoup
from pprint import pprint   
page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup =  BeautifulSoup(page.text, "html.parser")

def scrape_top_list() :
    details={}
    top_movies_details=[]
    main_div = soup.find('div', class_ = 'lister')
    tbody = main_div.find("tbody", class_ = "lister-list")
    trs = tbody.find_all("tr")
    for i in trs : 
        details['name']=i.find('td',class_="titleColumn").a.text
        details['position'] = i.find("td" , class_ = "titleColumn").text.strip().split('.')[0]
        details['year'] = int(i.find('td' , class_ = "titleColumn").span.text[1:5])
        details['imdb_rating'] = i.find('td', class_ = "ratingColumn imdbRating").strong.text
        details['movie_link'] = "http://www.imdb.com" + i.find('td' , class_ = 'titleColumn').a['href']
        top_movies_details.append(details.copy())
    return top_movies_details
scrape_top_list()