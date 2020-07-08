import constants
import copy
import random

players_list = []
teams_list = []
team_panther = []
team_bandits = []
team_warriors = []

def clean_data():
	# index = 1
	for player in players_list:
		if player['experience'].lower() == 'yes':
			player['experience'] = True
		elif player['experience'].
			player['experience'] = False

		height = player['height'].split(' ')
		player['height'] = int(height[0])

		guardian = player['guardians']
		if ' and ' in guardian:
			guardian = guardian.split(' and ')
		else:
		
		# print(f'{index}. '"{} is {}m tall!".format(player['name'], player['height']))
		# index+=1


def balance_team(team):
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


# MAIN PROGRAM
if __name__ == '__main__':
	players_list = copy.deepcopy(constants.PLAYERS)
	teams_list = copy.deepcopy(constants.TEAMS)

	clean_data()

	balance_team(team_panther)
	balance_team(team_bandits)
	balance_team(team_warriors)


	print("END")

