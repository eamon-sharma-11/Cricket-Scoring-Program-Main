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
innings = 1
batsmen_1 = ""
batsmen_2 = ""
out_full = False
team_select = False


####FUNCTIONS####

###SETTING SIDES DEPENDING ON WHAT THE USER HAS CHOOSEN
def side_set(Batting, Fielding):
    # Fielding Team set
    global batting_team
    global fielding_team
    global batting_team_copy

    fielding_team = [None] * len(Fielding)
    for i in range(0, len(Fielding)):
        fielding_team[i] = Fielding[i]

    ###COPY OF BATTING TEAM
    batting_team_copy = [None] * len(Batting)
    for i in range(0, len(Batting)):
        batting_team_copy[i] = Batting[i]

    for i in range(0, len(fielding_team)):
        print(f"Fielding Team: {fielding_team[i]}")

    # Batting Team set
    batting_team = [None] * len(Batting)
    for i in range(0, len(Batting)):
        batting_team[i] = Batting[i]

    for i in range(0, len(batting_team)):
        print(f"Batting Team: {batting_team[i]}")


###SETTING PLAYER NAMES IN RESPECTIVE TEAMS
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


###CAHNGING BOWLER IN FIELDING TEAM
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


###CODE FOR REMOVING PLAYER
def remove_player(player, team_array):
    for players in team_array:
        if players == player:
            team_array.remove(player)


###SELECTING BATSMEN
def choosing_batsmen(batsmen, location):
    pos = int(input(f"For our first batsmen, enter the postion they are in in the list:{batting_team}: ")) - 1
    batsmen = batting_team[pos]
    facing_players[location] = batsmen
    print(f"You have selected {batsmen} as a batsmen")
    for players in batting_team:
        if players == batsmen:
            batting_team.remove(batsmen)


# Start Program
def start():
    global match_type
    global over_type


match_type_setup = False
print("""Welcome to the cricket scoring program
The program can switch between T20 or One day. Please choose""")
match_type = input("T20/1D: ")
match_type = match_type.lower()
while match_type_setup == False:
    if match_type == "t20":
        over_type = 20
        break
    if match_type == "1d":
        over_type = 50
        break
    else:
        match_type = input("Invalid match type. Please try again. T20/1D: ")


# MOVING AROUND RESULTS
def moving_results():
    global out_array_1
    global out_array_2
    global out_array
    global overall_runs_1
    global overall_runs_2
    global team_out_1
    global team_out_2
    ###MOVING OUT PLAYERS INTO DIFFEERENT LIST IF TEAM 1 IS BATTING
    if current_facing_team == "team1":
        out_array_1 = [None] * len(out_array)
        for i in range(0, len(out_array)):
            out_array_1[i] = out_array[i]
        out_array = [None] * 10
        team_out_1 = team_out
        overall_runs_1 = total_runs
        ###MOVING OUT PLAYERS INTO DIFFEERENT LIST IF TEAM 1 IS BATTING
    if start_teams == "team2":
        out_array_2 = [None] * len(out_array)
        for i in range(0, len(out_array)):
            out_array_2[i] = out_array[i]
        out_array = [None] * 10
        team_out_2 = team_out
        overall_runs_2 = total_runs
        total_runs = 0


###START

start()
print(f"Each team will play {over_type} overs")

###ASK USER TO INPUT TEAMS
print("Input player names")
player_input(Team1, 1, False)
player_input(Team2, 1, False)

print(f'Team 1 consists of {Team1}')
print(f'Team 2 consists of {Team2}')

###SELECTING TEAM SIDES
start_teams = input("What team is batting first? Team1/Team2: ")

while team_select == False:
    if start_teams.lower() == "team1" or start_teams.lower() == "1":
        side_set(Team1, Team2)
        current_facing_team = "team1"

    if start_teams.lower() == "team2" or start_teams.lower() == "2":
        side_set(Team2, Team1)
        current_facing_team = "team2"
    else:
        start_teams = input("Invalid team, try agian. Team1/Team2: ")
        start_teams = start_teams.lower()

print("Flag")

#####CHOOSING BATSMEN####
choosing_batsmen(batsmen_1, 0)
choosing_batsmen(batsmen_2, 1)

###CHOOSING BOWLER###
current_bolwer_pos = int(
    input(f'For our first bowler, please enter the postion that they are in the list:{fielding_team}: ')) - 1
bowler = fielding_team[current_bolwer_pos]
print(f"You have selected {bowler} as the first bowler")
remove_player(bowler, fielding_team)

print(f'Our starting batting lineup include {batsmen_1} and {batsmen_2}')
print(f'They will be facing off against {bowler}')

team_length = len(batting_team)

