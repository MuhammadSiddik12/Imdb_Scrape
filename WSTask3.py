### Scrape a movies year and place them with decades ###

from WSTask2 import *
import json
def group_by_decade(movies):
    list1=[]
    movies_dc={}
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movies_dc[i]=[]
    for i in movies_dc:
        dec=i+9
        for x in movies:
            if x<=dec and x>=i:
                for v in movies[x]:
                    movies_dc[i].append(v)

    # with open('d.json','w') as f:
    #     f.write(json.dumps(movies_dc,indent=4))
    #     f.close()
group_by_decade(group_by_year(scrape_top_list()))