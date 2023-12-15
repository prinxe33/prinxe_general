### Takes in 5 potential leg parameters and returns the EV for each of the normal legs 
 
leg_list = []

### Get 5 Inputs and Append them to leg_list in nested lists 
for i in range(1,6):
    temp_prob = input("What is the probaility of Leg #" +str(i)+ " being correct?: ") 
    temp_sd = input("What is the SD of Leg #" +str(i)+ " being correct?: ") 
    leg_list.append([float(temp_prob), float(temp_sd)])
print(leg_list)

### 
leg_list = sorted(leg_list, key=lambda x: x[0], reverse=True)

print("done")
print(leg_list)

leg1_prob, leg1_sd = 0,0
leg2_prob, leg2_sd = 0,0
leg3_prob, leg3_sd = 0,0
leg4_prob, leg4_sd = 0,0
leg5_prob, leg5_sd = 0,0

### Transribe the data to hard variables 
def transcribe_data(list_input): 
    global leg1_prob, leg1_sd, leg2_prob, leg2_sd, leg3_prob, leg3_sd, leg4_prob, leg4_sd, leg5_prob, leg5_sd
    leg1_prob, leg1_sd = leg_list[0]
    leg2_prob, leg2_sd = leg_list[1]
    leg3_prob, leg3_sd = leg_list[2]
    leg4_prob, leg4_sd = leg_list[3]
    leg5_prob, leg5_sd = leg_list[4]

transcribe_data(leg_list) 
print("this is leg 1 prob :"+ str(leg1_prob))
print("this is leg 1 sd :"+ str(leg1_sd))

####### Find the EV for each of the given bet formations (7 total) 
#### GLobals 
cum_prob_2leg = 0 
ev_2leg = 0 
cum_prob_3leg = 0 
ev_3leg_noin = 0 
ev_3leg_in = 0 

def find_evs():
    global cum_prob_2leg , ev_2leg , cum_prob_3leg , ev_3leg_in, ev_3leg_noin 

### 2 Leg Bet with Highest Values 
# SOLVE FOR : cum_prob , ev
    cum_prob_2leg = leg1_prob * leg2_prob
    ev_2leg = (2 * cum_prob_2leg) - (1 - cum_prob_2leg)  
    # WORKS SUCESSFULLY 
### 3 Leg Bet with Highest Values 
    cum_prob_3leg = leg1_prob * leg2_prob * leg3_prob 
    ev_3leg_noin = (cum_prob_3leg * 5) - (1 - cum_prob_3leg)
    ev_3leg_in = ( (3) * cum_prob_3leg) + 2*((1 - leg1_prob)*(leg2_prob)*(leg3_prob)) + 2*((leg1_prob)*(1 - leg2_prob)*(leg3_prob) )  + 2*((leg1_prob)*(leg2_prob)*(1 - leg3_prob)) - 1 


find_evs()