####START OF MAIN GAME####
while innings != 3:
    facing_input = int(input(f"Enter position of the batsmen that is facing: {facing_players}: ")) - 1
    current_facing_player_pos_in_list = facing_input + 1
    facing = facing_players[facing_input]
    ###DUMB VARIABLE NAME CHANGE LATER
    while over != over_type or out_full == True or facing_length <= 1:
        print(f"This is innings {innings}")
        print("Please enter the following fields after the bowl is complete")
        play_out = input(f"Did {facing} get out? Y/N: ")
        play_out = play_out.lower()
        if play_out == "y":
            team_out = team_out + 1
            array_out = int(team_out)
            out_array[array_out - 1] = facing
            if not batting_team:
                out_full = True
                break
            new_batsmen_pos = int(input(f"Select the position of the new batsmen {batting_team}: ")) - 1
            facing_players[facing_input] = batting_team[new_batsmen_pos]
            for players in batting_team:
                for facing in facing_players:
                    if players == facing:
                        batting_team.remove(players)
                        facing_players.remove(players)
            print(f"The players who are out now include: {out}")
            print(f"The remaining players are {batting_team}")
            facing_length = len(facing_players)

        ###IF PLAYER IS NOT OUT
        if play_out == "n":
            current_play_runs = int(input("Please enter the amount of runs scored in that play: "))
            total_runs = current_play_runs + total_runs
            print(f"The current run total is {total_runs}")
            ball = ball + 1
            over = ball / 6
            ###wHICH PLAYER IS FACING NEXT BASED OF RUNS
            if current_play_runs % 2 == 0:
                print("Batsmen is same")
            if current_play_runs % 2 != 0:
                if current_facing_player_pos_in_list == 1:
                    facing = facing_players[1]
                    current_facing_player_pos_in_list = 2
                elif current_facing_player_pos_in_list == 2:
                    facing = facing_players[0]
                    current_facing_player_pos_in_list = 1
        ###CHANGES BOWLER IF OVER IS FINISHED
        if over == 1:
            bowler_change(bowler)
            print(f"Your new bowler is {bowler}")

    innings = innings + 1
    # print(f"The first innings has been completed. The score was {team_out}/{total_runs}")
    # print(f"The batsmen who got out were {out_array}")
    if innings == 2:
        ###RESETING VARIABLES FOR NEXT INNINGS
        print("FLAG FOR END OF INNINGS")

        moving_results()

        ###MOVES PLAYERS BETWEEN SIDES
        ###MOVING CURRENT BOWLER BACK INTO LIST
        fielding_team.append(bowler)

        print(f"Current fielding team : {fielding_team}")
        print(f"Current batting team : {batting_team}")

        ###MOVING CURRENT BATTING TEAM INTO TEMP LIST BEFORE MOVING TO MAIN LIST OF FIELDING TEAM
        new_fielding_team = [None] * len(batting_team_copy)
        for i in range(0, len(batting_team_copy)):
            new_fielding_team[i] = batting_team_copy[i]

        ###MOVING CURRENT FIELDING TEAM INTO TEMP LIST BEFORE MOVING TO MAIN LIST OF BATTING TEAM
        new_batting_team = [None] * len(fielding_team)
        for i in range(0, len(fielding_team)):
            new_batting_team[i] = fielding_team[i]

        ###MOVING NEW FIELDING TEAM FROM LIST "NEW FIELDING TEAM"
        fielding_team = [None] * len(new_fielding_team)
        for i in range(0, len(new_fielding_team)):
            fielding_team[i] = new_fielding_team[i]

        ###MOVING NEW BATTING TEAM FROM LIST "NEW BATTING TEAM"
        batting_team = [None] * len(new_batting_team)
        for i in range(0, len(new_batting_team)):
            batting_team[i] = new_batting_team[i]

        print(f"Current fielding team : {fielding_team}")
        print(f"Current batting team : {batting_team}")

        choosing_batsmen(batsmen_1, 0)
        choosing_batsmen(batsmen_2, 1)

        current_bolwer_pos = int(
            input(f'For our first bowler, please enter the postion that they are in the list:{fielding_team}: ')) - 1
        bowler = fielding_team[current_bolwer_pos]
        print(f"You have selected {bowler} as the first bowler")
        remove_player(bowler, fielding_team)

        print(f'Our starting batting lineup for innigs 2include {batsmen_1} and {batsmen_2}')
        print(f'They will be facing off against {bowler}')

    if innings == 3:
        moving_results()
        print("Results:")
        print(f"Team 1 final score: {team_out_1}/{overall_runs_1}")
        print(f"Team 2 final score: {team_out_2}/{overall_runs_2}")
























    






    

