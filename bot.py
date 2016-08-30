import tweepy
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
consumer_key = 'oPyIJbtdDPcYs89zc3Me3Ag9d'
consumer_secret = 'Ubv3S9yfBF29YFgpHByggJ1x9SiWqO2Zk7ciyd3fAwNdrtGkd2'
access_token = '769798187372642304-kDP8vVwySEKqrUEcrT113PJKc7C8YtW'
access_token_secret = 'R0vA6qCnGA8tfM2vNbD8ibHYV6Ses6YDA0WRUXtsqquDm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
places = api.geo_search(query='India', granularity = 'country')
place_id = places[0].id
#print(place_id)
#results = api.search(q = 'place:b850c1bfd38f30e0' , count=10)
#print(results.text)
#count=0
for result in api.search(q = 'place:b850c1bfd38f30e0' , count=10):
    #results
    #print(result.text)
    #print(result.translate(non_bmp_map))
    #print(result.coordinates)
    #count=count+1
    #print(count)
    text=result.text
    print(text.translate(non_bmp_map))
