import math 
################################################################
##### RETURN THE EV, CUM PROB, BE PROB

####### Types of Bets: 
# 1. 2 Leg 
# 2. 3 Leg
# 3. 3 Leg Insured 
# 4. 4 Leg 
# 5. 4 Leg Insured 
# 6. 5 Leg
# 7. 5 Leg Insured

##### Create a chart with a row for each of the bet types 
# Rows: Each type of bet that we can make 
# Columns: Name, EV, Gain %, CUM PROB 

################################################################
##### GLOBAL VARIABLES

leg1_prob, leg1_sd = 0,0
leg2_prob, leg2_sd = 0,0
leg3_prob, leg3_sd = 0,0
leg4_prob, leg4_sd = 0,0
leg5_prob, leg5_sd = 0,0
test_list = [ [ .93 , .1 ], [ .89  , .1], [ .85 , .2 ], [ .79 , .03 ], [ .77 , .08 ] ]

stats_2leg = 0 
stats_3leg = 0
stats_3legi = 0 
stats_4leg = 0 
stats_4legi = 0 
stats_5leg = 0 
stats_5legi = 0 

max_min_list = [] 
leg1_prob_min , leg1_prob_max = 0,0
leg2_prob_min , leg2_prob_max = 0,0
leg3_prob_min , leg3_prob_max = 0,0 
leg4_prob_min , leg4_prob_max = 0,0
leg5_prob_min , leg5_prob_max = 0,0

final_bets = [] 

################################################################
##### TRANSCRIBE ALL DATA ( OPTIONAL STEP, MIGHT REMOVE LATER FOR SIMPLICITY )

def transcribe_data(list_input): 
    global leg1_prob, leg1_sd, leg2_prob, leg2_sd, leg3_prob, leg3_sd, leg4_prob, leg4_sd, leg5_prob, leg5_sd
    leg1_prob, leg1_sd = list_input[0]
    leg2_prob, leg2_sd = list_input[1]
    leg3_prob, leg3_sd = list_input[2]
    leg4_prob, leg4_sd = list_input[3]
    leg5_prob, leg5_sd = list_input[4]

def transcribe_min_max_prob(list_input): 
    global max_min_list, leg1_prob_min, leg1_prob_max, leg2_prob_min, leg2_prob_max, leg3_prob_min, leg3_prob_max, leg4_prob_min, leg4_prob_max, leg5_prob_min, leg5_prob_max
    for i in list_input: 
        i_min = i[0] - i[1]*2
        i_max = i[0] + i[1]*2
        max_min_list.append([i_min, i_max])
    leg1_prob_min , leg1_prob_max = max_min_list[0]
    leg2_prob_min , leg2_prob_max = max_min_list[1]
    leg3_prob_min , leg3_prob_max = max_min_list[2]
    leg4_prob_min , leg4_prob_max = max_min_list[3]
    leg5_prob_min , leg5_prob_max = max_min_list[4]

################################################################
##### CALCULATE ALL BET INFORMATION 
    
## 2 Leg Bet 
# Input: leg1_prob , leg2_prob, leg1_sd, leg2_sd 
# Output: EV, 95% EV, CUM PROB 
def get_2leg(): 
    global stats_2leg 
    ## Get CUM PROB  
    cumprob_2leg = leg1_prob * leg2_prob
    ## Get the EV 
    ev_2leg = (cumprob_2leg * 3) - 1 
    ## Get 95% EV 
    ev95_2leg_min = ((leg1_prob_min) * (leg2_prob_min) * (3)) -1 
    ev95_2leg_max = ((leg1_prob_max) * (leg2_prob_max) * (3)) -1 
    ev95_2leg = [ ev95_2leg_min, ev95_2leg_max]
    ## Find the W/L Probabilites 
    if ev95_2leg_max >= 1 and ev95_2leg_min >= 1:  
        wprob_2leg = 1
        lprob_2leg = 0
        wlratio_2leg = 1
    elif ev95_2leg_max <= 1 and ev95_2leg_min <= 1:
        wprob_2leg = 0
        lprob_2leg = 1
        wlratio_2leg = 0
    else: 
        wprob_2leg = ev95_2leg_max - 1 
        lprob_2leg = 1 - ev95_2leg_min
        wlratio_2leg = wprob_2leg / lprob_2leg
    wperc_2leg = (wprob_2leg / ( wprob_2leg + lprob_2leg))*100
    ## Put data in stats_2leg 
    stats_2leg = [ev_2leg, ev95_2leg, cumprob_2leg, wlratio_2leg , wperc_2leg]

