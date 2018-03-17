import random

dict1 = {
			'It\'s Always Sunny in Philladelphia':[12, 15],
			'The Office':[9, 26],
			'Seinfeld':[9, 24],
			'Parks and Rec':[7, 24],
			'Curb your Enthusiasm':[9, 10]
			}

class Modules():
	def collection():
		GData = dict1
		return GData

	def menu():
		options = ['Choose Show', 'Add Show', 'Quit']
		for number, items in enumerate(options, 1):
			print(number, items)

	trying = 0
	def randomizer(trying):
		
		Season = Modules.collection()[trying][0]
		Episode = Modules.collection()[trying][1]	
		
		r_season = random.randint(1, Season)
		r_episode = random.randint(1, Episode)

		print('\n\nYou selected:', trying,'S', r_season,'E', r_episode)

	def repeater(selectedShow):
		repeat = 0
		while repeat == 0:
			another_ep = input('\nDo you want another episode?(Yes/No) _ ').lower()
			if another_ep == 'yes':
				Modules.randomizer(selectedShow)
			elif another_ep == 'no':
				print('\nOK.')
				break
			else:
				print('\nNot quite right, mate.')

#User updates:
dict1.update({'Rick and Morty': [3, 10]})
dict1.update({'Master of None': [2, 10]})
dict1.update({'BoJack Horseman': [4, 12]})
dict1.update({'Silicon Valley': [4, 10]})
dict1.update({'Arrested Development': [4, 22]})
