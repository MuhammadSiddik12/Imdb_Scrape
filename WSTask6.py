### Scrape a movies details and anslise the same languges from all the movies ###

from WSTask5 import *
def analise_movie_language(movies):
    list1=[]
    list2=[]
    a={}
    for i in movies:
        list1.append(i['language'])
    for i in list1:
        for m in i:
            list2.append(m)
    for f in list2:
        c=0
        for j in list2:
            if f==j:
                c+=1
        a[f]=c
    return a
analise_movie_language(get_movie_list_details(scrape_top_list()))