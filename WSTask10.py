### Scrape a movies and analyse there languges and directors ###

from WSTask5 import *
def analyse_language_and_directors(movies_list):
    director_dic={}
    for movie in movies_list:
        for director in movie['director']:
            director_dic[director]={}
    for i in range(len(movies_list)):
        for director in director_dic:
            if director in movies_list[i]['director']:
                for language in movies_list[i]['language']:
                    director_dic[director][language]=0
    for i in range(len(movies_list)):
        for director in director_dic:
            if director in movies_list[i]['director']:
                for language in movies_list[i]['language']:
                    director_dic[director][language]+=1
    return director_dic
print(analyse_language_and_directors(get_movie_list_details(scrape_top_list())))