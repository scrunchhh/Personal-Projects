import json
import pandas as pd

path = 'noc.json' #path to the json file
with open(path, 'r', encoding='utf-8') as noc: #read only
    data = json.load(noc) #load the json file in this python file

x = 0

#keywords to compare in captions
keywordsPeloton = ['peloton', 'peloton', 'leaderboard', ' lb ', ' #lb ', 'edm ride', 'pop ride', 'edmride', 'popride']
keywordsExercise = ['gym', 'exercise', 'workout', 'bench', 'squat', 'dealift',  'training', 'fitness', ' tread ', 'trail', 'strength', 'lifting']
keywordsSpExercise = ['demand ', ' OD ', 'bike', 'hike', 'boxing', 'treadmill', 'bootcamp', 'hiking,', 'biking', 'edm ride', 'pop ride', 'edmride', 'popride', 'rock ride', 'rockride',]
keywordsCause = ['charity']
keywordsSponsored = ['sponsor', '#ad', ' ad ', '#ads ', ' ads ']
keywordsManual = [' ich ', '#ich,', 'organization', '#organization', 'partner', '#partner', 'partnered', '#partnered', 'episode', '#episode', 'class', '#class', 'schedule', '#schedule', 'classes', '#classes'] 

l = 0

for i in data:
    for i in keywordsPeloton:
        if i in data[x]['caption'].lower():
            with open(path, 'w') as noc: 
                data[x]["pelotonrelated"] = 1 
                json.dump(data, noc, indent=6)
                print(f'line {l} is complete for user ')
                print(data[x]['username'])
                l += 1
        else:
            pass
    for i in keywordsExercise:
        if i in data[x]['caption'].lower():
            with open(path, 'w') as noc:
                data[x]["exerciserelated"] = 1 
                json.dump(data, noc, indent=6)
                print(f'line {l} is complete for user ')
                print(data[x]['username'])
                l += 1
        else:
            pass
    for i in keywordsSpExercise:
        if i in data[x]['caption'].lower():
            with open(path, 'w') as noc: 
                data[x]["specificexercisementioned"] = 1 
                data[x]["exerciserelated"] = 1 
                data[x]["pelotonrelated"] = 1
                json.dump(data, noc, indent=6)
                print(f'line {l} is complete for user ')
                print(data[x]['username'])
                l += 1
        else:
            pass
    for i in keywordsCause:
        if i in data[x]['caption'].lower():
            with open(path, 'w') as noc:
                data[x]["cause"] = 1 
                json.dump(data, noc, indent=6)
                print(f'line {l} is complete for user ')
                print(data[x]['username'])
                l += 1
        else:
            pass
    for i in keywordsSponsored:
        if i in data[x]['caption'].lower():
            with open(path, 'w') as noc:
                data[x]["sponsored"] = 1 
                json.dump(data, noc, indent=6)
                print(f'line {l} is complete for user ')
                print(data[x]['username'])
                l += 1
        else:
            pass
    for i in keywordsManual:
        if i in data[x]['caption'].lower() and data[x]['exerciserelated'] != 1 and data[x]['pelotonrelated'] != 1 and data[x]["specificexercisementioned"] != 1:
            with open(path, 'w') as noc:
                    data[x]["checkline"] = 'please check this'
                    json.dump(data, noc, indent=6)
                    print(f'line {l} is complete for user ')
                    print(data[x]['username'])
                    l += 1
        else:
            pass
    if 'peloton' in data[x]['username']:
        with open(path, 'w') as noc:
            data[x]["sponsored"] = 1
            data[x]["exerciserelated"] = 1 
            data[x]["pelotonrelated"] = 1 
            json.dump(data, noc, indent=6)
            print(f'line {l} is complete for user ')
            print(data[x]['username'])
            l += 1

    x += 1

df = pd.read_json("noc.json")
df.to_csv('csvnoc.csv', encoding = 'utf-8', index = False)
