#lottery application
#lottery numbers (0-50)
#user enters name
#users enters number
# the application generate a number
# If your number matches the application number
#  the user wins the jackpot
# if the numbers dont match user losses

import random

def lottery_cal():
    users_name = input("Enter your name here:  ")
    user_num = int(input("Enter your number from 0 - 50 here: "))
    lottery_gen = random.randint(0,50)
    if lottery_gen  == user_num:
        print( users_name,"Your number is", user_num, "the lottery winning number is", lottery_gen, "you are lucky winner")
    else:
        print( users_name,"Your number is",user_num, "the lottery winning number is", lottery_gen, "you lost, try again")

  


lottery_cal()
