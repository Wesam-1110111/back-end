'''
********  Docs ********
- hide the secrets files
- need user and password to show them
- ...

*********************** 
'''

import sys, os


# ------- user data ----------
USER = 'mrw'
PASSWORD = 'WesamIsMad'
# ----------------------------

def run():
	# clear screen
	print(m)
	print(menu)
	in_put = input('>> ')

def login():
	# sys(clear) to clear the screen
	print(m)
	
	user = input('User name: ')
	while(True):
		if user == USER:
			passwd = input('Password: ')
			while(True):
				if passwd == PASSWORD:
					print('True')
					run()
					break
				else:
					print('The password not correct, try again')
					passwd = input('Password: ')
			break
		
		else:
			print('The user name is not correct, try again')
			user = input('User name: ')

m = '''
*****************************************
*        Log into Wesam's brain         *
*****************************************

'''

menu = '''
1. Show files.
2. New file.
3. Open file.
4. Delete file.
0. Exit.
'''


print(m)


ans = input('Are you Wesam [y/n]:').lower()

while(True):
	if ans == 'y':
		print('\nThen Fuckoff\n')
		break
	elif ans == 'n':
		print('Go on')
		login()
		break
	else:
		print('Enter only: [y] for Yes, or [n] for No!')
		ans = input('\nAre you Wesam [y/n]:').lower()


