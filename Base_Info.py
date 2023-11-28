import json
def Basics(profile):
    Dictionary = {
        "User ID": profile.userid,
        "Number of Posts": profile.mediacount,
        "Number of Followers": profile.followers,
        "Number of Followees": profile.followees,
        "Biography":profile.biography,
    }

    Acct_json = json.dumps(Dictionary,indent=4)
    with open("Acct_Info.json","w") as out:
        out.write(Acct_json)
