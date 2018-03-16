import random
import lib.collection as collection

trying = 0
def randomizer(trying):
	
	Season = collection.Collection()[trying][0]
	Episode = collection.Collection()[trying][1]	
	
	r_season = random.randint(1, Season)
	r_episode = random.randint(1, Episode)

	print('\n\nYou selected:', trying,'S', r_season,'E', r_episode)