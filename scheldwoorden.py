#!usr/bin/python3

import os
import gzip
import collections
import json




def main():
    scheldwoorden = []
    cities = []
    places = []
    villages = []
    gemeentes = []

    with open('scheldwoorden.txt') as scheldwoorden_file:
        for line in scheldwoorden_file:
            line = line.split()
            scheldwoorden.append(line[3])
    with open('places.txt') as places_file:
        for line in places_file:
            places.append(line.strip())
    with open('cities.txt') as cities_file:
        for line in cities_file:
            cities.append(line.strip())
    with open('gemeentes.txt') as gemeentes_file:
        for line in gemeentes_file:
            gemeentes.append(line.strip())       

    village_count = 0
    city_count = 0
    village_tweets = 0
    cities_tweets = 0
    path = os.path.abspath('/home/evadyadko/iwo')
    os.chdir(path)

    for place in places:
        for city in cities:
            for gemeente in gemeentes:
                if city and gemeente not in place:
                    villages.append(place)

    villages = set(villages)


    for subdirect in os.listdir(path):
        if subdirect == '02':
            for filename in os.listdir(subdirect):
                with gzip.open(path + '/' + subdirect + '/' + filename, 'rb') as tweets:

                    for line in tweets:
                        data = json.loads(line.decode('utf-8'))
                        tweet = data['text']
                        tweet = tweet.lower()
                        wordlist = tweet.split(' ')   
                        loc = data['user']['location']

                        if loc == None:
                            pass
                        elif any(cit in loc for cit in cities):
                            cities_tweets += 1
                        elif any(vil in loc for vil in villages):
                            village_tweets += 1


                        if any(x in wordlist for x in scheldwoorden):
                            if loc == None:
                                pass
                            elif any(cit in loc for cit in cities):
                                city_count += 1
                            elif any(vil in loc for vil in villages):
                                village_count += 1

    percentage_village = 0
    percentage_city = 0

    try:
        percentage_village = village_count/village_tweets*100
        percentage_city = city_count/cities_tweets*100

    except ZeroDivisionError:
        pass


    print("The amount of tweets that contain an offensive word (village) is: {}".format(village_count))
    print("The amount of tweets that contain an offensive word (city) is: {}".format(city_count))
    print("Total tweets from people from a village: {}".format(village_tweets))
    print("Total tweets from people from a city: {}".format(cities_tweets))



    print("The relative percentage for villages: {}".format(percentage_village))
    print("The relative percentage for cities: {}".format(percentage_city))



if __name__  == '__main__':
    main()