import os
import json

with open("./config/websites.json") as data:
    websites = json.load(data)
    for website in websites["websites"]:
        if (not os.path.exists("./apps/"+website["name"])):
            os.system("cd ./apps && react-native init "+website["name"])
            if (os.path.exists("./apps"+website["name"])):
                print("create routes now")
        else:
            pass
    