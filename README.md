# Project 1:

This is my first Python project.

I intend to update it as i learn new cool stuff.
Here is the code:
import lib.collection as c
import lib.menu as m
import lib.randomizer as r
import lib.repeater as x

try:
	print('''
			______________________________________
			Welcome to the Random Episode Chooser!
				''')
	m.menu()

	option = int(input('\nChoose your number: _ '))-1

	if option == 0:
		Shows = list(c.Collection().keys())

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
					
				r.randomizer(selectedShow)
				x.repeat(selectedShow)
		
	elif option == 1:
		addShow = input('\nDo you want to add a new show?(Yes/No) _ ').lower()

		if addShow == 'yes':
			newShow = str(input('\nShow\'s name: _ '))
			newShow_s = int(input('Number of Seasons: _ '))
			newShow_e = int(input('Number of episodes per season: _ '))
			print('\n')

			dict2 = {newShow:[newShow_s, newShow_e]}
			
			with open('lib/collection.py','a') as f:
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
	print(e)
