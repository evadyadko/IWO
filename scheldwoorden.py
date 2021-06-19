#!usr/bin/python3

import os
import gzip
import collections
import json




def main():
    scheldwoorden = []
    cities = []

    with open('scheldwoorden.txt') as scheldwoorden_file:
        for line in scheldwoorden_file:
            line = line.split()
            scheldwoorden.append(line[3])
    with open('cities.txt') as cities_file:
        for line in cities_file:
            cities.append(line.strip())

    village_count = 0
    city_count = 0
    path = os.path.abspath('/home/eva/2019/')
    os.chdir(path)
    for subdirect in os.listdir(path):
        for filename in os.listdir(subdirect):
            with gzip.open(path + '/' + subdirect + '/' + filename, 'rb') as tweets:

                for line in tweets:
                    data = json.loads(line.decode('utf-8'))
                    tweet = data['text']
                    tweet = tweet.lower()
                    wordlist = tweet.split(' ')   
                    loc = data['user']['location']

                

                    
                    if any(x in wordlist for x in scheldwoorden):
                        if loc == None or loc == 'Nederland' or loc == 'NL' or loc == 'Netherlands':
                            pass
                        elif any(cit in loc for cit in cities):
                            city_count += 1
                        else:
                            village_count += 1

    print("The amount of tweets that contain an offensive word (village) is: {}".format(village_count))
    print("The amount of tweets that contain an offensive word (city) is: {}".format(city_count))


if __name__  == '__main__':
    main()
