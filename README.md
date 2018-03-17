# Project 1:

This is my first Python project.

I intend to update it as i learn new cool stuff

## Here is the code:

### The main part:

```
import lib.modules as m

try:
	print('''
			______________________________________
			Welcome to the Random Episode Chooser!
				''')
	m.Modules.menu()

	option = int(input('\nChoose your number: _ '))-1

	if option == 0:
		Shows = list(m.Modules.collection().keys())

		print('\n')
		for number, values in enumerate(Shows, 1):
			print(number, values)

		nselected = []
		while nselected == []:
			userShow = input('\nChoose your show\'s number(or anything else to quit): _ ')
			nselected = int(userShow)-1
				
			if nselected > len(Shows):
				print('Wrong number, please choose again.')
				nselected = []
				
			else:
				selectedShow = Shows[nselected]
					
				m.Modules.randomizer(selectedShow)
				m.Modules.repeat(selectedShow)
		
	elif option == 1:
		addShow = input('\nDo you want to add a new show?(Yes/No) _ ').lower()

		if addShow == 'yes':
			newShow = str(input('\nShow\'s name: _ '))
			newShow_s = int(input('Number of Seasons: _ '))
			newShow_e = int(input('Number of episodes per season: _ '))
			print('\n')

			dict2 = {newShow:[newShow_s, newShow_e]}
			
			with open('lib/modules.py','a') as f:
				f.write('\ndict1.update('+str(dict2)+')')
				f.close()
			
		elif addShow == 'no':
			print('\nOK.')
			
		else:
			print('\nI\'ll consider that a NO.')
							
	elif option == 2:
		pass

	else:
		print('\nNot an option')

except Exception as e:
	print('\nExiting.', e)
```
### The modules:

```
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

	def repeat(selectedShow):
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
```
