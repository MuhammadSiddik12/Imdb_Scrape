### Scrape a movie cast and add to the main dictionary ###

from WSTask12 import *
from WSTask5 import *
from pprint import pprint
def scrape_movie_cast(cast_name,main):
    for i in range(len(main)):
        dic={}
        dic['cast']=cast_name[i]
        main[i].update(dic.copy())
    return main
    # with open('main.json','w') as f:
    #     f.write(json.dumps(main,indent=4))
    #     f.close()
scrape_movie_cast(movie_li(get_movie_list_details(scrape_top_list()),scrape_top_list()),get_movie_list_details(scrape_top_list())
)