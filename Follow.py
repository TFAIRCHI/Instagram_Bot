import pandas as pd
def Get_Followers(profile):
    followers = [follower.username for follower in profile.get_followers()]
    followers_df = pd.DataFrame(followers)
    followers_df.to_csv('Followers.txt',index=False,header=None)

def Get_Following(profile):
    following = [followee.username for followee in profile.get_followees()]
    following_df = pd.DataFrame(following)
    following_df.to_csv('Following.txt',index=False,header=None)