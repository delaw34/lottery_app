
# lottery application
# jackpot winning number is 30
# lottery numbers (0-50)
# user enters name
# users enters numbers between 0-50
# the application generate a number
# If your the user number matches the lottery app number and the jackpot winning number 
#  the user wins the jackpot
# where the user numbers dont match the lottery app number user losses

jackpot_number = 30

import random

def lottery_cal():
    users_name = input("Enter your name here:  ")
    user_num = int(input("Enter your number from 0 - 50 here: "))
    lottery_gen = random.randint(0,50)
    if user_num > 50:
        print( "your input number", user_num, "is greater than 50, you are disqualified")
    elif user_num  == lottery_gen and lottery_gen == jackpot_number: 
        
        print( users_name,"Your number is", user_num, "your lottery winning number is", lottery_gen, "and the jackpot wining is", jackpot_number,  "CONGRATULATION! you are lucky winner")
    else:
        print( users_name,"Your number is",user_num, "your lottery winning number is", lottery_gen, "and the jackpot winning number is",jackpot_number, "you lost, try again")

  


lottery_cal()