
# pip install python-twitter
# https://dev.twitter.com/rest/public/search
# https://python-twitter.readthedocs.io/en/latest/getting_started.html
# https://python-twitter.readthedocs.io/en/latest/genindex.html
import os
import pandas as pd
import twitter
#from sqlalchemy import create_engine
#from pprint import pprint

from dotenv import load_dotenv
load_dotenv()

config={
    'apikey':os.getenv('APIKEY','nokey'),
    'apisecret':os.getenv('APISECRET','nokey'),
    'accesstoken':os.getenv('ACCESSTOKEN','nokey'),
    'accesstokensecret':os.getenv('ACCESSTOKENSECRET','nokey'),
}
print(config)
# 15 chamadas a cada 15 minutos
class Twitter_search:
    def __init__(self):
        self.api = twitter.Api(consumer_key=config['apikey'],
                  consumer_secret=config['apisecret'],
                  access_token_key=config['accesstoken'],
                  access_token_secret=config['accesstokensecret'],
                  sleep_on_rate_limit=True)


    def search_var(self,text,geocode=None):
        """
        Search Text String on twitter
        returns list of Status 
        [Status(ID=1582021029253513216, ScreenName=MartiniGuyYT, Created=Mon Oct 17 14:49:40 +0000 2022, Text='Should i give away another')]
        Args: 
            text to search
            geocode (str or list or tuple, optional):
                Geolocation within which to search for tweets. Can be either a
                string in the form of "latitude,longitude,radius" where latitude
                and longitude are floats and radius is a string such as "1mi" or
                "1km" ("mi" or "km" are the only units allowed). For example:
              >>> api.GetSearch(geocode="37.781157,-122.398720,1mi").
        Returns: 
            return [Status.NewFromJsonDict(x) for x in data.get('statuses', '')]
        """
        r = self.api.GetSearch(term=text)
        
        rdict = []
        for i in r:
            rdict.append(i.AsDict())
        return rdict


    def search_raw_query(self, raw_query):
        """
        you can use Twitter Advanced Search tool: https://twitter.com/search-advanced, 
        and then use the part of search URL after the “?” to use for the Api, removing the &src=typd portion.
        RAW QUERY, includes since, count variables
        results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
        """
        print("++++++++++ RAW_QUERY ++++++++++++")
        results = self.api.GetSearch(raw_query=raw_query)
        return results
        
    def get_trends(self):
        """ TRENDS CURRENT 
        """
        r = self.api.GetTrendsCurrent()
        return r

    # https://codebeautify.org/jsonviewer/f83352
    #r = api.GetTrendsWoeid(woeid='23424977') #EUA

    def get_trends_by_location(self, location):
        """
        woeid='23424768' BR
        curitiba 455822 (array 81) , brasilia 455819 ; sao paulo 455827 ; rio de janeiro 455825 , recife 455824
        Trend(Name='#GetKicksListing', Time=2022-10-18T14:33:25Z, URL=http://twitter.com/search?q=%23GetKicksListing)
        Return
        """
        if location =='BR':
            woeid='23424768'
        elif location =='US':
            woeid='23424977'
        elif location =='RJ':
            woeid='455825'
        elif location =='SP':
            woeid='455827'
        else:
            woeid='BR'
        trends = self.api.GetTrendsWoeid(woeid=woeid)
        
        rdict = []
        for i in trends:
            rdict.append(i.AsDict())
        return rdict


    def get_user(self, screen_name):    
        """
        r = api.GetUserRetweets()
        fulltextsplit = twt.text.split(" ")
        """
        r = self.api.GetUser(screen_name=screen_name)
        return r
        

if __name__=='__main__':
    twit=Twitter_search(config)
    
    #r_dict = twit.search_var("iphone 14")
    #print(r_dict)
    
    r = 1#twit.get_trends_by_location('BR')
    print(r)
    print(type(r))

    