# coding: utf-8

# https://pythonians.medium.com/13-advanced-python-scripts-for-everyday-programming-8de4c6dba476

import uvicorn
from fastapi import HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi import BackgroundTasks,FastAPI
import os
from dotenv import load_dotenv

from google_trends import Google_Pytrends
from google_news import get_google_news
from twitter_api import Twitter_search

import config
origins = config.origins

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/google_trends_three")
def get_google_trends_three(query: str):
    # criar instancia aqui para ter uma instancia para cada requisicao (evitar compartilhamento de instancia caso mais de um usuario acesse ao mesmo tempo)
    gts = Google_Pytrends()
    gts.build_payload([query])
    int_over_time = gts.get_interest_over_time()
    realtime_searches = gts.get_realtime_searches('BR')
    today_hot_trends_dict = gts.get_today_hot_trends(query)
    return {"response": "ok",
            "today_hot_trends":today_hot_trends_dict,
            "int_over_time":int_over_time,
            "realtime_searches":realtime_searches
            }

@app.get("/gt_hot")
def get_google_trends_hot_trends(query: str):
    # criar instancia aqui para ter uma instancia para cada requisicao (evitar compartilhamento de instancia caso mais de um usuario acesse ao mesmo tempo)
    gts = Google_Pytrends()
    gts.build_payload([query])
    today_hot_trends_dict = gts.get_today_hot_trends(query)
    return {"response": "ok",
            "results":today_hot_trends_dict,
            }

@app.get("/gt_time")
def get_google_trends_interest_over_time(query: str):
    # criar instancia aqui para ter uma instancia para cada requisicao (evitar compartilhamento de instancia caso mais de um usuario acesse ao mesmo tempo)
    gts = Google_Pytrends()
    gts.build_payload([query])
    int_over_time = gts.get_interest_over_time()
    return {"response": "ok",
            "results":int_over_time,
            }


@app.get("/gt_realtime")
def get_google_trends_realtime():
    # criar instancia aqui para ter uma instancia para cada requisicao (evitar compartilhamento de instancia caso mais de um usuario acesse ao mesmo tempo)
    gts = Google_Pytrends()
    realtime_searches = gts.get_realtime_searches('BR')
    return {"response": "ok",
            "results":realtime_searches
            }


@app.get("/google_news")
def get_google_news_data(query: str):
    results = get_google_news(query)
    return {"response":"ok",
            "search_results":results}


@app.get("/twt_search")
def get_twt_data(query: str):
    try:    
        twt = Twitter_search()
        results = twt.search_var(query)
        # created_at,  hashtags [] , lang, retweet_count, text, user {}

        trends = twt.get_trends_by_location('BR')
        # trends: name, query, timestamp, url, tweet_volume 
        response = "ok"
    except Exception as e:
        response = "except"
        results = str(e)
        trends = ""
    return { "response":response,
                "results":results,
                "trends":trends}


@app.get("/")
def read_root():
    return {"response": "welcome try /docs"}



if __name__=='__main__':
    port=80
    print('listening on port {}'.format(port))
    uvicorn.run(app, host="0.0.0.0", port=port)