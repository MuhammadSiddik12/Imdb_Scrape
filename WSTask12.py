### Scrape a movie details and find there name and there imdb ID ###

import requests        
from bs4 import BeautifulSoup as s  
from pprint import pprint
import json
from WSTask5 import *
from WSTask import *
def movie_li(movie,movie_link):
    list1=[]
    list_main=[]
    for i in movie_link:
        link=i['movie_link']
        p=main_file(link,movie)
        list_main.append(p)
    return list_main
def main_file(link,movie):
    d={}
    list1=[]
    page=requests.get(link) 
    soup=s(page.text,"html.parser")
    body=soup.find('body')
    table=body.find('table',class_="cast_list")
    actors_name=table.findAll('td',class_='')
    for i in actors_name:
        d['name']=i.find('a').text.split('\n')[0]
        d['imdb_id']=i.find('a')['href'].split('/')[2]
        list1.append(d.copy())
    return list1
    # for i in movie:
    #     name_=i['movie_link'].split('/')[4]
    #     name=name_+'_cast'+'.json'
    #     with open(name,'w') as f:
    #         f.write(json.dumps(i,indent=4))
    #         f.close()
movie_li(get_movie_list_details(scrape_top_list()),scrape_top_list())