## 3 Leg Bet 
# Input: leg1_prob, leg2_prob, leg3_prob, leg1_sd, leg2_sd, leg3_sd 
# Output: EV, 95% EV, CUM PROB 
def get_3leg(): 
    global stats_3leg 
    ## Get CUM PROB  
    cumprob_3leg = (leg1_prob * leg2_prob * leg3_prob)
    ## Get the EV 
    ev_3leg = (cumprob_3leg * 6) - 1
    ## Get 95% EV 
    ev95_3leg_min = ((leg1_prob_min) * (leg2_prob_min) * (leg3_prob_min)) - 1 
    ev95_3leg_max = ((leg1_prob_max) * (leg2_prob_max) * (leg3_prob_max)) - 1 
    ev95_3leg = [ev95_3leg_min, ev95_3leg_max]
     ## Find the W/L Probabilites 
    if ev95_3leg_max >= 1 and ev95_3leg_min >= 1:  
        wprob_3leg = 1
        lprob_3leg = 0
        wlratio_3leg = 1
    elif ev95_3leg_max <= 1 and ev95_3leg_min <= 1:
        wprob_3leg = 0
        lprob_3leg = 1
        wlratio_3leg = 0
    else: 
        wprob_3leg = ev95_3leg_max - 1 
        lprob_3leg = 1 - ev95_3leg_min
        wlratio_3leg = wprob_3leg / lprob_3leg
    wperc_3leg = (wprob_3leg / ( wprob_3leg + lprob_3leg))*100
    ## Put data in stats_3leg 
    stats_3leg = [ev_3leg, ev95_3leg, cumprob_3leg, wlratio_3leg , wperc_3leg]
    
## 3 Leg Bet Insured 
# Input: leg1_prob, leg2_prob, leg3_prob, leg1_sd, leg2_sd, leg3_sd 
# Output: EV, 95% EV, CUM PROB 
def get_3legi(): 
    global stats_3legi 
    ## Get the CUM PROB 
    cumprob_3legi = (leg1_prob * leg2_prob * leg3_prob)
    ## Get the EV 
    ev_3legi = (cumprob_3legi * 3) + ((1 - leg1_prob) * leg2_prob * leg3_prob * 1) + (leg1_prob * (1 - leg2_prob) * leg3_prob * 1) + (leg1_prob * leg2_prob * (1- leg3_prob) * 1) - 1 
    ## Get the 95% EV 
    ev95_3legi_min = (leg1_prob_min * leg2_prob_min * leg3_prob_min * 3) + ((1 - leg1_prob_min) * leg2_prob_min * leg3_prob_min * 1) + (leg1_prob_min * (1 - leg2_prob_min) * leg3_prob_min * 1) + (leg1_prob_min * leg2_prob_min * (1- leg3_prob_min) * 1) - 1 
    ev95_3legi_max = (leg1_prob_max * leg2_prob_max * leg3_prob_max * 3) + ((1 - leg1_prob_max) * leg2_prob_max * leg3_prob_max * 1) + (leg1_prob_max * (1 - leg2_prob_max) * leg3_prob_max * 1) + (leg1_prob_max * leg2_prob_max * (1- leg3_prob_max) * 1) - 1 
    ev95_3legi = [ev95_3legi_min, ev95_3legi_max]
    ## Put data in stats_3legi 
    stats_3legi = [ev_3legi, ev95_3legi, cumprob_3legi, 0, 0]

## 4 Leg Bet 
# Input: leg1_prob, leg2_prob, leg3_prob, leg4_prob, leg1_sd, leg2_sd, leg3_sd, leg4_sd 
# Output: EV, 95% EV, CUM PROB 
def get_4leg(): 
    global stats_4leg
    ## Get CUM PROB  
    cumprob_4leg = (leg1_prob * leg2_prob * leg3_prob * leg4_prob) 
    ## Get the EV 
    ev_4leg = (cumprob_4leg * 10) - 1
    ## Get 95% EV 
    ev95_4leg_min = ((leg1_prob_min) * (leg2_prob_min) * (leg3_prob_min) * (leg4_prob_min) * 10) - 1 
    ev95_4leg_max = ((leg1_prob_max) * (leg2_prob_max) * (leg3_prob_max) * (leg4_prob_max) * 10) - 1 
    ev95_4leg = [ev95_4leg_min, ev95_4leg_max]
    ## Put data in stats_4leg  
    stats_4leg = [ev_4leg, ev95_4leg, cumprob_4leg, 0, 0]

