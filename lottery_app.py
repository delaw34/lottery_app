#lottery application
#lottery numbers (0-50)
#jackpot number is 30
#users enters name
#If your number matches the jackpot number then user wins the prize

import random
jackpot_number = "30"

def lottery_cal():
    users_name = input("Enter your name here:  ")
    lottery_gen = random.randint(0,50)
    if lottery_gen  == jackpot_number:
        print( users_name,"Your results is", lottery_gen, "you are lucky winner")
    else:
        print( users_name,"Your lottery numbers is", lottery_gen, "you lost the winning number is 30, try again")

  


lottery_cal()