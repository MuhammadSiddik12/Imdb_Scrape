### Scrape a full movie details ###

import requests
from bs4 import BeautifulSoup
from pprint import pprint   

url = "https://www.imdb.com/title/tt0048473/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=QHR2NNP8ES32ZYX3NE9T&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1"
page = requests.get(url)
soup =  BeautifulSoup(page.text, "html.parser")

def scrape_movie_details() :
    d={}
    main_body = soup.find('body')
    d['name'] = main_body.find('div' , class_ = 'title_wrapper').h1.text[:-8]
    d['year'] = main_body.find('div',class_='title_wrapper').h1.span.text[1:5]
    subtext = main_body.find('div', class_ = 'subtext').time.text.strip() 
    time = int(subtext[0])*60
    e=subtext.split(' ')
    f=e[1].split('min')[-2]
    d['time_main'] = time + int(f) 
    d['genre'] = main_body.find('div', class_ = 'subtext').a.text
    d['bio']=main_body.find('div',class_="plot_summary").div.text.strip()
    d['director']=main_body.find('div',class_="plot_summary").find('div',class_='credit_summary_item').a.text
    d['country']=main_body.find_all('div',class_="txt-block")[5].text.strip().split('\n')[1]
    d['language']=main_body.find_all('div',class_="txt-block")[6].text.strip().split('\n')[1]
    return d
scrape_movie_details())