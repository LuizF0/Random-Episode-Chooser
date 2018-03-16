import lib.randomizer as r

def repeat(selectedShow):
	repeat = 0
	while repeat == 0:
		another_ep = input('\nDo you want another episode?(Yes/No) _ ').lower()
		if another_ep == 'yes':
			r.randomizer(selectedShow)
		elif another_ep == 'no':
			print('\nOK.')
			break
		else:
			print('\nNot quite right, mate.')