import yfinance as yf
import csv 
from datetime import datetime

####################
##-Demo Portfolio-##
#################### 
##-USE CASES 
#- Add to Holdings
#   - Collect Trade from User 
#   - Input Trade into demo_portfolio_csv_path 
#   - Re-run Stats collection on demo_portfolio_csv_path to find new values for demo_portfolio_status_path
#- Reduce Holdings
#   - Print out current trades in a numbered list 
#   - Enter the percent that the trade shoud be reduced 
#- Check Holdings
#   1. Trade Balances
#       - Go through demo_portfolio_csv_path to find balance of each trade 
#       - Give a report on each Trade Balance 
#           - PnL of each trade with balance (1D,1W,1M,1Y)
#   2. Portfolio Balance
#       - Go through demo_portfolio_csv_path to find balance for each equity 
#       - Give a report on Porfolio Balance
#           - PnL of each Equity with balance (1W, 1D, 1M, 1Y)
#################### 
# Path to csv with trades
demo_portfolio_csv_path = "C:\\Users\\ethan\\Desktop\\github rep\\prinxe_general\\demo_portfolio\\demo_portfolio_trades.csv"
# Path to csv with Porfolio Stats
demo_portfolio_status_path = "C:\\Users\\ethan\\Desktop\\github rep\\prinxe_general\\demo_portfolio\\demo_portfolio_status.csv"
# Path to csv with Portfolio Stock Amounts 
demo_portfolio_path = "C:\\Users\\ethan\\Desktop\\github rep\\prinxe_general\\demo_portfolio\\demo_portfolio_equities.csv" 
# Temporary storage for trade order 
complete_trade =  []
 
## inputing_trade() 
# Parameters: None 
# Purpose: Run to add uesr input about trade to append each value to complete_trade (list)
def inputing_trade(): 
    global complete_trade 
    Ticker_input = input("Ticker: ")
    LongShort_input = input("LongShort: ")
    Date_input = input("Date: (YYYY-MM-DD HH:MM) ")
    Amount_input = int(input("Amount: ")) 
    for i in [Ticker_input,LongShort_input,Date_input,Amount_input]:
        complete_trade.append(i)

## find_buy_price(input1, input2)
# Parameters: input1 = (Ticker symbol), input2 = (Date in this format "YYYY-MM-DD HH:MM")
# Purpose: To locate the price at input2 of input1 and append it to complete_trade (list)
def find_buy_price(input1,input2): 
    global complete_trade
    ticker1 = yf.Ticker(input1)
    intraday_data = ticker1.history(period='1d', interval='1m')
    desired_time = datetime.strptime(input2, '%Y-%m-%d %H:%M')
    intraday_time_format = desired_time.strftime('%Y-%m-%d %H:%M:%S')
    price_at_desired_time = intraday_data.loc[intraday_time_format]['Close']
    complete_trade.append(round(price_at_desired_time,4))

## find_buy_amount(trade_input)
# Parameters: trade_inpupt = (complete_trade)
# Purpose: To find the amount of stock bought and append it to complete_trade
def find_buy_amount(trade_input):
    global complete_trade 
    if trade_input[1] == "Long" or trade_input[1] == "LONG" or trade_input[1] == "long" or trade_input[1] == str(1): 
        complete_trade.append(round((float(trade_input[3])*float(1000))/float(trade_input[4])))
    elif trade_input[1] == "Short" or trade_input[1] == "SHORT" or trade_input[1] == "short" or trade_input[1] == str(0): 
        complete_trade.append(float(-1)*round((float(trade_input[3])*float(1000))/float(trade_input[4])))
    
## trascribetocsv(trade_input,link) 
# Parameters: trade_input = (list), link =(link to csv file)
# Purpose: To add trade_input as a new line to the linked csv file 
def transcribetocsv(trade_input,link): 
    with open(link, "a") as file: 
        writer = csv.writer(file)
        writer.writerow(trade_input)

