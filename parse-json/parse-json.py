import json

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    with open('facts.json') as json_file:
        data = json.load(json_file)
        for item in data['all']:
            if 'user' not in item:
                continue
            if 'name' not in item['user']:
                continue
            
            user_name_data = item['user']['name']
            first_name = user_name_data['first']
            last_name = user_name_data['last']

            print(first_name + ' ' + last_name)
  
    # First level is an array called all so iterate through the list
    # for item in json_list:
    #     print(item['user']["_id"] + '\n')
    # for item in json_list[]:
    #     print(item['user'] + '\n')
    # print("end")
    return 0

if __name__ == "__main__":
    main()