menu = \
    { "breakfast" : {
        "hours" : "7-11",
        "items" : {
            "breakfast burritos" : "$6.00",
            "pancakes" : "$4.00"}
        },
      "lunch" : {
        "hours" : "11-3",
        "items" : {
            "hamberger" : "$5.00"}
        },
      "dinner" : {
        "hours" : "3-10",
        "items" : {
            "spaghetti" : "$8.00"}
        }
      }

print(type(menu))

import json
menu_json = json.dumps(menu)
print(type(menu_json))
print(menu_json)

menu2 = json.loads(menu_json)
print(type(menu2))
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)

"""
for x in dir(json.JSONEncoder):
    print(x)
"""

import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
print(cfg)

print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])
