### Scrape a movies details and get a gerne list ###

from WSTask5 import *
def gerne_list(movies):
    list1=[]
    a={}
    for i in movies:
        list1.append(i['gerne'])
    for f in list1:
        c=0
        for j in list1:
            if f==j:
                c+=1
        a[f]=c
    return a 
gerne_list(get_movie_list_details(scrape_top_list()))