## 4 Leg Bet Insured 
# Input: leg1_prob, leg2_prob, leg3_prob, leg4_prob, leg1_sd, leg2_sd, leg3_sd, leg4_sd 
# Output: EV, 95% EV, CUM PROB 
def get_4legi(): 
    global stats_4legi , test_list
    ## Get the CUM PROB 
    cumprob_4legi = (leg1_prob * leg2_prob * leg3_prob * leg4_prob)
    ## Get the EV 
    ev_4legi =(cumprob_4legi * 6) + ((1 - leg1_prob) * leg2_prob * leg3_prob * leg4_prob * 1.5) + (leg1_prob * (1 - leg2_prob) * leg3_prob * leg4_prob * 1.5) + (leg1_prob * leg2_prob * (1-leg3_prob) * leg4_prob * 1.5) + (leg1_prob * leg2_prob * leg3_prob * (1-leg4_prob) * 1.5) - 1
    ## Get the 95% EV 
    ev95_4legi_min = (leg1_prob_min * leg2_prob_min * leg3_prob_min * leg4_prob_min * 6) + ((1 - leg1_prob_min) * leg2_prob_min * leg3_prob_min * leg4_prob_min * 1.5) + (leg1_prob_min * (1 - leg2_prob_min) * leg3_prob_min * leg4_prob_min * 1.5) + (leg1_prob_min * leg2_prob_min * (1-leg3_prob_min) * leg4_prob_min * 1.5) + (leg1_prob_min * leg2_prob_min * leg3_prob_min * (1-leg4_prob_min) * 1.5) - 1
    ev95_4legi_max = (leg1_prob_max * leg2_prob_max * leg3_prob_max * leg4_prob_max * 6) + ((1 - leg1_prob_max) * leg2_prob_max * leg3_prob_max * leg4_prob_max * 1.5) + (leg1_prob_max * (1 - leg2_prob_max) * leg3_prob_max * leg4_prob_max * 1.5) + (leg1_prob_max * leg2_prob_max * (1-leg3_prob_max) * leg4_prob_max * 1.5) + (leg1_prob_max * leg2_prob_max * leg3_prob_max * (1-leg4_prob_max) * 1.5) - 1
    ev95_4legi = [ev95_4legi_min, ev95_4legi_max]
    ## Put data in stats_4legi
    stats_4legi = [ev_4legi, ev95_4legi, cumprob_4legi, 0, 0]

## 5 Leg Bet 
# Input: leg1_prob, leg2_prob, leg3_prob, leg4_prob, leg5_prob, leg1_sd, leg2_sd, leg3_sd, leg4_sd, leg5_sd
# Output: EV, 95% EV, CUM PROB 
def get_5leg(): 
    global stats_5leg 
    ## Get CUM PROB  
    cumprob_5leg = (leg1_prob * leg2_prob * leg3_prob * leg4_prob * leg5_prob)
    ## Get the EV 
    ev_5leg = (cumprob_5leg * 20) - 1
    ## Get 95% EV 
    ev95_5leg_min = ((leg1_prob_min) * (leg2_prob_min) * (leg3_prob_min) * (leg4_prob_min) * (leg5_prob_min) * 20) - 1 
    ev95_5leg_max = ((leg1_prob_max) * (leg2_prob_max) * (leg3_prob_max) * (leg4_prob_max) * (leg5_prob_max) * 20) - 1 
    ev95_5leg = [ev95_5leg_min, ev95_5leg_max]
    ## Put data in stats_4leg  
    stats_5leg = [ev_5leg, ev95_5leg, cumprob_5leg, 0, 0]

