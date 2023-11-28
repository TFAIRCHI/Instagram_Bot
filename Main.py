import instaloader 
import pandas as pd

from Credentials import password, Username
from Follow import Get_Followers, Get_Following
from Base_Info import Basics

if __name__ == ('__main__'):
    bot = instaloader.Instaloader()
    bot.login(user=Username,passwd=password)
    profile = instaloader.Profile.from_username(bot.context,Username)
    Basics(profile)
    Get_Followers(profile)
    Get_Following(profile)
