### Scrape a movies year in sperate by years ###

from WSTask import *
def group_by_year(movies) :
    years = []
    for i in movies : 
        year =  i ['year']
        if year not in years : 
            years.append(year)
    movie_dict = {i:[] for i in years}
    years.sort()
    for i in movies  :
        year = i ['year']
        for x in movie_dict :
            if str(x) == str(year) :
                movie_dict[x].append(i)
    return movie_dict
group_by_year(scrape_top_list())
                          

        



