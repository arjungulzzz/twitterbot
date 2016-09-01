import tweepy
import sys
import time
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
consumer_key = 'oPyIJbtdDPcYs89zc3Me3Ag9d'
consumer_secret = 'Ubv3S9yfBF29YFgpHByggJ1x9SiWqO2Zk7ciyd3fAwNdrtGkd2'
access_token = '769798187372642304-kDP8vVwySEKqrUEcrT113PJKc7C8YtW'
access_token_secret = 'R0vA6qCnGA8tfM2vNbD8ibHYV6Ses6YDA0WRUXtsqquDm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
count=1
Past_Followers = 0
Current_Followers = 0
while(count>0):
    srk1 = api.get_user('@iamsrk')
    Past_Followers = srk1.followers_count
    api.update_status(status='@iamsrk Follower count is '+str(Past_Followers))
    time.sleep(86400)
    srk2 = api.get_user('@iamsrk')
    Current_Followers = srk2.followers_count
    api.update_status(status='Total Followers of @iamsrk = '+str(Current_Followers))
    api.update_status(status='New Followers Today = '+str(Current_Followers - Past_Followers))
    count=count+1
    print(count)
#Search_Results = api.search(q=("#Raees"))
#print(Search_Results.translate(non_bmp_map))
#api.update_status(status='@iamsrk Have a Nice Day')
#places = api.geo_search(query='India', granularity = 'country')
#place_id = places[0].id
#print(place_id)
#results = api.search(q = 'place:b850c1bfd38f30e0' , count=50)
#print(results.text)
#count=0
#for result in results:
    #results
    #print(result.text)
    #print(result.translate(non_bmp_map))
    #print(result.coordinates)
    #count=count+1
    #print(count)
    #text=result.text
    #print(text.translate(non_bmp_map))
    #print(result.coordinates)
'''for result in Search_Results:
    text=result.text
    print(text.translate(non_bmp_map))'''
