### Scrape a movie casts and check that actors acts in how many movie ###

from WSTask13 import *
from pprint import pprint
def analyse_actors(movies_list):
	main=[]
	movies=[]
	for i in movies_list:
		actors_dict = {}
		for actor in i['cast']:
			no_flag = 0
			for Cast in i['cast']:
				if actor['name'] == Cast['name']:
					no_flag +=1
			actors_dict[actor['imdb_id']] = {'name':actor['name'],'num_movies':no_flag}
		main.append(actors_dict.copy())
	for i in range(len(movies_list)):
		movies_list[i].update(main[i])
	for j in movies_list:
		movies.append([j])
	# with open('s.json','w') as e:
	# 	e.write(json.dumps(movies,indent=4))
	# 	e.close()
analyse_actors(scrape_movie_cast(movie_li(get_movie_list_details(scrape_top_list()),scrape_top_list()),get_movie_list_details(scrape_top_list())
))