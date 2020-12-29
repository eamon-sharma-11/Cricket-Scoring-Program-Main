

Team1 = []
Team2 = []
fin_T1 = False
fin_T2 = False
first_bowl = False
out = False
batsmen = []
Team1_facing = False
Team2_facing = False
new_bowler = False
balls = 0
start_teams = " "
ball = 0
amount_out = 0
out_flag = False
batsmen_out = []
team_out = 0
same = True
over = 0
play_complete = False
facing_players = [None] * 2
out_array = [None] * 10
total_runs = 0
innings = 0
batsmen_1 = ""
batsmen_2 = ""

####FUNCTIONS####

def side_set(Batting, Fielding):
    # Fielding Team set
    global batting_team
    global fielding_team

    fielding_team = [None] * len(Fielding)
    for i in range(0, len(Fielding)):
        fielding_team[i] = Fielding[i]

    for i in range(0, len(fielding_team)):
        print(f"Fielding Team: {fielding_team[i]}")

    # Batting Team set
    batting_team = [None] * len(Batting)
    for i in range(0, len(Batting)):
        batting_team[i] = Batting[i]

    for i in range(0, len(batting_team)):
        print(f"Batting Team: {batting_team[i]}")


def player_input(current_team, num_team, allowed_amount):
    print("Team player input")
    while allowed_amount == False:
        elem = int(input("Amount of players(Between 2 and 11): "))
        if elem > 11 or elem < 2:
            print("Incorrect amount, try again")
        else:
            allowed_amount = True
    for i in range(0, elem):
        p = None
        while not p or p in current_team:
            p = input(f'Enter player number {num_team} name (In batting order) eg J.Smith: ')
            if p in current_team: print('That player has already been entered, please retry...: ')
        current_team.append(p)
        num_team = num_team + 1
    print(current_team)


def bowler_change(bowler):
    if over == 1:
        new_bowler_pos = int(
            input(f"You must now select a new bowler from {fielding_team}. Enter the postition of your new bowler: "))
        new_bowler_pos = new_bowler_pos - 1
        bowler_moving_in = fielding_team[new_bowler_pos]
        bowler_moving_out = bowler
        bowler = bowler_moving_in
        fielding_team[new_bowler_pos] = bowler_moving_out

    print(f'Our new bowler is {bowler}')
    print(f"{fielding_team}")


def remove_player(player, team_array):
    for players in team_array:
        if players == player:
            team_array.remove(player)


def choosing_batsmen(batsmen, location):
    pos = int(input(f"For our first batsmen, enter the postion they are in in the list:{batting_team}: ")) - 1
    batsmen = batting_team[pos]
    facing_players[location] = batsmen
    print(f"You have selected {batsmen} as a batsmen")
    for players in batting_team:
        if players == batsmen:
            batting_team.remove(batsmen)


####START MAIN####
start = input("Inizalize scoring program? Y/N: ")
start = start.lower()

#ASK USER WHAT TYPE OF MATCH THEY WANT TO SCORE
if start == 'y':
    print("""Welcome to the cricket scoring program
The program can switch between T20 or One day. Please choose""")
    match_type = input("T20/1D")
    match_type = match_type.lower()
    if match_type == "t20":
        over_type = 20
    if match_type == "1d":
        over_type = 50

    teams = input("Start filling in teams? Y/N?: ")
    teams = teams.lower()
    if teams == 'y':
        player_input(Team1, 1, False)
        player_input(Team2, 1, False)

print(f'Team 1 consists of {Team1}')
print(f'Team 2 consists of {Team2}')

start = input("Start game? Y/N: ")
start = start.lower()

# Game Start
if start == 'y':
    start_teams = input("What team is batting first? Team1/Team2: ")
    start_teams = start_teams.lower()

    if start_teams == "team1" or start_teams == "1":
        # Batting = Team1
        # Bowling = Team2
        side_set(Team1, Team2)

    if start_teams == "team2" or start_teams == "2":
        # Batting = Team2
        # Bowling = Team1
        side_set(Team2, Team1)

print("Flag")

#####CHOOSING BATSMEN####
choosing_batsmen(batsmen_1, 0)
choosing_batsmen(batsmen_2, 1)

current_bolwer_pos = int(
    input(f'For our first bowler, please enter the postion that they are in the list:{fielding_team}:')) - 1
bowler = fielding_team[current_bolwer_pos]
print(f"You have selected {bowler} as the first bowler")
remove_player(bowler, fielding_team)

print(f'Our starting batting lineup include {batsmen_1} and {batsmen_2}')
print(f'They will be facing off against {bowler}')

team_length = len(batting_team)

####START OF MAIN GAME####
while innings != 3:
    while over != over_type or team_out == team_length:
        print("Flag: Main Game start")

        facing_input = int(input(f"Enter position of the batsmen that is facing: {facing_players}: ")) - 1
        facing = facing_players[facing_input]
        print("Please enter the following fields after the bowl is complete")
        play_out = input(f"Did {facing} get out? Y/N: ")
        play_out = play_out.lower()
        if play_out == "y":
            team_out = team_out + 1
            array_out = int(team_out)
            out_array[array_out - 1] = facing
            new_batsmen_pos = int(input(f"Select the position of the new batsmen {batting_team}")) - 1
            facing_players[facing_input] = batting_team[new_batsmen_pos]
            for players in batting_team:
                for facing in facing_players:
                    if players == facing:
                        batting_team.remove(players)
            print(f"The players who are out now include: {out}")
            print(f"The remaining players are {batting_team}")

        if play_out == "n":
            current_play_runs = int(input("Please enter the amount of runs scored in that play: "))
            total_runs = current_play_runs + total_runs
            print(f"The current run total is {total_runs}")
            ball = ball + 1
            over = ball / 6
    bowler_change(bowler)

# FOR WHEN NEW BOWLER CAN BE CHOSEN


innings = innings + 1
#####Test push from VSC