## recordingstas(trade_input)
# Parameters: Hardcoded linked to demo_portfolio_status_path, trade_input = (complete_trade)
# Purpose: To add 
def recordingstats(trade_input):
    global demo_portfolio_status_path
    updated_lines = []
    total_invested = 0 
    sum_long = 0 
    sum_short = 0 
    with open(demo_portfolio_status_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "Number__of_trades":
                row[1] = int(row[1])+ 1 
                updated_lines.append(row)
            elif row[0] == "Sum_Liquid":
                row[1] = float(row[1]) - ((float(trade_input[3])*float(1000)))
                updated_lines.append(row)
            elif row[0] == "Percent_Liquid":
                row[1] = ((float(row[1])*float(100000)) - ((float(trade_input[3])*float(1000)))) / float(100000)
                updated_lines.append(row)
            elif row[0] == "Sum_Invested":
                total_invested = float(row[1]) + ((float(trade_input[3])*float(1000)))
                row[1] = float(row[1]) + ((float(trade_input[3])*float(1000)))
                updated_lines.append(row)
            elif row[0] == "Percent_Invested":
                row[1] = ((float(row[1])*float(100000))+((float(trade_input[3])*float(1000)))) /float(100000)
                updated_lines.append(row)
            elif row[0] == "Sum_Long":
                if trade_input[1] == "Long" or trade_input[1] == "LONG" or trade_input[1] == "long" or trade_input[1] == str(1):
                    row[1] = float(row[1]) + (float(trade_input[3])*float(1000))
                    sum_long = row[1]
                    updated_lines.append(row)
                else:
                    sum_long = row[1]
                    updated_lines.append(row)
            elif row[0] == "Sum_Short":
                if trade_input[1] == "Short" or trade_input[1] == "SHORT" or trade_input[1] == "short" or trade_input[1] == str(0):
                    row[1] = float(row[1]) + (float(trade_input[3])*float(1000)) 
                    sum_short = row[1]
                    updated_lines.append(row)
                else: 
                    sum_short = row[1]
                    updated_lines.append(row)
            elif row[0] == "Percent_Long":
                if trade_input[1] == "Long" or trade_input[1] == "LONG" or trade_input[1] == "long" or trade_input[1] == str(1):
                    row[1] = float(sum_long) / float(total_invested)
                    updated_lines.append(row)
                else:
                    row[1] = float(sum_long) / float(total_invested)
                    updated_lines.append(row)
            elif row[0] == "Percent_Short":
                if trade_input[1] == "Short" or trade_input[1] == "SHORT" or trade_input[1] == "short" or trade_input[1] == str(0):
                    row[1] = float(sum_short) / float(total_invested)
                    updated_lines.append(row)
                else:
                    row[1] = float(sum_short) / float(total_invested) 
                    updated_lines.append(row)        

    # Write the updated lines back to the CSV file
    with open(demo_portfolio_status_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_lines)

def add_to_holdings():
    global complete_trade
    inputing_trade()
    find_buy_price(complete_trade[0],complete_trade[2])
    find_buy_amount(complete_trade)
    transcribetocsv(complete_trade,demo_portfolio_csv_path)
    recordingstats(complete_trade) 
# add_to_holdings()
    
def print_out_trades(link):
    with open(link, 'r') as file:
        reader = csv.reader(file)
        i = 1 
        for row in reader:
            print("Trade #" + str(i) + str(row))
            i+=1 
            
def reduce_holdings():
    print_out_trades(demo_portfolio_csv_path) 

reduce_holdings()  


def update_portfolio_shares(): 
    global demo_portfolio_csv_path
    temp = []
    temp2 = [] 
  
    with open(demo_portfolio_csv_path,'r') as file: 
        reader = csv.reader(file)
        for row in reader: 
            if len(row) != 0: 
                temp.append(row)

    for i in temp:
        if len(temp2) == 0: 
            temp2.append([(i[0]),float((i[5]))])
        else: 
            temp3 = 0 
            while temp3 < 1: 
                for j in temp2: 
                    if j[0] == i[0]:
                        j[1] = float((j[1])) + float((i[5]))
                        temp3 += 1 
                if temp3 == int(0): 
                    temp2.append([(i[0]),float((i[5]))])
                    temp3 += 1 
            
     
        with open(demo_portfolio_path, "w") as file: 
            for item in temp2:
                writer = csv.writer(file)
                writer.writerow(item)
 
def create_netportfolio_amounts():
    update_portfolio_shares()
# create_netportfolio_amounts()