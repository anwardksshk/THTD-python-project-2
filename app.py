import constants
import copy
import random

players_list = []
teams_list = []
team_panther = []
team_bandits = []
team_warriors = []

def average_height(total_heights, total_players):
	return total_heights / total_players

def clean_data():
	"""
	1) Reads the existing player data from the PLAYERS constants provided in constants.py 
	2) Cleans the player data without changing the original data 
	3) Saves it to a new collection

	Data to be cleaned:
	Height: This should be saved as an integer
	Experience: This should be saved as a boolean value (True or False)
	"""
	for player in players_list:
		if player['experience'].lower() == 'yes':
			player['experience'] = True
		elif player['experience'].lower() == 'no':
			player['experience'] = False

		height = player['height'].split(' ')
		player['height'] = int(height[0])

		guardian = player['guardians']
		if ' and ' in guardian:
			player['guardians'] = guardian.split(' and ')


def balance_team(team):
	"""
	Balance the players across the three teams: Panthers, Bandits and Warriors. 
	The teams will have the same number of total players on them.
	Eeach team will have the same number of experienced and inexperienced players.
	"""
	exp_count = 0
	no_exp_count = 0
	while len(team) != 6:
		i = random.choice(range(len(players_list)))
		if players_list[i]['experience'] == True and exp_count <= 2: 
			exp_count+=1
			team.append(players_list.pop(i))
		elif players_list[i]['experience'] == False and no_exp_count <= 2: 
			no_exp_count+=1
			team.append(players_list.pop(i))


def welcome():
	"""Only prints welcome message"""
	print("="*20 
		+ "WELCOME" 
		+ "="*20
		+ "\n"
		)


def show_stats(selected_team, team_name):
	"""Show team statistics of the selected team from menu"""
	members_names = []
	guardians_names = []
	no_inexperienced = 0
	no_experienced = 0
	total_heights = 0

	for player in selected_team:
		members_names.append(player['name'])
		guardians_names.append(player['guardians'])
		total_heights+=player['height']
		if player['experience'] == True:
			no_experienced+=1
		elif player['experience'] == False:
			no_inexperienced+=1		

	print("\n"
		+ "*"*6 
		+ "Team {}".format(team_name)
		+ "*"*6
		+ "\n"
		)
	print("Team: {}".format(team_name)
		+ "\n"
		+ "Total players: {} players".format(len(selected_team))
		+ "\n"
		+ "Players: {}".format(", ".join(members_names))
		+ "\n"
		+ "Total no. of inexperienced players: {}".format(no_inexperienced)
		+ "\n"
		+ "Total no. of experienced players: {}".format(no_experienced)
		+ "\n"
		+ "Average height of the team: {:.2f}".format(average_height(total_heights, no_experienced + no_inexperienced))
		+ "\n"
		+ "All guardians of all players: {}".format(", ".join(members_names))
		+ "\n\n"
		+ "*"*(12 + len("Team " + team_name))
		+ "\n"
		)


def menu():
	"""Display menu and prompt for options from user"""
	while True:
		try:
			option = int(input("Choose the option from the menu:\n"
				+ "1. Show Team Panther stats\n"
				+ "2. Show Team Bandits stats\n"
				+ "3. Show Team Warriors stats\n"
				+ "4. Quit program\n"
				+ "\n=> "))
		except ValueError:
			print("Value Error: Please only choose the number from the menu.")
		else:
			if option == 1:
				show_stats(team_panther, "Panther")
			elif option == 2:
				show_stats(team_bandits, "Bandits")
			elif option == 3:
				show_stats(team_warriors, "Warriors")
			elif option ==4:
				break


def end_program():
	"""Only prints closing message"""
	print("="*18 
		+ "THANK YOU" 
		+ "="*20
		+ "\n"
		)


# MAIN PROGRAM
if __name__ == '__main__':
	players_list = copy.deepcopy(constants.PLAYERS)
	teams_list = copy.deepcopy(constants.TEAMS)
	
	clean_data()

	balance_team(team_panther)
	balance_team(team_bandits)
	balance_team(team_warriors)
	
	welcome()
	menu()
	end_program()

