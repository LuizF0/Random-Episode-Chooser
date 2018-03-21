import lib.modules as m

try:
	print('''
			______________________________________
			Welcome to the Random Episode Chooser!
				''')
	m.menu()

	while True:
		option = int(input('\nChoose your number: _ '))-1

		if option == 0:
			Shows = list(m.collection().keys())

			print('\n')
			for number, values in enumerate(Shows, 1):
				print(number, values)

			while True:
				nselected = int(input('\nChoose your show\'s number(or anything else to quit): _ '))-1
				if nselected > len(Shows):
					print('Wrong number, please choose again.')
					nselected = []

				else:
					m.randomizer(Shows[nselected])
					m.repeater(Shows[nselected])
			break

		elif option == 1:
			while True:
				addShow = input('\nDo you want to add a new show?(Yes/No) _ ').lower()

				if addShow == 'yes':
					newShow = str(input('\nShow\'s name: _ '))
					newShow_s = int(input('Number of Seasons: _ '))
					newShow_e = int(input('Number of episodes per season: _ '))
					print('\n')

					dict2 = {newShow:[newShow_s, newShow_e]}
					
					with open('lib/modules.py','a') as f:
						f.write('\ndict1.update( %s )' % str(dict2))
						f.close()
					break

				elif addShow == 'no':
					print('\nOK.')
					break

				else:
					print('\nWrong option.')
			break

		elif option == 2:
			break

		else:
			print('\nNot an option')

except Exception as e:
	print('\nExiting.', e)