## 5 Leg Bet Insured 
# Input: leg1_prob, leg2_prob, leg3_prob, leg4_prob, leg5_prob, leg1_sd, leg2_sd, leg3_sd, leg4_sd, leg5_sd
# Output: EV, 95% EV, CUM PROB 
def get_5legi():
    global stats_5legi
    ## Get CUM PROB   
    cumprob_5legi = (leg1_prob * leg2_prob * leg3_prob * leg4_prob * leg5_prob)
    ## Get the EV 
    ev_5legi = (cumprob_5legi * 10) + ((1 - leg1_prob) * leg2_prob * leg3_prob * leg4_prob * leg5_prob * 2.5) + (leg1_prob * (1 - leg2_prob) * leg3_prob * leg4_prob * leg5_prob * 2.5) + (leg1_prob * leg2_prob * (1-leg3_prob) * leg4_prob * leg5_prob * 2.5) + (leg1_prob * leg2_prob * leg3_prob * (1-leg4_prob) * leg5_prob * 2.5) + (leg1_prob * leg2_prob * leg3_prob * leg4_prob * (1-leg5_prob) * 2.5) - 1
    ## Get 95% EV 
    ## Get 95% EV 
    ev95_5legi_min = (leg1_prob_min * leg2_prob_min * leg3_prob_min * leg4_prob_min * leg5_prob_min * 10) + ((1 - leg1_prob_min) * leg2_prob_min * leg3_prob_min * leg4_prob_min * leg5_prob_min * 2.5) + (leg1_prob_min * (1 - leg2_prob_min) * leg3_prob_min * leg4_prob_min * leg5_prob_min * 2.5) + (leg1_prob_min * leg2_prob_min * (1-leg3_prob_min) * leg4_prob_min * leg5_prob_min * 2.5) + (leg1_prob_min * leg2_prob_min * leg3_prob_min * (1-leg4_prob_min) * leg5_prob_min * 2.5) + (leg1_prob_min * leg2_prob_min * leg3_prob_min * leg4_prob_min * (1-leg5_prob_min) * 2.5) - 1
    ev95_5legi_max = (leg1_prob_max * leg2_prob_max * leg3_prob_max * leg4_prob_max * leg5_prob_max * 10) + ((1 - leg1_prob_max) * leg2_prob_max * leg3_prob_max * leg4_prob_max * leg5_prob_max * 2.5) + (leg1_prob_max * (1 - leg2_prob_max) * leg3_prob_max * leg4_prob_max * leg5_prob_max * 2.5) + (leg1_prob_max * leg2_prob_max * (1-leg3_prob_max) * leg4_prob_max * leg5_prob_max * 2.5) + (leg1_prob_max * leg2_prob_max * leg3_prob_max * (1-leg4_prob_max) * leg5_prob_max * 2.5) + (leg1_prob_max * leg2_prob_max * leg3_prob_max * leg4_prob_max * (1-leg5_prob_max) * 2.5) - 1
    ev95_5legi = [ev95_5legi_min, ev95_5legi_max]
    ## Put data in stats_4leg  
    stats_5legi = [ev_5legi, ev95_5legi, cumprob_5legi, 0, 0]

################################################################
##### CALLING ALL THE BET INFORMATION TO RUN 
def main_get_bets():
    get_2leg()
    get_3leg() 
    get_3legi()
    get_4leg()
    get_4legi()
    get_5leg()
    get_5legi()
    
################################################################
##### DISPLAY CHART / GRAPH 
def main_get_chart(): 
    global final_bets, stats_2leg , stats_3leg , stats_3legi , stats_4leg , stats_4legi , stats_5leg , stats_5legi 
    titles = ["2 Leg Parley" , "3 Leg Parley" , "3 Leg Parley Insured" , "4 Leg Parley" , "4 Leg Parley Insured" , "5 Leg Parley" , "5 Leg Parlay Insured "]
    final_bets = [stats_2leg , stats_3leg, stats_3legi , stats_4leg , stats_4legi, stats_5leg, stats_5legi]
    print("THIS IS THE SOLVED BETTING EV AND PROBABILITIES")
    for i in range(0,7):
        temp1 = (titles[i])
        temp2 = round((final_bets[i][0]),3)
        temp3 = round((final_bets[i][1][0]) ,3)
        temp4 = round((final_bets[i][1][1]) ,3)
        temp5 = round((final_bets[i][2]) ,3)
        temp6 = round((final_bets[i][3]),2)
        temp7 = round((final_bets[i][4]),2)

        temp_message = (str(temp1) +" | EV: " + str(temp2) + " | Cumlative Probability: " + str(temp5) +  "| 95% Value: (" + str(temp3) + "-" + str(temp4) + "), 95% W/L Ratio: " + str(temp6) + ", 95% Win %: " + str(temp7) +"%")
        print("")
        print(temp_message)
        

################################################################
####### GENERAL MAIN FUNCTION 
def main_main():
    transcribe_data(test_list)
    transcribe_min_max_prob(test_list)
    main_get_bets()
    main_get_chart()

main_main() 


