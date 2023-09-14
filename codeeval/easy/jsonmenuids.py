#!/usr/bin/python

import sys
import json

for line in open (sys.argv[1],'r'):
    menu_ids = json.loads(line.rstrip())
    count = 0
    for i in range(len(menu_ids["menu"]["items"])):#int(str(menu_ids["menu"]["items"]).count('}'))):
        temp = menu_ids["menu"]["items"][i]
        if not temp == None and 'label' in temp:
            count += temp["id"]
    print count
