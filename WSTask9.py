### Scrape a movies links and make a file with there link ID by taking some pause ###

from WSTask import *
import json,os,random,time
def imdb_id(fi,name):
    random_sleep=random.randint(5,10)
    for i in range(len(fi)):
        file_name=fi[i]+'.json'
        if os.path.exists('/home/navgurukul/Downloads/jsonData/'+file_name):
            with open('/home/navgurukul/Downloads/jsonData/'+file_name,'r') as f:
                print(f.read())
                f.close()
        else:
            time.sleep(random_sleep)
            with open('/home/navgurukul/Downloads/jsonData/'+file_name,'w') as f:
                f.write(json.dumps(name[i],indent=4))
                f.close()

def check_file_exits_or_not(movies):
    list1=[]
    for i in movies:
        list1.append(i['movie_link'].split('/')[-2])
    imdb_id(list1,movies)
check_file_exits_or_not(scrape_top_list())