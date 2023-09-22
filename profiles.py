#!/usr/bin/env python
import json
import os


# player_name = input("Input profile name": )
player_name = "deb"
player_profile = f"{player_name}.json"

if os.path.isfile(player_profile):
    with open(player_profile) as json_file:
        data = json.load(json_file)
        print(data)
        print(data.get('win'))
else:
    print('no player profile exist')

data['something new'] = 'foo'
json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("deb2.json", "w") as outfile:
    outfile.write(json_object)