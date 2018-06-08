import json

with open('player.json') as json_file:  
    playerdata = json.load(json_file)
    print(playerdata)
    print(str(len(playerdata['players'])))
    print(playerdata['players'][0]["Name"])
    print(playerdata['players'][1]["Name"]) 

    playerdata['players'][0]['isPlaying'] = True
    
for p in playerdata['players']:
    if p['isPlaying'] == True :
        print('ID: ' + str(p))
    #print('Name: ' + p['Name'])
    #print('Score: ' + p['Score'])
    #p['Score'] = '10'
    #print('Score: ' + p['Score'])

#playerdata['players']['Score']
