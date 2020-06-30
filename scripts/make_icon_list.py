import os, json


types = os.listdir('./public/icons')
icons_dict = {}
for t in types:
    icons = os.listdir('./public/icons/' + t)
    for ico in icons:
        ico_split = ico.split('-')
        ico_id = ico_split[0]
        if ico_id not in icons_dict.keys():
            icons_dict[ico_id] = {'name' : '', 'types': {}}
        name = ico_split[1].split('.')[0].title()
        icons_dict[ico_id]['name'] = name
        icons_dict[ico_id]['types'][t] = {'path' : '/icons/' + t + '/' + ico}

with open('src/assets/icon_list.json', 'w+') as f:
    f.write(json.dumps(icons_dict, indent=4, sort_keys=True))
