####### main sports betting code 

######### 1. Ask user for macro data 
# Collect: Number of Games, Name of Each Team (home, away), Number of Legs in Each Game, Insured or Not,  Risk, Reward
# Store data in this syntax: [# of games (int), [[Home Team 1, Away Team 1],[ Home Team 2, Away Team 2]] , [list of # of legs in each game] , (1 = Insured, 0 = Not Insured) , [ Risk (int) , Reward (int)] ], league code
total_bet = []
def macro_information(): 
    global total_bet
    macro_info_list = []

    # Get the number of games total 
    num_of_games = int(input("How many games involved?: "))
    macro_info_list.append(num_of_games)
    
    # Get the names of each team in all games 
    team_list = []
    count = 1 
    for i in range(1,num_of_games+1):
        home_team = input("Who is the Home team for Game # " + str(count) + "?: ")
        away_team = input("Who is the Away team for Game # " + str(count) + "?: ")
        team_list.append([home_team,away_team])
        count += 1
    macro_info_list.append(team_list)    

    # Get the number of legs in each team 
    list_of_legs = []
    total_legs = 0
    for i in range(0,macro_info_list[0]):
        count = 1
        print(macro_info_list)
        leg_amt = input("How many legs in "+ str(macro_info_list[1][i][0]) + " vs. " + str(macro_info_list[1][i][1]) + "?: ")
        total_legs += int(leg_amt)
        list_of_legs.append(int(leg_amt))
        count+=1
    list_of_legs.append(total_legs)
    macro_info_list.append(list_of_legs)

    # Check if the bet was insured 
    yes_answers = ["yes","Yes","y","Y"]
    no_answers = ["no","No","n","N"] 
    insured_input = input("Is the bet insured? Yes or No: ")
    bet_found = False 
    while bet_found == False: 
        for answers in yes_answers:
            if answers == insured_input: 
                macro_info_list.append(1)
                bet_found = True 
        for answers in no_answers:
            if answers == insured_input: 
                macro_info_list.append(0)
                bet_found = True 
        if bet_found == False: 
            print("Incorrect Output ")
            insured_input = input("Is the bet insured? Yes or No: ")

    # Get Risk and Reward 
    risk_input = (input("What was the risk?: "))
    reward_input = int(input("What was the reward?: "))
    macro_info_list.append([risk_input,reward_input])

    # What League is this 
    # Prem = 1 , Champions League = 2, MLS, = 3, La Liga = 4, German League = 5, International, 
    print("Premier League = 1, Champions League = 2, MLS = 3, LaLiga = 4, Bundesliga = 5, International = 6 ")
    league_input = int(input("What league is this game apart of?: "))
    macro_info_list.append(league_input)

    # Add the  macro list to the total bet list and printing the total bet 
    total_bet.append(macro_info_list)
    print(total_bet)

####### 2. Ask user for specific data 
# Collect: Player Name, Position, Team, Over-Under, # of Things (int), Things Measurment, Pre-Game or Live Bet
# Store data in this syntax: ['Player Name', 'Position Abreviations', Home = 1 Away = 0, Over = 1 Under = 0, [ # of Things (int),Things measured code] , Pre-Game = 1 or Live Bet = 0], RESULT Over = 1 Under = 0 ]

def specific_information():
    global total_bet
    specific_info = [] 

    leg_count = 1 
    for i in range(0,total_bet[0][0]):
        game_leg_count = 1
        for x in range(total_bet[0][2][i]):
            h_team,a_team = total_bet[0][1][i]
            # Get the Players name 
            player_name_input = input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| What is the players name?: ")
            specific_info.append(player_name_input)

            # Get Positon in Code 
            print("GK = 1, RB = 2, LB = 3, RCB = 4, LCB = 5, CDM = 6, RW = 7, HMD = 8, CF = 9, AMD = 10, LW = 11")
            player_position = int(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| What is the position of the player?: "))
            specific_info.append(player_position)

            # Get the Team 
            player_team = int(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| Home = 1 or Away = 0?: "))
            specific_info.append(player_team)

            # Get Over-Under
            over_under_bet = int(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| Over = 1 or Under = 0?: "))
            specific_info.append(over_under_bet)

            # Get Bet Perameters
                # Get the # of Things 
            things_measurement = (input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| What is the leg measuring?: "))
                # Get the Things Measured
            num_of_things = float(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| How many " + things_measurement + " are needed?: "))
                # Add both to the specific_info
            specific_info.append([num_of_things,things_measurement])

            # Get Pre-Game/Live Bet
            pre_or_live = int(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| Pre-Game = 1 or Live Bet = 0?: "))
            specific_info.append(pre_or_live)

            # Get RESULT 
            over_under_result = int(input("Leg " + str(leg_count) + "/" + str(total_bet[0][2][-1])+ " | " + h_team + " vs. " + a_team  + " "+ str(game_leg_count) +"/"+ str(total_bet[0][2][i]) + "| Over = 1 or Under = 0?: "))
            specific_info.append(over_under_result)

            # Add the counter to loop and add this leg to the bet_total
            game_leg_count += 1
            leg_count += 1 
            
            total_bet.append(specific_info)

############# MAIN FUNCTION 
def main():
    macro_information() 
    specific_information()

main()

# 2. Transribe data to Readable csv
# 3. Inputing data into csv file 
# 4. Inputing data into json file 

############## Printing Current Score Card : 
###### Show the betting template based on macro_info 
#### TEMPLATE 
##  Leg #1 
##  Team 1 vs Team 2 (1/2) | Bet 1/3
##  Player Name (Position Abriviation)
##  Team
##  Over 3.5 Shots 
##  Result (Hit or Missed)
##  
##  Leg #2
#   ...
