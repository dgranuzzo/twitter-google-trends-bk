
# coding: utf-8
# https://ealexbarros.medium.com/utilizando-python-para-armazenar-not%C3%ADcias-google-news-api-6d37f84cd426
# https://github.com/Iceloof/GoogleNews

from GoogleNews import GoogleNews
#import pandas as pd

def get_google_news(search_text, language='pt'):
    """
        Get Google News data
        Params: search_text str
        Returns: results dict
    """
    g_news = GoogleNews(period='d')
    g_news.setlang(language)
    g_news.search(search_text)
    results=g_news.result()
    return results
    

#df=pd.DataFrame(results)
#print(df.head())

#g_news=GoogleNews(start='08/01/2020',end='08/31/2020')
#g_news=g_news.get__links()

if __name__=='__main__':
    news="Copa Libertadores"
    r = get_google_news(news)
    print(r)
    print(type(r))
