# https://github.com/GeneralMills/pytrends/blob/master/examples/example.py
# https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
# https://github.com/Tanu-N-Prabhu/Python/blob/master/Google_Trends_API.ipynb

# pip install pytrends

from pytrends.request import TrendReq
import time
INTERVAL = 0.5
# status code 429: Too many requests

class Google_Pytrends:
    def __init__(self):#,name_search):
       self.pytrend = TrendReq()
       #self.query = name_search
    
    def build_payload(self, payload_list):
        """
         Create payload and capture API tokens. 
         Only needed for interest_over_time(), interest_by_region() & related_queries()
        """
        self.pytrend.build_payload(kw_list=payload_list)
        time.sleep(INTERVAL)
        return "ok"


    def get_interest_over_time(self):
        """ 
        Interest Over Time
        """
        try:
            df = self.pytrend.interest_over_time()
            time.sleep(INTERVAL)
            df_dict = {"status":"ok",
                        "results":df.to_dict()
                        }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
        return df_dict

    def get_interest_by_region(self):
        """Interest by Region
        """
        try:
            df = self.pytrend.interest_by_region()
            time.sleep(INTERVAL)
            df_dict =  {"status":"ok",
                        "results":df.to_dict()
                        }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
        return df_dict


    def get_related_queries(self):
        """ 
            Related Queries, returns a dictionary of dataframes
        """
        try:
            related_queries_dict = self.pytrend.related_queries()
            time.sleep(INTERVAL)
            df_dict ={"status":"ok",
                        "results":related_queries_dict
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }        
        return df_dict


    def get_trending_searches(self):
        # Get Google Hot Trends data
        try:
            df = self.pytrend.trending_searches()
            time.sleep(INTERVAL)
            df_dict = {"status":"ok",
                        "results":df.to_dict()
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
        return df_dict


    def get_today_hot_trends(self):
        # Get Google Hot Trends data
        try:
            df = self.pytrend.today_searches()
            time.sleep(INTERVAL)
            df_dict ={"status":"ok",
                        "results":df.to_dict()
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
        return df_dict


    def get_top_charts(self,hl,tz,geo):
        """
            Get Google Top Charts
            Params: hl='en-US', tz=300, geo='GLOBAL'
            Returns: pandas dataframe
        """
        try:
            df = self.pytrend.top_charts(2018, hl=hl, tz=tz, geo=geo)
            time.sleep(INTERVAL)
            df_dict ={"status":"ok",
                        "results":df.to_dict()
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
        return df_dict


    def get_today_hot_trends(self, keyword_to_get_suggestions):
        """ 
            Get Google Keyword Suggestions
            Params: str keyword_to_get_suggestions
            Returns: dict suggestions
        """
        try:
            suggestions_dict = self.pytrend.suggestions(keyword=keyword_to_get_suggestions)
            time.sleep(INTERVAL)
            df_dict ={"status":"ok",
                        "results":suggestions_dict
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
            
        return df_dict


    def get_realtime_searches(self, pn='BR'):
        """
            Get Google Realtime Search Trends
            Params: str pn country to search with two capital letters BR, US
            Returns: realtime_searches
        """
        try:
            df_results = self.pytrend.realtime_trending_searches(pn=pn)
            #df_dict = df_results['title'].astype('category').values
            df_dict = df_results['title'].to_list()
            
            time.sleep(INTERVAL)
            df_dict = {"status":"ok",
                        "results":df_dict
                    }
        except Exception as e:
            df_dict = {
                "status":"exception",
                "results":str(e)
            }
            
        return df_dict


if __name__=='__main__':
    print("main")
    query='Flamengo'
    gts = Google_Pytrends()
    #gts.build_payload([query])

    #int_over_time = gts.get_interest_over_time()
    #realtime_searches = gts.get_realtime_searches('BR')
    today_hot_trends_dict = gts.get_today_hot_trends(query)

    #print(int_over_time)
    print('=======')

    #print(realtime_searches)
    print('=======')

    print(today_hot_trends_dict)
    print(type(today_hot_trends_dict))
    print('=======')






