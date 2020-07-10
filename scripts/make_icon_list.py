import os, json


types = os.listdir('./public/icons')
icons_dict = {}
for t in types:
    icons_dict[t] = {}
    icons = os.listdir('./public/icons/' + t)
    for ico in icons:
        ico_split = ico.split('-')
        ico_id = ico_split[0]
        name = ico_split[1].split('.')[0].title()
        icons_dict[t][ico_id] = {'name' : name, 'path' : '/icons/' + t + '/' + ico}

with open('src/assets/icon_list.json', 'w+') as f:
    f.write(json.dumps(icons_dict, indent=4, sort_keys=True))
